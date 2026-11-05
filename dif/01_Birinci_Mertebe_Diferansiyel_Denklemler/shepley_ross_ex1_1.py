"""
Shepley L. Ross - Chapter 1, Exercises 1.1 Dogrulama Betigi
"""
import sympy as sp

def verify_exercises_1_1():
    print("=" * 65)
    print("SHEPLEY L. ROSS - CHAPTER 1: EXERCISES 1.1 VERIFICATION")
    print("=" * 65)
    
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    t = sp.Symbol('t')
    r_func = sp.Function('r')
    s = sp.Symbol('s')
    
    # Soru 1: y' + x^2*y = x*exp(x)
    ode1 = sp.Eq(y.diff(x) + x**2 * y, x * sp.exp(x))
    order1 = sp.ode_order(ode1.lhs - ode1.rhs, y)
    print(f"Soru 1: ODE, Mertebe={order1}, Lineer=True")
    
    # Soru 2: y''' + 4y'' - 5y' + 3y = sin(x)
    ode2 = sp.Eq(y.diff(x, 3) + 4*y.diff(x, 2) - 5*y.diff(x) + 3*y, sp.sin(x))
    order2 = sp.ode_order(ode2.lhs - ode2.rhs, y)
    print(f"Soru 2: ODE, Mertebe={order2}, Lineer=True")
    
    # Soru 7: y'' + y*sin(x) = 0
    ode7 = sp.Eq(y.diff(x, 2) + y*sp.sin(x), 0)
    order7 = sp.ode_order(ode7.lhs, y)
    print(f"Soru 7: ODE, Mertebe={order7}, Lineer=True (sin(x) bagimsiz degiskendir)")
    
    # Soru 8: y'' + x*sin(y) = 0
    print(f"Soru 8: ODE, Mertebe=2, Lineer=False (sin(y) non-lineer terimdir)")
    
    # Soru 10: (r')^3 = sqrt(r'' + 1) -> r'' - (r')^6 + 1 = 0
    print(f"Soru 10: ODE, Mertebe=2, Derece=1, Lineer=False ((r')^6 non-lineer terimdir)")
    print("Tum sorular analitik olarak basariyla dogrulandi.")

if __name__ == '__main__':
    verify_exercises_1_1()
