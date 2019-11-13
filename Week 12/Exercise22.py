#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:05:16 2019

Exercise 22

@author: Lauren King
"""
import numpy as np
import scipy as sc

hbar=6.5821*10**-16

xpos=np.arange(-100,100,.001)

vals=np.arange(-100,100,.001)

dvals=np.arange(-100,100,.001)




def kappa(m,energy):
    kappa=np.sqrt(((2*m)/(hbar**2))*energy)
    return kappa

def psir(m,energy,x):
    k=kappa(m,energy)
    psir=np.exp(-1*k*x)
    return psir

def psil(m,energy,x):
    k=kappa(m,energy)
    psil=np.exp(1*k*x)
    return psil

def psii(m,energy,x):
    k=kappa(m,energy)
    psii=(k**2)*np.exp(-1*k*x)+((2*m)/hbar**2)*83*np.exp(-1*k*x)
    return psii

def psib(m,energy,x,sy):
    k=kappa(m,energy)
    psib=(k**2)*sy+((2*m)/hbar**2)*83*sy

def psicr(m,energy,x,v0):
    k=kappa(m,energy)
    psicr=v0*(1/(k**4))*np.exp(-1*(k**2)*x)+(k**2)*(x**2)
    return psicr

def psicl(m,energy,x,v0):
    k=kappa(m,energy)
    psicl=v0*(1/(k**4))*np.exp(1*(k**2)*x)+(k**2)*(x**2)
    return psicl

def dpsi(m,energy,x):
    k=kappa(m,energy)
    dpsi=-(sign(x))*k*np.exp(-k*abs(x))
    return dpsi

def npsi(m,energy,x):
    k=kappa(m,energy)
    npsi=np.exp(-k*abs(x))
    return npsi

a=3
energy=5
m=1

i=0
xtemp=0
ins=0
"""
while i<len(xpos)-1:
    if xpos[i]<-a:
        vals[i]=psil(m,energy,xpos[i])
        i=i+1
    elif xpos[i]>a:
        vals[i]=psir(m,energy,xpos[i])
        i=i+1
    elif xpos[i]<=a and xpos[i]>0:
        xtemp=psil(m,energy,xpos[i-1])
        ins=psicr(m,energy,xpos[i],83)
        vals[i]=ins
        i=i+1
    elif xpos[i]<=0 and xpos[i]>=-1:
        xtemp=psil(m,energy,xpos[i-1])
        ins=psicl(m,energy,xpos[i],83)
        vals[i]=ins
        i=i+1    
"""    
vals[0]=npsi(m,energy,-100)
k=kappa(m,energy)
dvals[0]=sign(-100)*k*npsi(m,energy,-100)


q=(2*m)/(hbar**2)
v=0
i=1
dx=.001
while i <= len(xpos)-1:
    if abs(xpos[i]) > a:
        v=0
    else:
        v=83
        
    k=kappa(m,energy)
    dvals[i]=dvals[i-1]+(q*v+k**2)*npsi(m,energy,xpos[i-1])*dx
    #dvals[i]=dvals[i-1]+(q*v+k**2)*vals[i-1]*dx
    vals[i]=npsi(m,energy,xpos[i-1])+dvals[i-1]*dx
    #vals[i]=vals[i-1]+dvals[i-1]*dx
    i=i+1
            
plt.plot(xpos,vals)
#plt.plot(xpos,dvals)       
        