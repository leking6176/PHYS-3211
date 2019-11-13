#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:47:27 2019

Exercise 23

@author: Lauren King

"""

import numpy as np

m=0.1
vy0=3
vx0=2
db=0.05
b=np.arange(-1,1,db)

t=np.arange(0,100.001,.01)

def v(x,y):
    v=(x**2)*(y**2)*np.exp(-((x**2)+(y**2)))
    return v

def d2x(x,y,m):
    d2x=-(2/m)*(y**2)*x*(1-(x**2))*np.exp(-((x**2)+(y**2)))
    return d2x

def d2y(x,y,m):
    d2y=-(2/m)*(x**2)*x*(1-(y**2))*np.exp(-((y**2)+(x**2)))
    return d2y

vx=np.arange(0,100.001,.01)
vx[0]=vx0
vy=np.arange(0,100.001,.01)
vy[0]=vy0
xpos=np.arange(0,100.001,.01)
ypos=np.arange(0,100.001,.01)
ang=np.arange(0,100.001,.01)


h=.01

i=1
while i<len(vx-1):
    vy[i]=vy[i-1]+d2y(vx[i-1],vy[i-1],m)*h
    vx[i]=vx[i-1]+d2x(vx[i-1],vy[i-1],m)*h
    xpos[i]=(vx[i]*h)+xpos[i-1]
    ypos[i]=(vy[i]*h)+ypos[i-1]
    ang[i]=math.atan2(vy[i],vx[i])
    i=i+1
    
    
plt.plot(vy,vx)
plt.show()
plt.plot(t,vy)
plt.plot(t,vx)
plt.show()
plt.plot(t,xpos)
plt.plot(t,ypos)