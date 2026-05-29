#Exercise
#To find roots of a transcendental equation using Secant Method upto 3 decimal places

import numpy as np
import matplotlib.pyplot as plt
a=float(input("Enter Initial guess (I) : "))
b=float(input("Enter Initial guess (II) : "))
def f(x) :
    return np.tan(x)-x-1
def secant_method(a,b,tol=0.001,max_iter=100):
    iteration=0
    while iteration < max_iter:
        fa=f(a)
        fb=f(b)
        if f(b)-f(a)==0 :
            print ("error, denominator can't be zero")
            break
        c=b-(fb*(b-a)/(fb-fa))
        if abs(c-b)<tol:
            return c
        a=b
        b=c
        iteration +=1
    return b
root= secant_method(a,b,tol=0.001, max_iter=100)
print(f"the approx. root is : {root:.3f}")

x_vals = np.linspace(a, b, 100)  
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='black')   
plt.xlabel('-----x-----')
plt.ylabel('-----f (x)-----')

if root is not None:
    plt.plot(root, 0, 'o', label='Root', mec='red', mfc='red')
    
plt.title("Root of the Transcendental equation" )
plt.annotate(f'root({root:.3f})',xy=(root,0),xytext=(root+0.05,35),arrowprops=dict(facecolor='black', shrink=0.07, width=0.8, headwidth=7),fontsize=10)
plt.legend()
plt.grid(True)
plt.show()
