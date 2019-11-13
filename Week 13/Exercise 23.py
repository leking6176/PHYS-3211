#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:47:27 2019

Exercise 23

@author: Lauren King
"""
m=0.5
vy0=0.0
vx0=0.0
db=0.05
b=np.arange(-1,1,db)

def v(x,y):
    v=(x**2)*(y**2)*np.exp(-((x**2)+(y**2)))
    return v

vx=np.arange(0,10.001,.01)
vx[0]=vx0

vy=np.arange(0,10.001,.01)
vy[0]=vy0

