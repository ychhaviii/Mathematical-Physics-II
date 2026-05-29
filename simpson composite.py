# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 03:00:40 2026

@author: Chhavi
"""

import numpy as np 
import sympy as sp
X=sp.Symbol('X')
F_x=sp.exp(X) 
def f(x) :  
    return np.exp(x) 
a = float(input("Enter lower limit : ")) 
b = float(input("Enter upper limit : ")) 
n = int(input("Enter no. of intervals : ")) 
h = (b-a)/n 
F = (f(a)+f(b)) 
for i in range(1,n) : 
    x = a + i*h 
    y = f(x) 
    if i % 2 != 0 : 
        A = 4*y  
        F += A 
    if i % 2 == 0 : 
        B = 2*y 
        F += B 
I = (h/3)*F 
actual_val = sp.integrate(F_x,(X,a,b))
per_error = abs((actual_val - I )/actual_val)*100
print(f"Integration of e^x in interval [{a},{b}] is {I:.4f}") 
print(f"Actual value of integration is {actual_val:.4f}") 
print(f"percentage error = {per_error:.4f} %") 