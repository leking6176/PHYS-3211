#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:22:07 2019

Physical Pendulum 2

@author: Lauren King
"""

import numpy as np
import scipy as sc

def f(m,ang):
    f=-m*g*np.sin(ang)
    return f

m=2
l=1
v0=0
ang0=(np.pi)/5

vlist=[v0]
anglist=[ang0]


x0=np.sin(ang0)*l
y0=np.cos(ang0)*l

ylist=[y0]
xlist=[x0]


g=9.8

dt=.01
t=0.0

tlist=[t]

i=0
while i<1000:
    t=t+dt
    v0= v0+ (dt/m)*f(m,ang0)
    ang0= ang0+v0*dt
    vlist.append(v0)
    anglist.append(ang0)
    tlist.append(t)
    i=i+1
    

q=0
while q<1000:
    a=np.sin(anglist[q])*l
    b=np.cos(anglist[q])*l
    xlist.append(a)
    ylist.append(b)
    q=q+1
    
period= 2*np.pi*np.sqrt(l/g)    
  

plt.plot(tlist,anglist)
plt.show()

plt.plot(tlist,xlist)
#plt.show()

plt.plot(tlist,ylist) 

plt.show()
plt.plot(xlist,ylist)

stop=0
i=1
while stop==0:
    if anglist[i]>= anglist[0]:
        stop=1
        print("Calculated time period: "+ str(tlist[i]))
    else:
        stop=0
        i=i+1

print("Theoretical time period: "+str(period))