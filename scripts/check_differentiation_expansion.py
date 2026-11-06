#!/usr/bin/env python3
"""Independent numerical checks for the 2026-11 differentiation additions.

Original objectives, Newton solves, four-index contractions, direct inverses,
and a full matrix exponential series supply independent numerical evaluations.
These finite-difference spot checks supplement the analytical domain arguments;
they do not prove differentiability, asymptotics, or convergence.
Only Python's standard library is needed.
"""

import cmath
import math


checks = 0


def near(identifier, actual, expected, tol=2e-7):
    global checks
    if not (math.isfinite(abs(actual)) and math.isfinite(abs(expected))
            and math.isfinite(tol) and tol >= 0):
        raise AssertionError(f"{identifier}: nonfinite comparison or invalid tolerance")
    if not abs(actual - expected) <= tol * max(1, abs(expected)):
        raise AssertionError(f"{identifier}: {actual!r} != {expected!r}")
    checks += 1


def require(identifier, condition, message):
    global checks
    if not condition:
        raise AssertionError(f"{identifier}: {message}")
    checks += 1


def derivative(f, t, h=1e-5):
    return (f(t + h) - f(t - h)) / (2 * h)


def second(f, t, h=2e-4):
    return (f(t + h) - 2 * f(t) + f(t - h)) / h**2


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def eye(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    return [dot(row, x) for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def inverse(a):
    """Pivoted elimination, independently of rank-one or 2x2 formulas."""
    n = len(a)
    aug = [list(row) + ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(aug[i][j]))
        if abs(aug[pivot][j]) < 1e-13:
            raise ArithmeticError("singular matrix in independent inverse")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        scale = aug[j][j]
        aug[j] = [x / scale for x in aug[j]]
        for i in range(n):
            if i != j:
                scale = aug[i][j]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def matrix_exp(a):
    """Full matrix series: does not use A^2=-tI or scalar C/S formulas."""
    result = eye(len(a))
    term = eye(len(a))
    for n in range(1, 160):
        term = [[x / n for x in row] for row in mm(term, a)]
        result = [[x + y for x, y in zip(r, s)]
                  for r, s in zip(result, term)]
        if max(abs(x) for row in term for x in row) < 1e-17:
            return result
    raise ArithmeticError("matrix exponential series did not converge")


def bounded_maximum(f):
    """Golden-section optimization on [0,1], retaining both boundary values."""
    a, b = 0.0, 1.0
    ratio = (math.sqrt(5) - 1) / 2
    c, d = b - ratio * (b - a), a + ratio * (b - a)
    for _ in range(90):
        if f(c) < f(d):
            a, c = c, d
            d = a + ratio * (b - a)
        else:
            b, d = d, c
            c = b - ratio * (b - a)
    return max(f(0), f(1), f((a + b) / 2))


# D4-007: the original value has a differentiable but non-C1 extension.
def oscillating_power(x):
    return math.exp(math.log1p(x * x) * math.sin(1 / x)) if x else 1.0


def oscillating_slope(x):
    return oscillating_power(x) * (
        2 * x * math.sin(1 / x) / (1 + x * x)
        - math.log1p(x * x) * math.cos(1 / x) / (x * x))


for x in [-1.2, -.3, .07, .4, 2.0]:
    near("D4-007", derivative(oscillating_power, x, 1e-7),
         oscillating_slope(x), 2e-7)
for h in [1e-2, 1e-3, 1e-4]:
    require("D4-007", abs(oscillating_power(h) - 1) <= h * h * (1 + 1e-8),
            "extension value exceeds its exact x^2 bound")
near("D4-007", derivative(oscillating_power, 0, 1e-5), 0, 2e-5)
for n, sign in [(20, -1), (20.5, 1)]:
    x = 1 / (2 * math.pi * n)
    near("D4-007", derivative(oscillating_power, x, 1e-9), sign, 4e-5)


# D4-008: solve the original implicit equation independently by Newton iteration.
def implicit_height(x):
    y = 1.0
    for _ in range(30):
        f = x * math.exp(y) + y * math.exp(x) - 1
        step = f / (x * math.exp(y) + math.exp(x))
        y -= step
        if abs(step) < 1e-15:
            return y
    raise ArithmeticError("D4-008: Newton solve did not converge")


for x in [-.02, 0, .02]:
    y = implicit_height(x)
    fx = math.exp(y) + y * math.exp(x)
    fy = x * math.exp(y) + math.exp(x)
    yp = -fx / fy
    ypp = -(y * math.exp(x) + 2 * (math.exp(y) + math.exp(x)) * yp
            + x * math.exp(y) * yp * yp) / fy
    near("D4-008", derivative(implicit_height, x, 1e-6), yp, 2e-8)
    near("D4-008", second(implicit_height, x, 1e-4), ypp, 4e-6)
near("D4-008", derivative(implicit_height, 0, 1e-6), -(math.e + 1), 2e-8)
near("D4-008", second(implicit_height, 0, 1e-4), 2 * (math.e + 1)**2 - 1, 4e-6)
for x in [-1e-3, 1e-3]:
    polynomial = 1 - (math.e + 1) * x + ((math.e + 1)**2 - .5) * x*x
    residual = x * math.exp(polynomial) + polynomial * math.exp(x) - 1
    require("D4-008", abs(residual) < 100 * abs(x)**3,
            "quadratic substitution leaves a residual larger than O(x^3)")


# D4-009: an independent constrained optimizer checks the piecewise value.
def optimized_value(t):
    return bounded_maximum(lambda x: t * x - x**4)


for t in [-3, 0, .1, 1, 3.8, 4, 7]:
    expected = 0 if t <= 0 else (3 * (t / 4)**(4/3) if t < 4 else t - 1)
    near("D4-009", optimized_value(t), expected, 1e-12)
for t in [-1, .2, 1, 3.5, 5]:
    xp = 0 if t < 0 else ((t / 4)**(1/3) if t < 4 else 1)
    xpp = (t / 4)**(-2/3) / 12 if 0 < t < 4 else 0
    near("D4-009", derivative(optimized_value, t), xp, 2e-8)
    near("D4-009", second(optimized_value, t, 1e-3), xpp, 2e-5)
near("D4-009", derivative(optimized_value, 4, 1e-5), 1, 1e-6)


# D4-010: full matrix exponential values and differences across t=0.
def exponential_input(t):
    return [[0.0, 1.0], [-t, 0.0]]


for t in [-4, -.3, 0, .2, 3]:
    if t > 0:
        c = math.cos(math.sqrt(t))
        s = math.sin(math.sqrt(t)) / math.sqrt(t)
    elif t < 0:
        c = math.cosh(math.sqrt(-t))
        s = math.sinh(math.sqrt(-t)) / math.sqrt(-t)
    else:
        c = s = 1.0
    sp = (c - s) / (2 * t) if t else -1/6
    value = [[c, s], [-t*s, c]]
    slope = [[-s/2, sp], [-(s+c)/2, -s/2]]
    direct = matrix_exp(exponential_input(t))
    for i in range(2):
        for j in range(2):
            near("D4-010", direct[i][j], value[i][j], 2e-12)
            near("D4-010", derivative(
                lambda z: matrix_exp(exponential_input(z))[i][j], t),
                slope[i][j], 3e-8)
    near("D4-010", direct[0][0]*direct[1][1] - direct[0][1]*direct[1][0],
         1, 2e-11)
near("D4-010", derivative(lambda z: matrix_exp(exponential_input(z))[0][1], 0),
     -1/6, 2e-8)
wrong = mm(matrix_exp(exponential_input(0)), [[0, 0], [-1, 0]])
require("D4-010", abs(wrong[0][1] + 1/6) > .1,
        "scalar exponential derivative was accidentally accepted")


# D4-011: independent entry elimination checks symmetric parameter gradients.
def matrix_objective(a):
    ainv = inverse(a)
    return math.log(a[0][0]*a[1][1] - a[0][1]*a[1][0]) + ainv[0][0] + ainv[1][1]


for a, b, c in [(2, .3, 3), (.2, .1, 4), (1, -.8, 1)]:
    delta = a*c - b*b
    expected = [(c+1)/delta - c*(a+c)/delta**2,
                -2*b/delta + 2*b*(a+c)/delta**2,
                (a+1)/delta - a*(a+c)/delta**2]
    pars = [a, b, c]
    for j in range(3):
        def f(z):
            p = pars.copy()
            p[j] = z
            return matrix_objective([[p[0], p[1]], [p[1], p[2]]])
        near("D4-011", derivative(f, pars[j], 1e-6), expected[j], 2e-7)
    direct_entry = derivative(lambda z: matrix_objective([[a, z], [b, c]]), b, 1e-6)
    near("D4-011", expected[1], 2 * direct_entry, 2e-7)


# D3-008: eliminate the perturbed full matrix rather than using rank-one inversion.
base = [[3, .4, .1], [.4, 2, .2], [.1, .2, 1.5]]
bvec, uvec = [1, -.4, 2], [.3, 1, -.6]
base_inv = inverse(base)
wu = mv(base_inv, uvec)
alpha, beta = dot(uvec, wu), dot(bvec, wu)
gamma = dot(bvec, mv(base_inv, bvec))


def rank_one_matrix(t, u=uvec):
    return [[base[i][j] + t*u[i]*u[j] for j in range(3)] for i in range(3)]


def rank_one_response(t, b=bvec, u=uvec):
    return dot(b, mv(inverse(rank_one_matrix(t, u)), b))


for scaled_t in [-3, -.5, 0, 1, 4]:
    t, h = scaled_t / alpha, 1e-4 / max(1, alpha)
    near("D3-008", rank_one_response(t), gamma - t*beta**2/(1+alpha*t), 2e-11)
    near("D3-008", derivative(rank_one_response, t, h),
         -beta**2/(1+alpha*t)**2, 2e-7)
    near("D3-008", second(rank_one_response, t, h),
         2*alpha*beta**2/(1+alpha*t)**3, 2e-6)
pole = -1 / alpha
for value in mv(rank_one_matrix(pole), wu):
    near("D3-008", value, 0, 1e-12)
compatible_b = [1, -wu[0]/wu[1], 0]
compatible_value = dot(compatible_b, mv(base_inv, compatible_b))
for t in [-3/alpha, 0, 1/alpha, pole + 1e-4/alpha]:
    near("D3-008", rank_one_response(t, compatible_b), compatible_value, 2e-9)
for t in [-100, 0, 100]:
    near("D3-008", rank_one_response(t, u=[0, 0, 0]), gamma, 1e-12)
near("D3-008", rank_one_response(pole + 1e-6/alpha) * (1e-6/alpha),
     beta**2/alpha**2, 3e-5)


# D3-009: all 81 tensor slots, with anisotropy and off-diagonal multiplicity.
tensor = {}
for i, value in enumerate([2, 3, 4]):
    tensor[i, i, i, i] = value
tensor[0, 0, 1, 1] = tensor[1, 1, 0, 0] = .5
for key in [(0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 1, 0)]:
    tensor[key] = 5


def strain(t):
    return [[t, t*t, 0], [t*t, math.exp(t), 0], [0, 0, math.sin(t)]]


def tensor_energy(t):
    e = strain(t)
    return .5 * sum(tensor.get((i, j, k, l), 0)*e[i][j]*e[k][l]
                    for i in range(3) for j in range(3)
                    for k in range(3) for l in range(3))


for t in [-.4, 0, .6]:
    value = t*t + 1.5*math.exp(2*t) + 2*math.sin(t)**2 + .5*t*math.exp(t) + 10*t**4
    slope = 2*t + 3*math.exp(2*t) + 4*math.sin(t)*math.cos(t) + .5*(t+1)*math.exp(t) + 40*t**3
    curvature = 2 + 6*math.exp(2*t) + 4*math.cos(2*t) + .5*(t+2)*math.exp(t) + 120*t*t
    near("D3-009", tensor_energy(t), value, 1e-12)
    near("D3-009", derivative(tensor_energy, t), slope, 2e-8)
    near("D3-009", second(tensor_energy, t, 1e-4), curvature, 3e-6)


# D3-010: multiply the rotation matrices before taking differences.
def anisotropy(t, a=2, b=5):
    r = [[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]]
    return mm(mm(r, [[a, 0], [0, b]]), transpose(r))


xvec = [.4, -1.2]
for t in [-2, 0, .7, 4]:
    a, b = 2, 5
    direct = anisotropy(t)
    expected = [[-(a-b)*math.sin(2*t), (a-b)*math.cos(2*t)],
                [(a-b)*math.cos(2*t), (a-b)*math.sin(2*t)]]
    for i in range(2):
        for j in range(2):
            near("D3-010", derivative(lambda z: anisotropy(z)[i][j], t),
                 expected[i][j], 2e-8)
            near("D3-010", derivative(lambda z: anisotropy(z, 3, 3)[i][j], t),
                 0, 2e-9)
    near("D3-010", derivative(lambda z: dot(xvec, mv(anisotropy(z), xvec)), t),
         (a-b)*((xvec[1]**2-xvec[0]**2)*math.sin(2*t)
                + 2*xvec[0]*xvec[1]*math.cos(2*t)), 2e-8)
    near("D3-010", direct[0][0] + direct[1][1], a+b, 1e-12)
    near("D3-010", direct[0][0]*direct[1][1] - direct[0][1]*direct[1][0], a*b, 1e-12)


# D3-011: direct normalization, finite differences, and differentiated norm identities.
def normalized(t):
    v = [math.exp(t), math.sin(t), t]
    radius = math.sqrt(dot(v, v))
    return [x/radius for x in v]


for t in [-3, -.4, 0, .7, 3]:
    v = [math.exp(t), math.sin(t), t]
    w, z = [math.exp(t), math.cos(t), 1], [math.exp(t), -math.sin(t), 0]
    r = math.sqrt(dot(v, v))
    p, q = dot(v, w), dot(w, w) + dot(v, z)
    first = [w[i]/r - p*v[i]/r**3 for i in range(3)]
    sec = [z[i]/r - 2*p*w[i]/r**3 - q*v[i]/r**3 + 3*p*p*v[i]/r**5
           for i in range(3)]
    for i in range(3):
        near("D3-011", derivative(lambda z: normalized(z)[i], t), first[i], 3e-8)
        near("D3-011", second(lambda z: normalized(z)[i], t), sec[i], 3e-6)
    n = normalized(t)
    near("D3-011", dot(n, n), 1, 1e-12)
    near("D3-011", dot(n, first), 0, 1e-12)
    near("D3-011", dot(n, sec), -dot(first, first), 1e-11)


# D3-012: original complex radial quotient and the exceptional k=0 extension.
def radial(r, k):
    return (cmath.exp(-1j*k*r) - 1)/r if r else -1j*k


for k in [0, .5, -2, 3]:
    for r in [.1, .7, 2]:
        expected = (1 - (1 + 1j*k*r)*cmath.exp(-1j*k*r))/r**2
        near("D3-012", derivative(lambda z: radial(z, k), r, 1e-6), expected, 2e-8)
    h = 1e-5
    near("D3-012", (radial(h, k) - radial(0, k))/h, -k*k/2, 6e-5)
    near("D3-012", (radial(abs(-h), k) - radial(0, k))/(-h), k*k/2, 6e-5)
for p in [[0, 0, 0], [.1, -.2, .3], [3, 1, 2]]:
    near("D3-012", radial(math.sqrt(dot(p, p)), 0), 0, 1e-12)


print(f"{checks} independent differentiation-expansion numerical checks passed.")
