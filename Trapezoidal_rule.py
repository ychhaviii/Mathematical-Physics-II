import numpy as np 
import sympy as sp
X=sp.Symbol('X')
F=1/(1+X**2)
def f(x) : 
    return 1/(1+x**2)
a = float(input("Enter lower limit : ")) 
b = float(input("Enter upper limit : ")) 
n = int(input("Enter no. of intervals : ")) 
h = (b-a)/n 
A = (f(a)+f(b))/2 
for i in range(1,n) : 
    x = a + i*h 
    y = f(x) 
    A += y 
result = h*A 
actual_val = sp.integrate(F,(X,a,b))
per_error = abs((actual_val - result )/actual_val)*100
print(f"Integration of 1/1+x^2 in interval [{a},{b}] is {result:.4f}") 
print(f"Actual value of integration is {actual_val:.4f}") 
print(f"percentage error = {per_error:.4f} %") 
