#!/usr/bin/env python3
"""Independent stdlib checks for I4-012..016 and I3-015..019.

Cartesian, surface-graph, and original angular quadratures are compared with
different representations. Analytically justified tail/remainder bounds are
kept explicit; finite numerical agreement does not prove improper convergence,
the principal-value prescription, or differentiation under an integral.
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


def integral(function, a, b, n=2000):
    assert n > 0 and n % 2 == 0
    h = (b-a)/n
    return h/3 * (function(a) + function(b)
                  + 4*sum(function(a+i*h) for i in range(1, n, 2))
                  + 2*sum(function(a+i*h) for i in range(2, n, 2)))


def derivative(function, x=0, h=1e-4):
    return (function(x+h)-function(x-h))/(2*h)


def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def inverse(a):
    work = [list(row)+[float(i == j) for j in range(3)] for i, row in enumerate(a)]
    for j in range(3):
        pivot = max(range(j, 3), key=lambda i: abs(work[i][j]))
        work[j], work[pivot] = work[pivot], work[j]
        value = work[j][j]
        assert abs(value) > 1e-14
        work[j] = [x/value for x in work[j]]
        for i in range(3):
            if i != j:
                multiple = work[i][j]
                work[i] = [work[i][k]-multiple*work[j][k] for k in range(6)]
    return [row[3:] for row in work]


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def shifted(a, h, t):
    return [[a[i][j]+t*h[i][j] for j in range(3)] for i in range(3)]


def quadratic(a, x):
    return sum(x[i]*a[i][j]*x[j] for i in range(3) for j in range(3))


# I4-012: rays in the original Cartesian directions intersect the ellipsoid at
# radius (n^T Q n)^(-1/2). This avoids the solution's Q^(1/2) coordinate map.
radial_gaussian = integral(lambda r: r*r*math.exp(-r*r), 0, 1)
ball_gaussian = math.pi**1.5*math.erf(1)-2*math.pi/math.e


def ellipsoid_gaussian(q):
    def latitude(theta):
        s, c = math.sin(theta), math.cos(theta)
        return s*integral(lambda phi: quadratic(q, (s*math.cos(phi), s*math.sin(phi), c))**-1.5,
                          0, 2*math.pi, n=160)
    return radial_gaussian*integral(latitude, 0, math.pi, n=160)


q0 = [[2, 1, 0], [1, 2, 0], [0, 0, 4]]
qh = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
for index, q in enumerate([q0, [[2, .4, .2], [.4, 1.7, -.3], [.2, -.3, 1.4]],
                         [[1, 0, 0], [0, 1, 0], [0, 0, 1]]]):
    near(f"I4-012 Cartesian rays case {index}", ellipsoid_gaussian(q),
         ball_gaussian/math.sqrt(determinant(q)), tolerance=4e-7)
near("I4-012 moving-domain perturbation", derivative(lambda t: ellipsoid_gaussian(shifted(q0, qh, t))),
     ball_gaussian/(6*math.sqrt(3)), tolerance=8e-7)
for t in [-2.9, -.4, .9]:
    near(f"I4-012 determinant t={t}", determinant(shifted(q0, qh, t)), 4*(4-(1+t)**2))
for t in [-3, 1]:
    near(f"I4-012 excluded SPD endpoint t={t}", determinant(shifted(q0, qh, t)), 0)


# I4-013: original z-sections, cap radial coordinates, and the actual lateral
# tangent cross product check the three distinct oriented flux contributions.
for a, c, height in [(2, 3, 1.5), (.7, .4, 2), (1.2, 1e6, .8)]:
    label = f"I4-013 a,c,H={a,c,height}"
    radius = lambda z: a*math.sqrt(1+(z/c)**2)
    volume = integral(lambda z: math.pi*radius(z)**2, -height, height)
    near(label+" volume", volume, 2*math.pi*a*a*(height+height**3/(3*c*c)))

    def lateral(z):
        r = radius(z)
        rp = a*a*z/(c*c*r)
        return integral(lambda theta: (r*math.cos(theta))**2+(r*math.sin(theta))**2-z*r*rp,
                        0, 2*math.pi, n=24)

    side = integral(lateral, -height, height, n=40)
    near(label+" lateral", side, 4*math.pi*a*a*height)
    caps = []
    for sign in [-1, 1]:
        z = sign*height
        flux = integral(lambda r: 2*math.pi*r*z*sign, 0, radius(z))
        near(label+f" cap {sign}", flux, math.pi*a*a*height*(1+(height/c)**2))
        caps.append(flux)
    near(label+" divergence theorem", side+sum(caps), 3*volume)


# I4-014 and I3-017 use K with PARAMETER m, independently computed by AGM.
def elliptic_k(m):
    assert 0 <= m < 1
    a, b = 1.0, math.sqrt(1-m)
    for _ in range(50):
        if abs(a-b) <= 1e-15*a:
            return math.pi/(2*a)
        a, b = (a+b)/2, math.sqrt(a*b)
    raise AssertionError("elliptic K AGM did not converge")


def elliptic_e(m):
    # Binomial series integrated termwise; different from angular quadrature.
    assert 0 <= m < 1
    coefficient, power, total = 1.0, 1.0, 1.0
    for n in range(1, 10000):
        coefficient *= ((2*n-1)/(2*n))**2
        power *= m
        term = coefficient*power/(2*n-1)
        total -= term
        if term < 1e-16:
            return math.pi*total/2
    raise AssertionError("elliptic E series did not converge")


def ellipse_original(a, b):
    return integral(lambda t: (a*math.cos(t))**2*math.hypot(a*math.sin(t), b*math.cos(t)),
                    0, 2*math.pi, n=4000)


for a, b in [(2, 1.6), (1, .3), (1.4, 1.399), (2, 2)]:
    m = 1-(b/a)**2
    expected = (math.pi*a**3 if m == 0 else
                4*a**3*((2*m-1)*elliptic_e(m)+(1-m)*elliptic_k(m))/(3*m))
    actual = ellipse_original(a, b)
    near(f"I4-014 weighted ellipse {a,b}", actual, expected)
    between(f"I4-014 geometric bounds {a,b}", actual, math.pi*a*a*b, math.pi*a**3)
for m in [.02, .1, .2]:
    a = 1.3
    remainder = ellipse_original(a, a*math.sqrt(1-m))-math.pi*a**3*(1-3*m/8-5*m*m/64)
    bound = 35*math.pi*a**3*m**3/(1024*(1-.2)**2.5)
    between(f"I4-014 controlled Taylor remainder m={m}", remainder, -bound, 0)


# I4-015: direct Cartesian cube quadrature computes normalization and all six
# centered moments, including their original-kernel perturbation derivatives.
# Every tested A has Gershgorin lower bound >= .8; outside [-7,7]^3 the Gaussian
# and degree-four moment tails are < 1e-11. The grid is also refined below.
def gaussian_cartesian(a, h, n=48, extent=7):
    step = 2*extent/n
    # Trapezoidal summation exploits the exponentially small boundary values;
    # Simpson's alternating weights introduce a much coarser Fourier alias.
    grid = [(-extent+i*step, (.5 if i in (0, n) else 1)*step)
            for i in range(n+1)]
    pairs = [(i, j) for i in range(3) for j in range(i, 3)]
    result = [0.0]*14
    for x, wx in grid:
        for y, wy in grid:
            for z, wz in grid:
                point = (x, y, z)
                weight = wx*wy*wz*math.exp(-quadratic(a, point))
                perturbation = -quadratic(h, point)
                result[0] += weight
                result[7] += weight*perturbation
                for index, (i, j) in enumerate(pairs, 1):
                    moment = weight*point[i]*point[j]
                    result[index] += moment
                    result[index+7] += moment*perturbation
    return result


gh = [[.2, 1, .1], [1, -.1, .4], [.1, .4, .3]]
for case, a in enumerate([[[2, .4, .2], [.4, 1.7, -.3], [.2, -.3, 1.4]],
                          [[3, 1, 0], [1, 2, 0], [0, 0, 4]]]):
    numerical = gaussian_cartesian(a, gh)
    inv = inverse(a)
    z = math.pi**1.5/math.sqrt(determinant(a))
    trace = sum(multiply(inv, gh)[i][i] for i in range(3))
    ordered = multiply(multiply(inv, gh), inv)
    near(f"I4-015 Cartesian normalization case {case}", numerical[0], z)
    near(f"I4-015 original-kernel normalization derivative case {case}", numerical[7], -z*trace/2)
    for index, (i, j) in enumerate([(i, j) for i in range(3) for j in range(i, 3)], 1):
        near(f"I4-015 Cartesian moment {case,i,j}", numerical[index], z*inv[i][j]/2)
        near(f"I4-015 covariance {case,i,j}", numerical[index]/numerical[0], inv[i][j]/2)
        near(f"I4-015 noncommuting moment derivative {case,i,j}", numerical[index+7],
             -z*trace*inv[i][j]/4-z*ordered[i][j]/2)
        covariance_slope = (numerical[index+7]*numerical[0]-numerical[index]*numerical[7])/numerical[0]**2
        near(f"I4-015 noncommuting covariance derivative {case,i,j}", covariance_slope, -ordered[i][j]/2)
    between(f"I4-015 perturbation really noncommutes case {case}",
            max(abs(multiply(a, gh)[i][j]-multiply(gh, a)[i][j]) for i in range(3) for j in range(3)),
            .01, 10)
refined = gaussian_cartesian(a, gh, n=56)
near("I4-015 Cartesian grid refinement", max(abs(x-y) for x, y in zip(numerical, refined)), 0)
near("I4-015 specified offdiagonal covariance", inverse(a)[0][1]/2, -.1)
near("I4-015 specified offdiagonal covariance derivative",
     derivative(lambda t: inverse(shifted(a, qh, t))[0][1]/2), -.14)


# I4-016: x=exp(-u/rate) evaluates the ORIGINAL difference quotient, including
# signed/equal exponents. Scaling resolves the tail when both approach -1.
def log_quotient(a, b):
    rate = min(a+1, b+1)
    assert rate > 0
    ar, br = (a+1)/rate, (b+1)/rate
    difference = ar-br
    if difference == 0:
        return 0.0
    sign = math.copysign(1, difference)
    return integral(lambda u: difference if u == 0 else
                    sign*math.exp(-min(ar, br)*u)*(-math.expm1(-abs(difference)*u))/u,
                    0, 40, n=12000)


for a, b in [(0, 1), (2, -.5), (-.8, -.2), (-.4, -.4), (0, 0), (1, 0),
             (-1+2e-5, -1+1e-5), (-1+1e-5, -1+5e-5)]:
    near(f"I4-016 original quotient {a,b}", log_quotient(a, b), math.log((a+1)/(b+1)))
for a, b in [(.2, .7), (-.6, -.3)]:
    near(f"I4-016 a partial {a,b}", derivative(lambda v: log_quotient(v, b), a), 1/(a+1))
    near(f"I4-016 b partial {a,b}", derivative(lambda v: log_quotient(a, v), b), -1/(b+1))
for ratio in [.2, 1, 3]:
    for epsilon in [1e-2, 1e-5]:
        near(f"I4-016 joint-boundary path {ratio,epsilon}",
             log_quotient(-1+ratio*epsilon, -1+epsilon), math.log(ratio))


# I3-015: pole subtraction is performed BEFORE quadrature. It is the stated
# equal-exclusion principal value, not an ordinary integral across the pole.
def dilog_unit(x):
    assert 0 <= x <= 1
    if x == 1:
        return math.pi**2/6
    if x > .5:
        return math.pi**2/6-math.log(x)*math.log1p(-x)-dilog_unit(1-x)
    power, total = x, 0.0
    for n in range(1, 1000):
        term = power/(n*n)
        total += term
        if term < 1e-17:
            return total
        power *= x
    raise AssertionError("dilogarithm series did not converge")


def pv_original(a):
    la = math.log(a)
    def regularized(t):
        w = t+la
        return 1 if abs(w) < 1e-12 else w/math.expm1(w)
    # The omitted regularized t-tail is <= 2/a exp(-40)(41+|ln a|).
    return integral(regularized, 0, 40, n=12000)+la*math.log((1-a)/a)


for a in [.0001, .03, .2, .5, .8, .9999]:
    expected = math.pi**2/3-dilog_unit(a)-math.log(a)**2/2
    tail = 2/a*math.exp(-40)*(41+abs(math.log(a)))
    near(f"I3-015 regularized original kernel a={a}", pv_original(a), expected,
         tolerance=2e-8+tail)
near("I3-015 midpoint exact check", pv_original(.5), math.pi**2/4)
a = .0001
between("I3-015 zero-endpoint renormalized bounds", pv_original(a)+math.log(a)**2/2-math.pi**2/3,
        -a/(1-a), -a, slack=2e-9)
# The ordinary a=1 endpoint integral is independent of the dilogarithm's
# hardcoded endpoint: x=exp(-t) gives t/expm1(t), with removable value one.
endpoint_tail = 41*math.exp(-40)/(1-math.exp(-40))
near("I3-015 ordinary removable endpoint integral",
     integral(lambda t: 1 if t == 0 else t/math.expm1(t), 0, 40, n=12000),
     math.pi**2/6, tolerance=2e-8+endpoint_tail)


# I3-016: original Cartesian height graphs x=+-a sqrt(1-y²/b²-z²/c²),
# regularized at their rim, differ from the author's angular surface chart.
def area_height_graph(a, b, c):
    return 2*b*c*integral(lambda u: integral(
        lambda phi: math.sqrt(u*u+a*a*(1-u*u)*(math.cos(phi)**2/b**2+math.sin(phi)**2/c**2)),
        0, 2*math.pi, n=120), 0, 1, n=120)


def area_angular(a, b, c):
    return 8*integral(lambda theta: integral(lambda phi:
        math.sin(theta)*math.sqrt((b*c*math.sin(theta)*math.cos(phi))**2
                                  +(a*c*math.sin(theta)*math.sin(phi))**2
                                  +(a*b*math.cos(theta))**2), 0, math.pi/2, n=120),
        0, math.pi/2, n=120)


for a, b, c in [(3, 2, 1), (1.2, 1.1, .9), (2, 2, 2)]:
    graph = area_height_graph(a, b, c)
    near(f"I3-016 independent surface graphs {a,b,c}", graph, area_angular(a, b, c))
    near(f"I3-016 physical axis permutation {a,b,c}", graph, area_height_graph(c, a, b))
    between(f"I3-016 area bounds {a,b,c}", graph, 4*math.pi*b*c, 4*math.pi*a*b)
    if a == c:
        near("I3-016 sphere", graph, 4*math.pi*a*a)
    n, m = 13, 17
    dt, dp = math.pi/(2*n), math.pi/(2*m)
    midpoint = 8*dt*dp*sum(
        math.sin((i+.5)*dt)*math.sqrt(
            (b*c*math.sin((i+.5)*dt)*math.cos((j+.5)*dp))**2
            +(a*c*math.sin((i+.5)*dt)*math.sin((j+.5)*dp))**2
            +(a*b*math.cos((i+.5)*dt))**2)
        for i in range(n) for j in range(m))
    bound = math.pi**3*a*b/4*(math.sqrt(2)/n+1/m)
    between(f"I3-016 certified midpoint error {a,b,c}", abs(graph-midpoint), 0, bound)


# I3-017: the original ring-angle kernel is compared with the AGM, including
# both sides of the ring, the axis, reflection, and a near-source observation.
def ring_original(a, rho, z):
    delta2 = (a-rho)**2+z*z
    return integral(lambda theta: 1/math.sqrt(delta2+4*a*rho*math.sin(theta/2)**2),
                    0, 2*math.pi, n=24000)


for a, rho, z in [(2, 0, 0), (2, 0, -3), (1, .3, .4), (1, 1.4, -.2),
                  (1, 1, .02), (1, .98, 0)]:
    d = math.hypot(a+rho, z)
    delta = math.hypot(a-rho, z)
    m = 4*a*rho/(d*d)
    actual = ring_original(a, rho, z)
    near(f"I3-017 original ring {a,rho,z}", actual, 4*elliptic_k(m)/d)
    between(f"I3-017 geometric bounds {a,rho,z}", actual, 2*math.pi/d, 2*math.pi/delta)
    if rho == 0:
        near(f"I3-017 on-axis {a,z}", actual, 2*math.pi/math.hypot(a, z))
    near(f"I3-017 z reflection {a,rho,z}", actual, ring_original(a, rho, -z))
for delta in [.01, .001]:
    # Vertical approach avoids a linear change in d. AGM resolves the narrow
    # singular peak; this comparison checks the logarithmic coefficient/constant.
    d = math.hypot(2, delta)
    actual = 4*elliptic_k(1-delta*delta/(d*d))/d
    leading = 2*math.log(8/delta)
    near(f"I3-017 near-ring logarithm delta={delta}", actual, leading, tolerance=delta**1.5)


# I3-018: integrate in the original y coordinate analytically, then x by
# quadrature, and compare against the Duffy radial primitives.
def panel_cartesian(h, alpha, beta, gamma):
    def strip(x):
        if x == 0 and h == 0:
            return alpha*math.asinh(1)
        base = math.hypot(x, h)
        return ((alpha+beta*x)*math.asinh(x/base)
                + gamma*(math.sqrt(2*x*x+h*h)-base))
    return integral(strip, 0, 1, n=8000)


def panel_radial(h, alpha, beta, gamma):
    if h == 0:
        return (alpha+beta/2)*math.asinh(1)+gamma*(math.sqrt(2)-1)/2
    def integrand(v):
        c2 = 1+v*v
        root = math.sqrt(c2+h*h)
        a0 = 1/(root+h)
        a1 = root/(2*c2)-h*h*math.asinh(math.sqrt(c2)/h)/(2*c2**1.5)
        return alpha*a0+(beta+gamma*v)*a1
    return integral(integrand, 0, 1)


for weights in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-2, 3, -4), (0, -2, 3), (0, 0, 0)]:
    for h in [0, .03, .7]:
        near(f"I3-018 original Cartesian panel {weights,h}", panel_cartesian(h, *weights),
             panel_radial(h, *weights))
    alpha, beta, gamma = weights
    h = .002
    residual = abs(panel_cartesian(h, *weights)-panel_cartesian(0, *weights)+math.pi*alpha*h/4)
    bound = h*h/2*(abs(alpha)+(abs(beta)+abs(gamma))*math.asinh(math.sqrt(2)/h))
    between(f"I3-018 derivative remainder {weights}", residual, 0, bound, slack=2e-9)


# I3-019: finite original-coordinate quadrature is compared with independently
# summed Fresnel series. Large-parameter and infinite-domain checks explicitly
# retain their proved remainder/tail bounds, rather than quadraturing infinity.
def fresnel_series(z):
    term, total = complex(z), complex(z)
    for n in range(1, 1000):
        term *= (1j*math.pi*z*z/2)/n*(2*n-1)/(2*n+1)
        total += term
        if abs(term) < 1e-17:
            return total
    raise AssertionError("Fresnel series did not converge")


def fresnel_original(k, a):
    return 2*integral(lambda x: cmath.exp(1j*k*x*x), 0, a, n=24000)


for k, a in [(1e-5, 1.2), (.3, .7), (1, 1), (2, 1.2)]:
    actual = fresnel_original(k, a)
    exact = math.sqrt(2*math.pi/k)*fresnel_series(a*math.sqrt(2*k/math.pi))
    near(f"I3-019 finite Fresnel normalization {k,a}", actual, exact)
    between(f"I3-019 magnitude bound {k,a}", abs(actual), 0, 2*a)
    if k < .001:
        between("I3-019 controlled small-k expansion", abs(actual-2*a-2j*k*a**3/3),
                0, k*k*a**5/5, slack=2e-12)
near("I3-019 continuous k=0 value", fresnel_original(0, 1.2), 2.4)
near("I3-019 negative-k conjugation", fresnel_original(-2, 1.2), fresnel_original(2, 1.2).conjugate())
for k, a in [(10, 1), (40, .7), (100, 1.2)]:
    actual = fresnel_original(k, a)
    leading = math.sqrt(math.pi/k)*cmath.exp(1j*math.pi/4)+cmath.exp(1j*k*a*a)/(1j*k*a)
    between(f"I3-019 controlled stationary+endpoint remainder {k,a}", abs(actual-leading),
            0, 1/(k*k*a**3), slack=2e-10)
for epsilon, k in [(.5, 1), (.1, 3)]:
    extent = math.sqrt(40/epsilon)
    truncated = 2*integral(lambda x: cmath.exp(-(epsilon-1j*k)*x*x), 0, extent, n=24000)
    tail = math.exp(-epsilon*extent**2)/(epsilon*extent)
    near(f"I3-019 absolutely convergent damped Gaussian {epsilon,k}", truncated,
         math.sqrt(math.pi)/cmath.sqrt(epsilon-1j*k), tolerance=2e-8+tail)
for epsilon in [0, .01, .3]:
    a, b, k = 2, 15, 3
    finite_tail = integral(lambda x: cmath.exp((-epsilon+1j*k)*x*x), a, b, n=24000)
    between(f"I3-019 uniform finite-tail bound epsilon={epsilon}", abs(finite_tail), 0, 1/(k*a))


print(f"{checks} independent integration expansion 2 checks passed")
