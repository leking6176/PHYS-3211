#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:07:38 2019

Lab 05

@author: Lauren King
"""

import numpy as np
import scipy as sc

def f(k,x,p):
    fReturn=-k*(x**(p-1))
    return fReturn

def statf(cs,m,v):
    if v==0:
        statf=-m*cs*9.8
    else:
        statf=0
    return statf

def kinf(ck,m,v1,v2):
    if v==0:
        kinf=0
    elif v1/v2 < 0:
        kinf=0
    else:
        kinf=-m*ck*(v1/np.abs(v1))*9.8
    return kinf

def viscf(b,v):
    viscf=-b*v
    return viscf

def eulerfriction(m,x,v,k,p,h,cs,ck,b):
    xpos=np.arange(0,10.001,.01)
    xpos[0]=x
    vel=np.arange(0,10.001,.01)
    vel[0]=v
    t=np.arange(0,10.001,.01)
    vel[1]=vel[0]+(f(k,xpos[0],p)+statf(ck,m,vel[0])+kinf(ck,m,vel[0],1)+viscf(b,vel[0]))*(h/m)
    xpos[1]=xpos[0]+vel[1]*h
    i=2
    
    while i<len(t-2):
        vel[i]=vel[i-1]+(f(k,xpos[i-1],p)+statf(ck,m,vel[i-1])+kinf(ck,m,vel[i-1],vel[i-2])+viscf(b,vel[i-1]))*(h/m)
        xpos[i]=xpos[i-1]+vel[i]*h
        i=i+1
    
    return vel,xpos

def euler(m,x,v,k,p,h):
    i=1
    xarr=np.arange(0,10.001,.01)
    xarr[0]=x
    yarr=np.arange(0,10.001,.01)
    yarr[0]=v
    
    t=np.arange(0,10.001,.01)
    
    while i<len(t-1):
        yarr[i]=yarr[i-1]+f(k,xarr[i-1],p)*(h/m)
        xarr[i]=xarr[i-1]+yarr[i]*h
        i=i+1
    
    return yarr,xarr

"""
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
"""

m=2
v0=0
x0=2
k=10
h=.01

#a=rk2(m,x0,v0,k,2,h)


#plt.plot(t,a[0])
#plt.plot(t,a[1])

#plt.show

#b=rk2friction(m,x0,v0,k,2,h,.9,.9,.5)

#plt.plot(t,b[0])
#plt.plot(t,b[1])

#plt.show()

c=euler(m,x0,v0,k,2,h)
d=eulerfriction(m,x0,v0,k,2,h,.3,.2,0)



plt.plot(t,c[0])
plt.plot(t,c[1])

plt.plot(t,d[0])
plt.plot(t,d[1])


