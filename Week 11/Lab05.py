#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:07:38 2019

Lab 05

@author: Lauren King
"""

import numpy as np
import scipy as sc

def statf(cs,m):
    statf=-m*cs*9.8
    return statf

def kinf(ck,m,v):
    if v==0:
        kinf=0
    else:
        kinf=-m*ck*(v/np.abs(v))*9.8
    return kinf

def viscf(b,v):
    viscf=-b*v
    return viscf

def rk2(m,x,v,k,p,h):
    vel[0]=v
    xpos[0]=x
    vtemp=v
    xtemp=x
    i=1
    while i < ((10/h)-1):
        va= vtemp+h*f(k,xtemp,p)/2
        xa= xtemp+h*vtemp/2
        vtemp= vtemp+h*f(k,xa,p)
        xtemp=xtemp+h*va
        vel[i]=vtemp
        xpos[i]=xtemp
        i=i+1
    return vel,xpos  

def rk2friction(m,x,v,k,p,h,cs,ck,b):
    vel[0]=v
    xpos[0]=x
    vtemp=v
    xtemp=x
    i=1
    while i < ((10/h)-1):
        va= vtemp+h*((f(k,xtemp,p)/2)+statf(cs,m)+kinf(ck,m,vel[i-1])+viscf(b,vel[i-1]))
        xa= xtemp+h*vtemp/2
        vtemp= vtemp+h*f(k,xa,p)
        xtemp=xtemp+h*va
        vel[i]=vtemp
        xpos[i]=xtemp
        i=i+1
    return vel,xpos  


m=2
v0=0
x0=2
k=10
h=.01

a=rk2(m,x0,v0,k,2,h)


plt.plot(t,a[0])
plt.plot(t,a[1])

plt.show

b=rk2friction(m,x0,v0,k,2,h,.9,.9,.5)

plt.plot(t,b[0])
plt.plot(t,b[1])
