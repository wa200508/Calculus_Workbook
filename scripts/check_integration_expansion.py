#!/usr/bin/env python3
"""Independent numerical checks for I4-007..011 and I3-010..014.

Only Python's standard library is required. Original-coordinate quadrature and
independent representations supplement the analytical review; numerical checks
do not prove domain, convergence, or interchange assertions. Explicit improper
tail bounds are retained in the comparisons rather than treated as quadrature.
"""

import cmath
import math


checks = 0


def near(label, actual, expected, tolerance=2e-7):
    global checks
    if not (math.isfinite(abs(actual)) and math.isfinite(abs(expected))
            and math.isfinite(tolerance) and tolerance >= 0):
        raise AssertionError(f"{label}: nonfinite comparison or invalid tolerance")
    error = abs(actual - expected)
    allowed = tolerance * max(1, abs(expected))
    if not error <= allowed:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}; error {error:g} > {allowed:g}")
    checks += 1


def between(label, actual, lower, upper, slack=2e-10):
    global checks
    if not (all(math.isfinite(value) for value in (actual, lower, upper, slack))
            and lower <= upper and slack >= 0):
        raise AssertionError(f"{label}: nonfinite interval comparison or invalid bounds/slack")
    if not lower - slack <= actual <= upper + slack:
        raise AssertionError(f"{label}: {actual!r} outside [{lower!r}, {upper!r}]")
    checks += 1


def integral(function, a, b, n=4000):
    assert n > 0 and n % 2 == 0
    h = (b - a) / n
    return h / 3 * (
        function(a) + function(b)
        + 4 * sum(function(a + i*h) for i in range(1, n, 2))
        + 2 * sum(function(a + i*h) for i in range(2, n, 2))
    )


def derivative(function, x, h=1e-4):
    return (function(x+h) - function(x-h)) / (2*h)


def second_derivative(function, x, h=1e-3):
    return (function(x+h) - 2*function(x) + function(x-h)) / h**2


# I4-007: original z-coordinate sections, each a circular segment in the
# scaled x,y disk. The slicing direction differs from the cap's plane normal.
def cap_by_z_sections(axes, normal, offset):
    a, b, c = axes
    m1, m2, m3 = (axes[i]*normal[i] for i in range(3))
    transverse = math.hypot(m1, m2)
    assert transverse > 0

    def section(w):
        radius_squared = max(0, 1-w*w)
        if radius_squared == 0:
            return 0
        radius = math.sqrt(radius_squared)
        cut = (offset-m3*w) / transverse
        if cut <= -radius:
            return math.pi*radius_squared
        if cut >= radius:
            return 0
        return (radius_squared*math.acos(cut/radius)
                - cut*math.sqrt(max(0, radius_squared-cut*cut)))

    return a*b*c*integral(section, -1, 1, n=12000)


def cap_formula(axes, normal, offset):
    rho = math.sqrt(sum((axes[i]*normal[i])**2 for i in range(3)))
    abc = math.prod(axes)
    eta = offset/rho
    if eta <= -1:
        return 4*math.pi*abc/3
    if eta >= 1:
        return 0
    return math.pi*abc*(1-eta)**2*(2+eta)/3


axes, normal = (2, 3, 4), (1, -.7, .5)
rho = math.sqrt(sum((axes[i]*normal[i])**2 for i in range(3)))
for eta in [-1.3, -1, -.6, 0, .35, 1, 1.3]:
    near(f"I4-007 cap eta={eta}", cap_by_z_sections(axes, normal, eta*rho),
         cap_formula(axes, normal, eta*rho), tolerance=3e-7)
for eta in [-.5, 0, .6]:
    slope = derivative(lambda h: cap_by_z_sections(axes, normal, h), eta*rho, h=1e-3)
    near(f"I4-007 section derivative eta={eta}", slope,
         -math.pi*math.prod(axes)*(1-eta*eta)/rho, tolerance=3e-5)


# I4-008: x=tan(theta) maps the original improper integral to a smooth finite
# one. This does not perform the partial-fraction subtraction under review.
def quadratic_poles(a, b):
    return integral(
        lambda theta: math.cos(theta)**2 / (
            (math.sin(theta)**2 + a*a*math.cos(theta)**2)
            * (math.sin(theta)**2 + b*b*math.cos(theta)**2)),
        0, math.pi/2, n=8000)


for a, b in [(.3, 2), (1, 1), (1, 1+1e-8), (2, .7)]:
    expected = math.pi/(2*a*b*(a+b))
    near(f"I4-008 a={a} b={b}", quadratic_poles(a, b), expected, tolerance=2e-9)
    near(f"I4-008 partial a={a} b={b}",
         derivative(lambda t: quadratic_poles(t, b), a, h=1e-5),
         -expected*(1/a+1/(a+b)), tolerance=2e-7)


# I4-009: entrywise quadrature of the original matrix resolvent after
# s=u/(1-u). If B=(1-u)A+uI, then R(s)^2 ds=B^-2 du; the endpoint is I.
def inverse2(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[a[1][1]/det, -a[0][1]/det], [-a[1][0]/det, a[0][0]/det]]


def product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def add(a, b, multiplier=1):
    return [[a[i][j]+multiplier*b[i][j] for j in range(2)] for i in range(2)]


def matrix_integral(a):
    def entry(u, i, j):
        b = [[(1-u)*a[r][s] + (u if r == s else 0) for s in range(2)] for r in range(2)]
        bi = inverse2(b)
        return product(bi, bi)[i][j]
    return [[integral(lambda u: entry(u, i, j), 0, 1, n=2000)
             for j in range(2)] for i in range(2)]


perturbation = [[.4, .7], [.7, -.2]]
for case, a in enumerate([[[2, .3], [.3, 1.4]], [[1, 0], [0, 3]], [[2, 0], [0, 2]]]):
    ai = inverse2(a)
    accumulated = matrix_integral(a)
    expected_slope = product(product(ai, perturbation), ai)
    step = 1e-4
    positive = matrix_integral(add(a, perturbation, step))
    negative = matrix_integral(add(a, perturbation, -step))
    for i in range(2):
        for j in range(2):
            near(f"I4-009 matrix {case} entry {i},{j}", accumulated[i][j], ai[i][j], tolerance=2e-9)
            near(f"I4-009 perturbation {case} entry {i},{j}",
                 (positive[i][j]-negative[i][j])/(2*step), -expected_slope[i][j], tolerance=2e-8)
    if case < 2:
        commutator = add(product(a, perturbation), product(perturbation, a), -1)
        between(f"I4-009 case {case} is noncommuting", max(abs(x) for row in commutator for x in row), .1, 10)


# I4-010: keep the original variable and signed endpoint order when t<-L.
length = 1.2
gaussian_original = lambda t: integral(lambda x: math.exp(-(x-t)**2), -length, t, n=4000)
for t in [-4, -length, -.3, 1.7]:
    near(f"I4-010 original t={t}", gaussian_original(t), math.sqrt(math.pi)/2*math.erf(t+length), tolerance=2e-10)
    near(f"I4-010 first t={t}", derivative(gaussian_original, t), math.exp(-(t+length)**2), tolerance=2e-8)
    near(f"I4-010 second t={t}", second_derivative(gaussian_original, t),
         -2*(t+length)*math.exp(-(t+length)**2), tolerance=2e-6)
for signed_distance in [-3, 3]:
    value = gaussian_original(signed_distance-length)
    limit = math.copysign(math.sqrt(math.pi)/2, signed_distance)
    between(f"I4-010 signed tail {signed_distance}", abs(value-limit), 0,
            math.exp(-signed_distance**2)/(2*abs(signed_distance)), slack=2e-12)


# I4-011: direct original angular/radial quadrature versus an independently
# evaluated entire Bessel series, including q=0 and negative wavenumbers.
def bessel_j1(z):
    term = z/2
    total = term
    for m in range(1, 200):
        term *= -z*z/(4*m*(m+1))
        total += term
        if abs(term) < 1e-17:
            return total
    raise AssertionError("I4-011 Bessel series did not converge")


def aperture_original(q, radius):
    return integral(lambda r: r*integral(lambda theta: cmath.exp(1j*q*r*math.cos(theta)),
                                        0, 2*math.pi, n=240), 0, radius, n=160)


radius = 1.3
for q in [0, .01, .5, -.7, 3]:
    actual = aperture_original(q, radius)
    expected = math.pi*radius**2 if q == 0 else 2*math.pi*radius*bessel_j1(q*radius)/q
    near(f"I4-011 q={q}", actual, expected, tolerance=2e-8)
for q in [.05, .4, -.6]:
    actual = aperture_original(q, radius).real
    quadratic = math.pi*radius**2-math.pi*radius**4*q*q/8
    between(f"I4-011 remainder q={q}", actual-quadratic, 0, math.pi*radius**6*q**4/192, slack=2e-9)


# I3-010: original x-coordinate quadrature. The explicit positive tail has
# width at most 1/R, so the finite integral is compared with an interval.
cutoff = 2000
for a in [0, .02, .5, -1, 2]:
    actual = integral(lambda x: a*a if x == 0 else (math.sin(a*x)/x)**2,
                      0, cutoff, n=200000)
    between(f"I3-010 a={a}", math.pi*abs(a)/2-actual, 0, 1/cutoff, slack=2e-8)
for a in [.5, -1, 2]:
    differentiated = integral(lambda x: 2*a if x == 0 else math.sin(2*a*x)/x,
                              0, cutoff, n=200000)
    # Oscillatory integration by parts gives a uniform derivative tail bound
    # on neighborhoods separated from a=0, without absolute integrability.
    between(f"I3-010 derivative tail a={a}",
            abs(differentiated-math.copysign(math.pi/2, a)),
            0, 1/(abs(a)*cutoff), slack=2e-8)


# I3-011: x=exp(-t) converts the original logarithmic integral without using
# its geometric series. Retain both the exponential quadrature tail and the
# integral-comparison bounds for the independent zeta sum.
cutoff = 40
log_moment = integral(lambda t: t*t/(math.exp(t)+1), 0, cutoff, n=20000)
moment_tail = (cutoff**2+2*cutoff+2)*math.exp(-cutoff)
terms = 10000
zeta_sum = math.fsum(1/k**3 for k in range(1, terms+1))
between("I3-011 zeta interval", log_moment,
        1.5*(zeta_sum+1/(2*(terms+1)**2))-moment_tail,
        1.5*(zeta_sum+1/(2*terms**2)), slack=2e-10)
for n in [1, 2, 5, 10]:
    partial = 2*sum((-1)**(k-1)/k**3 for k in range(1, n+1))
    between(f"I3-011 remainder N={n}", (-1)**n*(log_moment-partial),
            1/(n+1)**3, 2/(n+1)**3, slack=moment_tail+2e-10)


# I3-012: quadrature in the original x coordinate resolves the narrow layer.
for a in [2, .5, .1, .01, .001]:
    n = max(4000, 2*math.ceil(20/a))
    actual = integral(lambda x: a/(x*x+a*a), 0, 1, n=n)
    near(f"I3-012 a={a}", actual, math.atan(1/a), tolerance=2e-8)
for a in [.1, .5, 2]:
    numerical_slope = derivative(lambda t: integral(lambda x: t/(x*x+t*t), 0, 1), a)
    near(f"I3-012 derivative a={a}", numerical_slope, -1/(1+a*a), tolerance=2e-8)
for a in [.1, .3, .8]:
    actual = integral(lambda x: a/(x*x+a*a), 0, 1)
    cubic = math.pi/2-a+a**3/3
    between(f"I3-012 cubic remainder a={a}", actual-cubic, -a**5/5, 0)
a = .001
for multiple in [.5, 2, 10]:
    actual = integral(lambda x: a/(x*x+a*a), 0, multiple*a, n=4000)
    near(f"I3-012 layer M={multiple}", actual, math.atan(multiple), tolerance=2e-9)
delta = .1
outside = integral(lambda x: a/(x*x+a*a), delta, 1)
between("I3-012 fixed outside interval", outside, 0, a/delta)


# I3-013: evaluate F(r(t)) dot r'(t) on the stated parameterized curves.
def circulation(x, y, dx, dy):
    return (-y*dx+x*dy)/(x*x+y*y)


for a, b, direction in [(2, .5, 1), (1, 1, 1), (.1, 3, 1), (2, .5, -1)]:
    actual = integral(lambda t: circulation(a*math.cos(t), direction*b*math.sin(t),
                                            -a*math.sin(t), direction*b*math.cos(t)),
                      0, 2*math.pi, n=12000)
    near(f"I3-013 ellipse {a},{b} orientation {direction}", actual, direction*2*math.pi, tolerance=2e-9)
for center, radius in [(2, .5), (-2, 1), (1.01, 1)]:
    actual = integral(lambda t: circulation(center+radius*math.cos(t), radius*math.sin(t),
                                            -radius*math.sin(t), radius*math.cos(t)),
                      0, 2*math.pi, n=16000)
    near(f"I3-013 displaced center {center}", actual, 0, tolerance=2e-9)


# I3-014: integrate the original y-coordinate analytically first, then remove
# the interior logarithmic x singularity with x=x0 +/- s^2. This construction
# is independent of the source-centered Duffy partition in the manuscript.
def panel_original(x0, y0):
    def transformed(s, direction):
        if s == 0:
            return 0
        distance = s*s
        x = x0+direction*distance
        return 2*s*(math.asinh((x-y0)/distance)+math.asinh(y0/distance))
    return (integral(lambda s: transformed(s, -1), 0, math.sqrt(x0), n=20000)
            + integral(lambda s: transformed(s, 1), 0, math.sqrt(1-x0), n=20000))


def panel_boundary_formula(x0, y0):
    vertices = [(0, 0), (1, 0), (1, 1)]
    result = 0
    for i in range(3):
        w = (vertices[i][0]-x0, vertices[i][1]-y0)
        v = (vertices[(i+1) % 3][0]-x0, vertices[(i+1) % 3][1]-y0)
        edge = (v[0]-w[0], v[1]-w[1])
        edge_length = math.hypot(*edge)
        determinant = w[0]*v[1]-w[1]*v[0]
        height = determinant/edge_length
        projection = (w[0]*edge[0]+w[1]*edge[1])/edge_length
        result += height*(math.asinh((projection+edge_length)/height)-math.asinh(projection/height))
    return result


for x0, y0 in [(.6, .2), (.8, .7), (2/3, 1/3), (.12, .03)]:
    actual = panel_original(x0, y0)
    near(f"I3-014 source {x0},{y0}", actual, panel_boundary_formula(x0, y0), tolerance=2e-7)
near("I3-014 centroid closed expression", panel_original(2/3, 1/3),
     2/3*(math.asinh(1)+math.asinh(2))+2/(3*math.sqrt(2))*math.asinh(3), tolerance=2e-7)


print(f"{checks} integration-expansion quadrature, finite-difference, and domain-case checks passed.")
