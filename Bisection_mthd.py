#Exercise 
#To determine the depth upto which a spherical homogeneous object of given radius and density will sink into a fluid of given density. Using Bisection Method.

import matplotlib.pyplot as plt
import numpy as np
r=float(input("enter radius of sphere (m) : "))
d_obj=float(input("enter density of object in (kg/m^3) : "))
d_fluid=float(input("enter density of object in (kg/m^3) : "))
def f(D):
    return (d_fluid*D**3 - 3*r*d_fluid*D**2 + 4*d_obj*r**3)
def calculate_sink_depth(r, d_obj, d_fluid, tol=0.001, maxiter=100):
    if d_obj > d_fluid:
        print("The object completely sinks in the fluid")
        return 2*r
    a=0 #LOWER LIMIT
    b=2*r #UPPER LIMIT    
    if f(a)*f(b)>0 :
        print("Bisection method fails: No root found in range [0, 2r].")
        return None
    iteration=0
    while (b-a)/2 > tol:
        midpoint = (a+b)/2
        if f(midpoint)==0:
            print("The exact root found")
            return midpoint
        elif f(a)*f(midpoint)<0:
            b= midpoint
        else:
            a= midpoint
        iteration += 1
        if iteration > maxiter:
            break
    return (a+b)/2
depth = calculate_sink_depth(r, d_obj, d_fluid, tol=0.001, maxiter=100)
if depth is not None:
    print(f"Parameters: Radius={r}m, Obj Density={d_obj}kg/m^3, Fluid Density={d_fluid}kg/m^3")
    print(f"The sphere sinks to a depth of: {depth:.4f} meters.")
    x_vals = np.linspace(0, 2*r, 100) 
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='black', linestyle='--', label='when f(D)=0')
plt.xlabel('-----depth(D)------')
plt.ylabel("------f(D)-------")

if depth is not None:
    plt.plot(depth, 0,'o', mec='red', mfc='red', label='sinked depth')
plt.title(f"Archemedes principle for a sphere of radius ({r}m)")
plt.annotate(f"sinked depth{depth:.4f}",xy=(depth,0),xytext=(depth+0.3, 1000),arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), fontsize=7)
plt.legend()
plt.grid(True, color='green')
plt.show()
