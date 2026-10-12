#!/usr/bin/env python3
"""Independent numerical spot checks for advanced and mixed-set formulas.

Finite differences and quadrature check selected nonsingular inputs; they do
not establish the domain and convergence proofs given in the manuscript.
Only Python's standard library is required.
"""
import math, cmath
checks=0

def near(actual, expected, tol=2e-7):
    global checks
    assert abs(actual-expected)<=tol*max(1,abs(expected)), (actual,expected)
    checks+=1

def derivative(f,x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

def integral(f,a,b,n=20000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*i-1)*h) for i in range(1,n//2+1))+2*sum(f(a+2*i*h) for i in range(1,n//2)))

# Scalar cutoff derivative, tested both near and away from the boundary.
for w in [1.001,1.2,3,20]:
    near(derivative(lambda x:math.sqrt(x*x-1)/2,w,h=1e-7),w/(2*math.sqrt(w*w-1)),tol=2e-6)
# Complex kernel: each spatial partial is compared with a central difference.
for p,k in [([.3,.4,.5],0),([.3,.4,.5],2),([2,-1,3],4)]:
    radius=math.sqrt(sum(x*x for x in p))
    for j in range(3):
        def kernel(t):
            q=p.copy();q[j]=t;r=math.sqrt(sum(x*x for x in q))
            return cmath.exp(-1j*k*r)/(4*math.pi*r)
        near(derivative(kernel,p[j]),-cmath.exp(-1j*k*radius)*(1+1j*k*radius)*p[j]/(4*math.pi*radius**3))
# A nonconstant complex response, differentiated on a smooth phase chart.
for w in [.2,.8,1.3]:
    X=lambda x:1+x*x
    Y=lambda x:math.exp(-x)
    near(derivative(lambda x:math.atan2(Y(x),X(x)),w),(X(w)*(-Y(w))-Y(w)*(2*w))/(X(w)**2+Y(w)**2))
# Ellipsoid graph and its implicit normal.
a,b,c=2,3,4
for x,y in [(.2,.5),(1,.7),(1.7,.1)]:
    g=lambda x,y:c*math.sqrt(1-x*x/a**2-y*y/b**2)
    near(derivative(lambda t:g(t,y),x),-c*x/(a*a*math.sqrt(1-x*x/a**2-y*y/b**2)))
    near(derivative(lambda t:g(x,t),y),-c*y/(b*b*math.sqrt(1-x*x/a**2-y*y/b**2)))
# Hyperboloid tangent orthogonality and area factor.
for u,v in [(0,.3),(.5,1.2),(-1,4)]:
    ch,sh=math.cosh(u),math.sinh(u)
    tu=[a*sh*math.cos(v),a*sh*math.sin(v),c*ch]
    tv=[-a*ch*math.sin(v),a*ch*math.cos(v),0]
    nn=[c*ch*math.cos(v),c*ch*math.sin(v),-a*sh]
    near(sum(tu[j]*nn[j] for j in range(3)),0)
    near(sum(tv[j]*nn[j] for j in range(3)),0)
# Matrix-defined field, including off-diagonal terms.
Q=[[2,.3,.1],[.3,3,.2],[.1,.2,4]]
p=[.4,-.5,.8]
def phi(p):return sum(p[i]*Q[i][j]*p[j] for i in range(3) for j in range(3))**(-.5)
q=phi(p)**(-2)
for j in range(3):
    def field(t):r=p.copy();r[j]=t;return phi(r)
    near(derivative(field,p[j]),-sum(Q[j][i]*p[i] for i in range(3))/q**1.5)
# Matrix solve component derivatives, with varied right-hand sides.
for t in [-.8,-.2,.4,.9]:
    for b1,b2 in [(1,0),(1,1),(1+2j,-.4+.7j)]:
        sol=lambda t:((b1-t*b2)/(1-t*t),(b2-t*b1)/(1-t*t))
        for j,answer in enumerate([(2*t*b1-(1+t*t)*b2)/(1-t*t)**2,(2*t*b2-(1+t*t)*b1)/(1-t*t)**2]):
            near(derivative(lambda v:sol(v)[j],t,h=1e-6),answer)
# Sine substitution and Taylor approximation remainder.
near(integral(math.sin,0,math.pi),2)
for k,L in [(0,2),(.05,3),(-.1,1),(2,1)]:
    val=integral(lambda x:math.sin(k*x)/x if x else k,0,L)
    if abs(k*L)<1:
        assert abs(val-(k*L-k**3*L**3/18))<=abs(k)**5*L**5/600+1e-14
        checks+=1
# Damped oscillation: direct quadrature, exponential tail below 1e-20.
for eps,k in [(1,2),(.4,1),(2,.5)]:
    near(integral(lambda x:math.exp(-eps*x)*(math.sin(k*x)/x if x else k),0,50/eps),math.atan(k/eps),tol=2e-8)
# Complex finite aperture, including phase matching and a sinc zero.
for d,L in [(0,2),(1e-4,3),(-2,1),(2*math.pi,1)]:
    val=integral(lambda z:cmath.exp(1j*d*z),0,L)
    s=d*L/2
    near(val,L*cmath.exp(1j*s)*(math.sin(s)/s if s else 1))
# Line kernel and its differentiated integral.
for rho,L in [(.2,1),(1,2),(4,.5)]:
    near(integral(lambda s:1/math.sqrt(rho*rho+s*s),-L,L),2*math.asinh(L/rho))
    near(integral(lambda s:-rho/(rho*rho+s*s)**1.5,-L,L),-2*L/(rho*math.sqrt(rho*rho+L*L)))
# Independent polar-coordinate evaluation of the weakly singular triangle.
near(integral(lambda theta:1/math.cos(theta),0,math.pi/4),math.log(1+math.sqrt(2)))
# Gaussian radial quadrature compared with the special-function answer.
near(4*math.pi*integral(lambda r:r*r*math.exp(-r*r),0,1),math.pi**1.5*math.erf(1)-2*math.pi/math.e)
# Original surface measure compared with the hyperboloid's closed form.
for U in [.01,.5,1.7]:
    T=math.sinh(U)
    val=2*math.pi*integral(lambda u:math.cosh(u)*math.sqrt(math.cosh(u)**2+math.sinh(u)**2),-U,U)
    near(val,2*math.pi*(T*math.sqrt(1+2*T*T)+math.asinh(math.sqrt(2)*T)/math.sqrt(2)))
# A coupled symmetric cutoff, integrated separately on both sides of the pole.
for pole in [-.4,0,.3]:
    delta=.05
    val=integral(lambda x:1/(x-pole),-1,pole-delta)+integral(lambda x:1/(x-pole),pole+delta,1)
    near(val,math.log((1-pole)/(1+pole)))

# D4-001: simultaneous base/exponent dependence, on both domain components.
for x in [-2,-.3,.2,1.4]:
    f=lambda t:math.exp(math.atan(t)*math.log(math.log1p(t*t)))
    answer=f(x)*(math.log(math.log1p(x*x))/(1+x*x)+2*x*math.atan(x)/((1+x*x)*math.log1p(x*x)))
    near(derivative(f,x),answer)
# D4-002/003: inverse branches and the conjugate-radical simplification.
for x in [-3,-.4,.6,2]:
    near(derivative(lambda t:math.acos(math.tanh(t)),x),-1/math.cosh(x))
    near(derivative(lambda t:-1/math.cosh(t),x),math.sinh(x)/math.cosh(x)**2)
    near(derivative(lambda t:math.log((math.sqrt(1+t*t)+t)/(math.sqrt(1+t*t)-t)),x),2/math.sqrt(1+x*x))
# D4-004: independent graph partials and derivative along the constrained path.
g=lambda x,y:(-x+math.sqrt(2-x*x-2*y*y))/2
for x,y in [(.2,.3),(-.6,.4),(.8,-.2)]:
    D=2-x*x-2*y*y
    near(derivative(lambda v:g(v,y),x),-.5-x/(2*math.sqrt(D)))
    near(derivative(lambda v:g(x,v),y),-y/math.sqrt(D))
for t in [.2,1.4,3.6]:
    near(derivative(lambda v:g(math.cos(v),math.sin(v)/math.sqrt(2)),t),math.sin(t)/2)
# D4-005: complex derivative determines the continuous phase derivative.
for w,tau,T in [(-2,.5,.2),(.3,2,1),(3,1,0)]:
    H=lambda v:(1+1j*v*tau)/(1-1j*v*tau)*cmath.exp(-1j*v*T)
    near((derivative(H,w)/H(w)).imag,2*tau/(1+w*w*tau*tau)-T)
# D4-006: finite differences of the original moving-bound integral.
F=lambda t:integral(lambda z:math.exp(-t*z*z)/(1+z*z),t*t,math.exp(t),n=1000)
for t in [-.4,0,.5]:
    answer=math.exp(t)*math.exp(-t*math.exp(2*t))/(1+math.exp(2*t))-2*t*math.exp(-t**5)/(1+t**4)-integral(lambda z:z*z*math.exp(-t*z*z)/(1+z*z),t*t,math.exp(t),n=1000)
    near(derivative(F,t),answer)
near(derivative(F,0),math.pi/4-.5)
# I4-001: cancellation at zero is evaluated with expm1 for quadrature.
for a,b in [(.4,2),(3,.7),(1,1)]:
    f=lambda x:math.exp(-a*x)*(-math.expm1(-(b-a)*x))/x if x else b-a
    near(integral(f,0,40/min(a,b)),math.log(b/a),tol=2e-7)
# I4-002: original logarithmic integral, parameter derivative, and series.
J=lambda a:integral(lambda x:math.log1p(a*x)/x if x else a,0,1,n=1000)
for a in [-.7,0,.5,3]:
    near(derivative(J,a),math.log1p(a)/a if a else 1)
for a in [-.5,.6]:
    near(J(a),sum((-1)**(n+1)*a**n/n**2 for n in range(1,100)))
# I4-003: original damped oscillatory difference, rather than its derivative.
for a,b,c in [(.7,1,2),(2,0,3),(.4,2,2)]:
    f=lambda x:math.exp(-a*x)*(-2*math.sin((b+c)*x/2)*math.sin((b-c)*x/2))/x if x else 0
    near(integral(f,0,40/a),.5*math.log((a*a+c*c)/(a*a+b*b)))
# I4-004: angular quadrature handles the original endpoint weight.
W=lambda lam:integral(lambda theta:math.log1p(lam*math.cos(theta)),0,math.pi,n=2000)
for lam in [-.95,-.3,0,.5,.98]:
    near(W(lam),math.pi*math.log((1+math.sqrt(1-lam*lam))/2))
# I4-005: direct parametric surface flux on a nonspherical ellipsoid.
# The area vector is the cofactor of the linear sphere map, including sin(theta).
for d,expected in [(0,4*math.pi),(.3,4*math.pi),(3,0)]:
    a,b,c=1,1.3,.8
    def ring(theta):
        def flux(phi):
            x=d+a*math.sin(theta)*math.cos(phi);y=b*math.sin(theta)*math.sin(phi);z=c*math.cos(theta)
            r=math.sqrt(x*x+y*y+z*z)
            area=[b*c*math.sin(theta)**2*math.cos(phi),a*c*math.sin(theta)**2*math.sin(phi),a*b*math.sin(theta)*math.cos(theta)]
            return (x*area[0]+y*area[1]+z*area[2])/r**3
        return integral(flux,0,2*math.pi,n=200)
    near(integral(ring,0,math.pi,n=200),expected,tol=2e-7)
# I4-006: integrate the original Cartesian kernel in y analytically, then x numerically.
K=lambda h:math.asinh(1/math.sqrt(1+h*h))+h*math.atan(h/math.sqrt(2+h*h))-math.pi*h/4
for h in [.01,.2,1,4]:
    near(integral(lambda x:math.asinh(x/math.sqrt(x*x+h*h)),0,1),K(h))
    error=K(h)-math.log1p(math.sqrt(2))+math.pi*h/4
    assert -1e-14<=error<=h*h/(2*math.sqrt(2))+1e-14
    checks+=1
near((K(1e-6)-math.log1p(math.sqrt(2)))/1e-6,-math.pi/4,tol=1e-6)
print(f'{checks} independent finite-difference, quadrature, and geometric checks passed.')
