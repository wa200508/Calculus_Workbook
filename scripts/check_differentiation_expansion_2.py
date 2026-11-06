#!/usr/bin/env python3
"""Independent numerical spot checks for the second differentiation expansion.

Checks compare original functions, implicit solves, and full matrix operations
with the manuscript's analytic formulas. Finite differences and quadrature do
not replace analytical domain, fold, phase, or concentration arguments.
Only Python's standard library is required.
"""
import cmath
import math

checks = 0


def near(label, actual, expected, tol=2e-7):
    """Reject nonfinite inputs before a relative/absolute numerical comparison."""
    global checks
    try:
        valid = (math.isfinite(abs(actual)) and math.isfinite(abs(expected))
                 and math.isfinite(tol) and tol >= 0)
    except (TypeError, ValueError, OverflowError):
        valid = False
    if not valid:
        raise AssertionError(f"{label}: nonfinite value or invalid tolerance")
    scale = max(1, abs(expected))
    # Scaling before subtraction also avoids overflow for opposite large values.
    error = abs(actual / scale - expected / scale)
    if not math.isfinite(error) or error > tol:
        raise AssertionError(f"{label}: {actual!r} != {expected!r} (tol={tol!r})")
    checks += 1


def require(label, condition, message):
    global checks
    if not condition:
        raise AssertionError(f"{label}: {message}")
    checks += 1


def first(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)


def second(f, x, h=2e-4):
    return (f(x+h)-2*f(x)+f(x-h))/h**2


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(x):
    return math.sqrt(dot(x, x))


def eye(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    return [dot(row, x) for row in a]


def solve(a, b):
    rows = [list(row)+[rhs] for row, rhs in zip(a, b)]
    n = len(rows)
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(rows[i][j]))
        if abs(rows[pivot][j]) < 1e-14:
            raise ArithmeticError("independent solve encountered a singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [x/scale for x in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [x-scale*y for x, y in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def inverse(a):
    return transpose([solve(a, col) for col in eye(len(a))])


def determinant(a):
    rows = [list(row) for row in a]
    result = 1.
    for j in range(len(rows)):
        pivot = max(range(j, len(rows)), key=lambda i: abs(rows[i][j]))
        if abs(rows[pivot][j]) < 1e-15:
            return 0.
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            result = -result
        value = rows[j][j]
        result *= value
        for i in range(j+1, len(rows)):
            factor = rows[i][j]/value
            for k in range(j+1, len(rows)):
                rows[i][k] -= factor*rows[j][k]
    return result


def simpson(f, a, b, n=800):
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+j*h) for j in range(1, n, 2))
                +2*sum(f(a+j*h) for j in range(2, n, 2)))


def coordinate_first(f, x, j, h=1e-6):
    plus, minus = list(x), list(x)
    plus[j] += h
    minus[j] -= h
    return (f(plus)-f(minus))/(2*h)


def coordinate_second(f, x, i, j, h=2e-4):
    if i == j:
        plus, minus = list(x), list(x)
        plus[i] += h
        minus[i] -= h
        return (f(plus)-2*f(x)+f(minus))/h**2
    result = 0.
    for si in [-1, 1]:
        for sj in [-1, 1]:
            point = list(x)
            point[i] += si*h
            point[j] += sj*h
            result += si*sj*f(point)
    return result/(4*h*h)


# D4-012: evaluate the original folded arctangent on all three components.
def folded_angle(x):
    return math.atan(2*x/(1-x*x))


for x in [-3, -1.3, -.7, 0, .5, 1.3, 3]:
    correction = -math.pi if x < -1 else (math.pi if x > 1 else 0.)
    near("D4-012 lift", folded_angle(x)+correction, 2*math.atan(x), 2e-12)
    near("D4-012 derivative", first(folded_angle, x, 1e-6), 2/(1+x*x), 2e-8)
for pole in [-1, 1]:
    near("D4-012 left limit", folded_angle(pole-1e-8), math.pi/2, 2e-8)
    near("D4-012 right limit", folded_angle(pole+1e-8), -math.pi/2, 2e-8)


# D4-013: principal complex argument stays smooth between the actual zeros.
tau = 1.3
response = lambda w: 1-cmath.exp(-1j*w*tau)
for m in [-2, -1, 0, 1]:
    for fraction in [.2, .6, .85]:
        w = 2*math.pi*(m+fraction)/tau
        phase = cmath.phase(response(w))
        near("D4-013 phase", phase, (m+.5)*math.pi-w*tau/2, 2e-12)
        near("D4-013 phase derivative", first(lambda z: cmath.phase(response(z)), w),
             -tau/2, 2e-8)
        ratio = first(response, w)/response(w)
        near("D4-013 logarithmic derivative", ratio,
             tau/(2*math.tan(w*tau/2))-1j*tau/2, 3e-8)
    zero = 2*math.pi*m/tau
    near("D4-013 zero value", response(zero), 0, 2e-12)
    near("D4-013 right zero direction", cmath.phase(response(zero+1e-6)),
         math.pi/2, 2e-6)
    near("D4-013 left zero direction", cmath.phase(response(zero-1e-6)),
         -math.pi/2, 2e-6)


# D4-014: full inversion and determinant elimination along the constrained path.
def unimodular(t):
    return [[1+t*t, t], [t, 1.]]


for t in [-3, -.4, 0, .8, 2]:
    near("D4-014 determinant", determinant(unimodular(t)), 1, 2e-12)
    near("D4-014 log first", first(lambda z: math.log(determinant(unimodular(z))), t),
         0, 2e-8)
    near("D4-014 log second", second(lambda z: math.log(determinant(unimodular(z))), t),
         0, 5e-7)
    slope = [[0., -1.], [-1., 2*t]]
    curvature = [[0., 0.], [0., 2.]]
    for i in range(2):
        for j in range(2):
            f = lambda z: inverse(unimodular(z))[i][j]
            near("D4-014 inverse first", first(f, t), slope[i][j], 3e-8)
            near("D4-014 inverse second", second(f, t), curvature[i][j], 2e-6)
for t in [0., .2, 1., 5., 20.]:
    a = unimodular(t)
    ai = inverse(a)
    def largest(mat):
        v = [1., .3]
        for _ in range(180):
            w = mv(mat, v)
            size = norm(w)
            v = [x/size for x in w]
        return dot(v, mv(mat, v))
    numeric_condition = largest(a)*largest(ai)
    expected = ((math.sqrt(t*t+4)+abs(t))/2)**4
    near("D4-014 spectral condition", numeric_condition, expected, 3e-10)
require("D4-014 ill conditioning", ((math.sqrt(404)+20)/2)**4 > 1e5,
        "constant determinant was mistaken for bounded condition number")


# D4-015: monotone bisection of the original cubic, not a derivative formula.
def upper_cubic(x):
    if x <= -2:
        raise ValueError("D4-015: the strict upper branch requires x>-2")
    lo, hi = 1., max(2., abs(x)+2)
    for _ in range(90):
        mid = (lo+hi)/2
        if mid**3-3*mid < x:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


for x in [-1.5, -.4, 2., 5., 30.]:
    y = upper_cubic(x)
    near("D4-015 original constraint", y**3-3*y, x, 2e-12)
    near("D4-015 first", first(upper_cubic, x), 1/(3*(y*y-1)), 3e-7)
    near("D4-015 second", second(upper_cubic, x), -2*y/(9*(y*y-1)**3), 4e-6)
near("D4-015 regular x=2", upper_cubic(2), 2, 2e-12)
for delta in [1e-3, 1e-4]:
    error = upper_cubic(-2+delta)-1-math.sqrt(delta/3)+delta/18
    require("D4-015 fold remainder", abs(error) <= .02*delta**1.5,
            "the quadratic-in-sqrt(delta) fold expansion fails")
delta = 1e-8
y = upper_cubic(-2+delta)
near("D4-015 fold slope", (1/(3*(y*y-1)))*(2*math.sqrt(3*delta)), 1, 2e-4)
near("D4-015 fold curvature", (-2*y/(9*(y*y-1)**3))*(-4*math.sqrt(3)*delta**1.5),
     1, 2e-4)


# D4-016: original soft absolute value, plus mass and concentration quadrature.
def soft_abs(x, eps):
    return eps*math.log(2*math.cosh(x/eps))


for eps in [.15, .6, 2.]:
    for x in [-1., -.2, 0., .3, 1.]:
        near("D4-016 first", first(lambda z: soft_abs(z, eps), x),
             math.tanh(x/eps), 3e-8)
        near("D4-016 second", second(lambda z: soft_abs(z, eps), x, 1e-4),
             1/(eps*math.cosh(x/eps)**2), 2e-6)
        error = soft_abs(x, eps)-abs(x)
        require("D4-016 uniform error", -1e-13 <= error <= eps*math.log(2)+1e-13,
                "uniform soft-absolute-value error bound fails")
    near("D4-016 sharp error at zero", soft_abs(0, eps), eps*math.log(2), 2e-12)
    mass = simpson(lambda u: 1/math.cosh(u)**2, -14, 14)
    near("D4-016 curvature mass", mass, 2, 3e-10)
    weighted = simpson(lambda u: math.cos(eps*u)/math.cosh(u)**2, -14, 14)
    require("D4-016 concentration test", abs(weighted-2) <= 2*eps*math.log(2)+1e-10,
            "Lipschitz test-function concentration estimate fails")
    for c in [.5, 1., 3.]:
        inner = simpson(lambda x: 1/(eps*math.cosh(x/eps)**2), -c*eps, c*eps)
        near("D4-016 scaled inner mass", inner, 2*math.tanh(c), 2e-10)
for radius in [2., 4., 8.]:
    tail = 2*simpson(lambda u: 1/math.cosh(u)**2, radius, 20, 2400)
    near("D4-016 exact tail", tail, 2*(1-math.tanh(radius)), 2e-10)
    require("D4-016 tail bound", tail <= 4*math.exp(-2*radius)+1e-12,
            "curvature mass did not concentrate at the stated rate")


# D3-013: central differences of the sum of the two original Euclidean norms.
focus = 1.5


def two_focus(x):
    return norm([x[0]-focus, x[1], x[2]]) + norm([x[0]+focus, x[1], x[2]])


for x in [[.3, .4, -.7], [-2., .2, .5], [.2, 0., 0.]]:
    directions = [[x[0]-focus, x[1], x[2]], [x[0]+focus, x[1], x[2]]]
    lengths = [norm(v) for v in directions]
    gradient = [sum(v[j]/r for v, r in zip(directions, lengths)) for j in range(3)]
    hessian = [[sum(float(i == j)/r-v[i]*v[j]/r**3
                    for v, r in zip(directions, lengths)) for j in range(3)]
               for i in range(3)]
    for j in range(3):
        near("D3-013 gradient", coordinate_first(two_focus, x, j), gradient[j], 3e-8)
        for i in range(3):
            near("D3-013 Hessian", coordinate_second(two_focus, x, i, j),
                 hessian[i][j], 3e-6)
    for v in [[1., .2, -.4], [.1, -1., .7]]:
        require("D3-013 convexity", dot(v, mv(hessian, v)) >= -1e-12,
                "a norm-sum Hessian lost positive semidefiniteness")
for s in [-1.4, -.3, 0., 1.2]:
    near("D3-013 stationary segment", two_focus([s, 0, 0]), 2*focus, 2e-12)
    near("D3-013 axial gradient", coordinate_first(two_focus, [s, 0, 0], 0), 0, 2e-8)
for sign in [-1, 1]:
    point = [sign*focus, 0., 0.]
    step = 1e-6
    right = (two_focus([point[0]+step, 0, 0])-two_focus(point))/step
    left = (two_focus([point[0]-step, 0, 0])-two_focus(point))/(-step)
    near("D3-013 focus right slope", right, 1+sign, 3e-8)
    near("D3-013 focus left slope", left, -1+sign, 3e-8)


# D3-014: quotient values, mixed finite differences, and repeated eigenspaces.
def rayleigh(a, x):
    return dot(x, mv(a, x))/dot(x, x)


def rayleigh_derivatives(a, x):
    s = dot(x, x)
    rho = rayleigh(a, x)
    ax = mv(a, x)
    w = [ax[j]-rho*x[j] for j in range(len(x))]
    gradient = [2*z/s for z in w]
    hessian = [[2*(a[i][j]-rho*float(i == j))/s
                -4*(x[i]*w[j]+w[i]*x[j])/s**2 for j in range(len(x))]
               for i in range(len(x))]
    return gradient, hessian


a_rayleigh = [[2., .3, -.2], [.3, 3., .4], [-.2, .4, 1.]]
for x in [[.7, -.4, 1.2], [-1., .5, .3], [.4, .8, -.2]]:
    f = lambda v: rayleigh(a_rayleigh, v)
    gradient, hessian = rayleigh_derivatives(a_rayleigh, x)
    for j in range(3):
        near("D3-014 gradient", coordinate_first(f, x, j), gradient[j], 3e-8)
        for i in range(3):
            near("D3-014 full Hessian", coordinate_second(f, x, i, j),
                 hessian[i][j], 3e-6)
    near("D3-014 homogeneous gradient", dot(x, gradient), 0, 2e-12)
    for actual, expected in zip(mv(hessian, x), [-z for z in gradient]):
        near("D3-014 homogeneous Hessian", actual, expected, 2e-12)
repeated = [[1., 0., 0.], [0., 1., 0.], [0., 0., 4.]]
x = [1., 2., 0.]
gradient, hessian = rayleigh_derivatives(repeated, x)
for value in gradient:
    near("D3-014 repeated-eigenvalue stationarity", value, 0, 2e-12)
for i in range(3):
    for j in range(3):
        near("D3-014 repeated-eigenvalue flatness", hessian[i][j],
             6/dot(x, x) if i == j == 2 else 0, 2e-12)
scalar = [[2*float(i == j) for j in range(3)] for i in range(3)]
gradient, hessian = rayleigh_derivatives(scalar, [.3, -.2, .7])
for value in gradient + [v for row in hessian for v in row]:
    near("D3-014 scalar matrix", value, 0, 2e-12)
near("D3-014 directional origin limit 1", rayleigh(repeated, [1e-8, 0, 0]), 1, 2e-12)
near("D3-014 directional origin limit 2", rayleigh(repeated, [0, 0, 1e-8]), 4, 2e-12)


# D3-015: multiply a full inverse/determinant transport before differencing.
def transport_input(t):
    return [[math.exp(t), t, 0.], [0., 1., t], [0., 0., 1.]]


def transport(t, c):
    f = transport_input(t)
    r = inverse(f)
    d = determinant(f)
    return [[d*z for z in row] for row in mm(mm(r, c), transpose(r))]


for t in [-1., -.2, 0., .7, 1.4]:
    e, em = math.exp(t), math.exp(-t)
    expected = [[em*(-1+2*t-t*t+4*t**3-t**4), -1-3*t*t, 2*t],
                [-1-3*t*t, e*(t+1)**2, -e*(t+1)],
                [2*t, -e*(t+1), e]]
    for i in range(3):
        for j in range(3):
            near("D3-015 explicit derivative", first(lambda z: transport(z, eye(3))[i][j], t),
                 expected[i][j], 3e-8)
    c = [[2., .2, .1], [.2, 1., .15], [.1, .15, 1.5]]
    f = transport_input(t)
    r = inverse(f)
    fp = [[e, 1., 0.], [0., 0., 1.], [0., 0., 0.]]
    ell = mm(r, fp)
    q = transport(t, c)
    left, right = mm(ell, q), mm(q, transpose(ell))
    trace = sum(ell[j][j] for j in range(3))
    invariant = mm(mm(f, q), transpose(f))
    for i in range(3):
        for j in range(3):
            ordered = trace*q[i][j]-left[i][j]-right[i][j]
            near("D3-015 ordered general derivative", first(lambda z: transport(z, c)[i][j], t),
                 ordered, 3e-8)
            near("D3-015 independent congruence", invariant[i][j], e*c[i][j], 3e-11)
    near("D3-015 determinant invariant", determinant(q), e*determinant(c), 3e-10)
    fixed_x = [.3, -.4, .8]
    energy_slope = trace*dot(fixed_x, mv(q, fixed_x))-2*dot(fixed_x, mv(left, fixed_x))
    def spatial_energy(z):
        ft = transpose(transport_input(z))
        spatial_vector = solve(ft, fixed_x)
        return determinant(transport_input(z))*dot(spatial_vector, mv(c, spatial_vector))
    near("D3-015 independent spatial energy", first(spatial_energy, t), energy_slope, 3e-8)


# D3-016: an independent spectral square root, then Sylvester linear solves.
def sqrt_spd2(a):
    center = (a[0][0]+a[1][1])/2
    gap = math.hypot((a[0][0]-a[1][1])/2, a[0][1])
    if center-gap <= 0:
        raise ValueError("D3-016: square-root input must be positive definite")
    angle = .5*math.atan2(2*a[0][1], a[0][0]-a[1][1])
    c, s = math.cos(angle), math.sin(angle)
    rotation = [[c, -s], [s, c]]
    return mm(mm(rotation, [[math.sqrt(center+gap), 0.], [0., math.sqrt(center-gap)]]),
              transpose(rotation))


def sylvester(s, b):
    coefficients = [[2*s[0][0], 2*s[0][1], 0.],
                    [s[0][1], s[0][0]+s[1][1], s[0][1]],
                    [0., 2*s[0][1], 2*s[1][1]]]
    x00, x01, x11 = solve(coefficients, [b[0][0], b[0][1], b[1][1]])
    return [[x00, x01], [x01, x11]]


sqrt_h = [[1., 1.], [1., 2.]]


def sqrt_input(t):
    return [[1+t, t], [t, 4+2*t]]


for t in [-.6, 0., .5, 2.]:
    a = sqrt_input(t)
    s = sqrt_spd2(a)
    x = sylvester(s, sqrt_h)
    xx = mm(x, x)
    y = sylvester(s, [[-2*z for z in row] for row in xx])
    squared = mm(s, s)
    for i in range(2):
        for j in range(2):
            near("D3-016 original root identity", squared[i][j], a[i][j], 3e-12)
            near("D3-016 first Sylvester", first(lambda z: sqrt_spd2(sqrt_input(z))[i][j], t),
                 x[i][j], 3e-8)
            near("D3-016 second Sylvester", second(lambda z: sqrt_spd2(sqrt_input(z))[i][j], t),
                 y[i][j], 6e-6)
    if t == 0:
        expected_x = [[.5, 1/3], [1/3, .5]]
        expected_y = [[-13/36, -2/9], [-2/9, -13/72]]
        for i in range(2):
            for j in range(2):
                near("D3-016 first at zero", x[i][j], expected_x[i][j], 3e-12)
                near("D3-016 second at zero", y[i][j], expected_y[i][j], 3e-12)
lower = math.sqrt(5)-3
require("D3-016 full SPD boundary", determinant(sqrt_input(lower-.01)) < 0,
        "the nonpositive side of the SPD boundary was included")
require("D3-016 negative-definite exclusion", determinant(sqrt_input(-6)) > 0 and 1-6 < 0,
        "positive determinant alone was used as an SPD test")
repeat_h = [[1., .4], [.4, -.5]]
repeat_h2 = mm(repeat_h, repeat_h)
def repeated_root(t):
    return sqrt_spd2([[4*float(i == j)+t*repeat_h[i][j] for j in range(2)] for i in range(2)])
for i in range(2):
    for j in range(2):
        near("D3-016 repeated-eigenvalue first", first(lambda z: repeated_root(z)[i][j], 0),
             repeat_h[i][j]/4, 3e-8)
        near("D3-016 repeated-eigenvalue second", second(lambda z: repeated_root(z)[i][j], 0),
             -repeat_h2[i][j]/32, 3e-7)


# D3-017: independently solve the original scalar radius relation by Newton.
def radial_forward(x):
    return [(1+dot(x, x))*z for z in x]


def radial_inverse(y):
    rho = norm(y)
    if not rho:
        return [0., 0., 0.]
    r = rho if rho < 1 else rho**(1/3)
    for _ in range(30):
        step = (r+r**3-rho)/(1+3*r*r)
        r -= step
        if abs(step) < 1e-15:
            break
    return [r*z/rho for z in y]


for y in [[0., 0., 0.], [.2, .3, -.4], [2., -1., .5], [-3., 2., 1.]]:
    x = radial_inverse(y)
    r2 = dot(x, x)
    alpha, beta = 1+r2, 1+3*r2
    jac = [[alpha*float(i == j)+2*x[i]*x[j] for j in range(3)] for i in range(3)]
    expected = [[float(i == j)/alpha-2*x[i]*x[j]/(alpha*beta)
                 for j in range(3)] for i in range(3)]
    direct_inverse = inverse(jac)
    for j in range(3):
        near("D3-017 original inverse identity", radial_forward(x)[j], y[j], 3e-12)
        for i in range(3):
            numerical = coordinate_first(lambda z: radial_inverse(z)[i], y, j)
            near("D3-017 inverse derivative", numerical, expected[i][j], 3e-8)
            near("D3-017 full inverse matrix", direct_inverse[i][j], expected[i][j], 3e-12)
    near("D3-017 determinant", determinant(jac), alpha*alpha*beta, 3e-12)
    for j in range(3):
        for k in range(3):
            u, v = [expected[i][j] for i in range(3)], [expected[i][k] for i in range(3)]
            composed = [dot(x, v)*u[i]+dot(x, u)*v[i]+dot(u, v)*x[i] for i in range(3)]
            bilinear = [-2*z for z in mv(expected, composed)]
            for i in range(3):
                numerical = coordinate_second(lambda z: radial_inverse(z)[i], y, j, k)
                near("D3-017 second inverse derivative", numerical, bilinear[i], 3e-6)
    if norm(y):
        bound = norm([x[i]-y[i] for i in range(3)])
        require("D3-017 origin error bound", bound <= norm(y)**3+1e-12,
                "the direct Frechet-derivative estimate failed")
point = [2., 0., 0.]
near("D3-017 nonzero radial second check",
     coordinate_second(lambda z: radial_inverse(z)[0], point, 0, 0), -3/32, 3e-7)
near("D3-017 nonzero transverse second check",
     coordinate_second(lambda z: radial_inverse(z)[0], point, 1, 1), -1/8, 3e-7)


if __name__ == "__main__":
    print(f"{checks} independent second-expansion differentiation checks passed.")
