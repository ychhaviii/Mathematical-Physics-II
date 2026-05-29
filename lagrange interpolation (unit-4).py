# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 06:29:08 2026

@author: Chhavi
"""
#2025/13/108
import numpy as np
import matplotlib.pyplot as plt
x_temp=np.array([110,130,160,190])
y_viscosity=np.array([10.8,8.1,5.5,4.8])
def f(x_val, y_val, x_0):
    N=len(x_val)
    result=0
    for i in range(N):
        product=1
        for j in range(N):
            if i != j:
                product *=(x_0-x_val[j])/(x_val[i]-x_val[j])
        result +=y_viscosity[i]*product
    return result
x_0=float(input("Enter the value of temperature(x) for which we have to find viscosity(y) (in degree celsius) : "))
Y=f(x_temp,y_viscosity,x_0)
print(f"Value of viscosity at temperatue={x_0} degree is : ", f"{Y:.4f}", "poise")
plt.figure(figsize=(8,5))
X_pts=np.linspace(100,200,1000)
y_pts=[]
for k in X_pts:
    y_pts.append(f(x_temp,y_viscosity,k))
Y_pts=np.array(y_pts)
plt.scatter(x_temp,y_viscosity,label='known data points', marker='o', s= 15)
plt.scatter(x_0,Y,s=200,label=(f'required value of viscosity at temperatue(x)={x_0}'), marker="*")
plt.plot(X_pts, Y_pts,label='INTERPOLATED RESULT')
plt.title("LAGRANGE INTERPOLATION \n Name : Chhavi Yadav\n Roll no : 2025/13/108")
plt.xlabel('----x----')
plt.ylabel('----f(x)----')
plt.legend()
plt.grid()
plt.show()