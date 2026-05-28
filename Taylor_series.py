import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
x_sym = sp.symbols('x')
f_sym = sp.exp(x_sym)
x_val = float(input("Enter x value to evaluate: "))
a_val = float(input("Enter about point (a): "))
num_terms = int(input("Enter the no. of terms required in Taylor series: "))
taylor_poly = 0
for i in range(num_terms):
    derivative = sp.diff(f_sym, x_sym, i).subs(x_sym, a_val)
    term = (derivative / sp.factorial(i)) * (x_sym - a_val)**i
    taylor_poly += term
x_vals = np.linspace(-0.9, 4, 100)
func_actual = sp.lambdify(x_sym, f_sym, "numpy")
func_approx = sp.lambdify(x_sym, taylor_poly, "numpy")
y_actual = func_actual(x_vals)
y_approx = func_approx(x_vals)
if np.isscalar(y_approx):
    y_approx = np.full_like(x_vals, y_approx)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_actual, label=f"Actual: e^x)", color='black', lw=2)
plt.plot(x_vals, y_approx, label=f"Taylor Approx", linestyle="--")
plt.title(f"Taylor Series Approximation of e^(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
result = taylor_poly.subs(x_sym, x_val)
print(f"Approximated value at x={x_val}: {result.evalf()}")
act_value=f_sym.subs(x_sym, x_val).evalf()
print(f"Actual value at x={x_val}:", act_value)
Tru_error= act_value-result
print("Tru_error : ", Tru_error)
