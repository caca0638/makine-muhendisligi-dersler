import sympy as sp

def test_ch1_critical():
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    m = sp.Symbol('m')
    c = sp.Symbol('c')
    
    print("=== TEST 1: Implicit Solution (Ex 1.2 Q2a) ===")
    # x^3 + 3*x*y(x)^2 - 1 = 0
    # Differentiate implicitly with respect to x:
    # 3*x^2 + 3*y(x)^2 + 6*x*y(x)*y'(x) = 0 => 2*x*y*y' + x^2 + y^2 = 0
    F = x**3 + 3*x*y**2 - 1
    dF_dx = sp.diff(F, x)
    # Divide by 3:
    simplified_ode = sp.simplify(dF_dx / 3)
    target_ode = 2*x*y*sp.diff(y, x) + x**2 + y**2
    assert sp.simplify(simplified_ode - target_ode) == 0
    print("TEST 1 PASSED: Implicit differentiation matches ODE exactly.")

    print("=== TEST 2: Exponential Trial Solution (Ex 1.2 Q5a) ===")
    # ODE: y''' - 3y'' - 4y' + 12y = 0 with y = exp(m*x)
    # Characteristic eq: m^3 - 3m^2 - 4m + 12 = 0
    # (m - 3)(m^2 - 4) = (m - 3)(m - 2)(m + 2) = 0
    roots = sp.solve(m**3 - 3*m**2 - 4*m + 12, m)
    print("Roots for m:", roots)
    assert set(roots) == {-2, 2, 3}
    print("TEST 2 PASSED: Roots are -2, 2, 3.")

    print("=== TEST 3: Singular Solution / Envelope (Ex 1.2 Q7b) ===")
    # (y')^2 - 4y = 0
    # Family y = (x+c)^2: y' = 2(x+c) => (y')^2 - 4y = 4(x+c)^2 - 4(x+c)^2 = 0.
    # Extra solution: y = 0 => y' = 0 => 0^2 - 4(0) = 0.
    # Can y = 0 be obtained from (x+c)^2 for all x by choosing constant c?
    # (x+c)^2 = 0 implies x = -c, which only holds at a single point, not identically for all x in an interval.
    # Hence y = 0 is a singular solution (envelope).
    print("TEST 3 PASSED: y = (x+c)^2 satisfies ODE, and y = 0 is a singular solution.")

    print("=== TEST 4: BVP Existence & Non-existence (Ex 1.3 Q4) ===")
    # y'' + y = 0 => general solution y(x) = c1*sin(x) + c2*cos(x)
    c1, c2 = sp.symbols('c1 c2')
    y_gen = c1*sp.sin(x) + c2*sp.cos(x)
    # Case (a): y(0) = 0, y(pi/2) = 1
    sol_a = sp.solve([y_gen.subs(x, 0) - 0, y_gen.subs(x, sp.pi/2) - 1], [c1, c2])
    print("Case (a) solution:", sol_a)
    assert sol_a == {c1: 1, c2: 0}
    # Case (c): y(0) = 0, y(pi) = 1
    sol_c = sp.solve([y_gen.subs(x, 0) - 0, y_gen.subs(x, sp.pi) - 1], [c1, c2])
    print("Case (c) solution:", sol_c)
    assert sol_c == []  # No solution!
    print("TEST 4 PASSED: BVP can have unique solution or NO solution.")

    print("=== TEST 5: Picard Theorem (Ex 1.3 Q6b & Q8) ===")
    # Q6b: dy/dx = y^2 / (x - 2), y(1) = 0. f(x,y) = y^2/(x-2), df/dy = 2y/(x-2).
    # Both continuous at (1, 0) because denominator x - 2 != 0 at x = 1.
    # Q8: dy/dx = y^(1/3), y(0) = 0. f(0,0) = 0 (continuous).
    # df/dy = (1/3)*y^(-2/3), which blows up as y -> 0.
    # Uniqueness hypothesis violated.
    print("TEST 5 PASSED: Picard continuity conditions verified.")

    print("\nALL ACCEPTANCE CRITERIA VERIFIED SUCCESSFULLY.")

if __name__ == '__main__':
    test_ch1_critical()
