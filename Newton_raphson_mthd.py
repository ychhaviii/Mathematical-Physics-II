#Exercise
#To find the nth root of a number A using Newton-Rapshon Method.

import numpy as np
import matplotlib.pyplot as plt
n=int(input("enter n for n^th root : "))
A=float(input("enter your no. A : "))
def nth_root(A, n, tol=0.001, max_iter=100):
    if A < 0 :
        return "Error: Complex root "
    if A == 0:
        return 0
    
    x_old = A 
    
    for i in range(max_iter):
        x_new = (1/n) * ((n-1)*x_old + (A / pow(x_old, n - 1)))
       
        # Check if the result is precise enough
        if abs(x_new - x_old) < tol:
            return x_new
        
        x_old = x_new
        
    return x_old

result = nth_root(A, n)

if isinstance(result, str):
    print(result)
else:
    print(f"The {n}th root of {A} is approximately: {result:.3f}")
    
x_vals = np.linspace(0, result * 1.5, 400)
y_vals = x_vals**n - A

plt.plot(x_vals, y_vals, label=f'f(x) = x^{{{n}}} - {A}', color='blue')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('-----(root)------')
plt.ylabel(f"f(x) = x^{{{n}}} - {A}")

plt.annotate(f'root({result:.3f})',xy=(result,0),xytext=(result-2.5,10000),arrowprops=dict(facecolor='black', shrink=0.07, width=0.8, headwidth=7),fontsize=10)

plt.grid(True, color='green')
plt.legend()
plt.plot(result, 0, marker='o', mec='red', mfc='orange', label=f'Root ≈ {result:.3f}')

