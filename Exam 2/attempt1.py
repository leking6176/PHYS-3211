#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:54:03 2019

Exam 2 Physical Pendulum

@author: Lauren King
"""









"""
import numpy as np
import scipy as sc

#t=np.arange(0,10.001,.01)

#y=np.arange(0,10.001,.01)
#y[0]=.001

g=9.8


def f(m,ang):
    f=m*g*np.sin(ang)
    return f


m=2
ang=(np.pi)/2
h=.01


arrang=np.arange(-ang,ang,.01)
arrang=arrang*-1
i=0

t=np.arange(0,len(arrang),.01)
y=np.arange(0,len(arrang),.01)
x=np.arange(0,len(arrang),.01)


while i<(len(arrang)-1):
    y[i]=y[i-1]+f(m,arrang[i])*h
    x[i]=x[i-1]+y[i]*h
    
    i=i+1
    
plt.plot(t,x)
plt.plot(t,y)

"""