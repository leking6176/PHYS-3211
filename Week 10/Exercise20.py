#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:35:00 2019

Exercise 20

@author: Lauren King
"""


import numpy as np
import scipy as sc

a=0
b=10
n=100
k=1

y1=zeros((2),float)
y=zeros((2),float)
fReturn=zeros((2),float)
k1=zeros((2),float)
y2=zeros((2),float)

y[0]=0
y[1]=.001
t=a
h=(b-a)/n

def f(x,p):
    f=-k*(x**(p-1))
    return f

#graph1= gdisplay(x=0,y=0,width=400,height=400)
#funct1=gcurve(color=color.yellow)
#graph2=gdisplay(x=400,y=0,width=400,height=400)
#funct2=gcurve(color=color.red)

def rk2(x,h,n):
    k1= [0]*(n)
    k2= [0]*(n)
    fR= [0]*(n)
    y1= [0]*(n)
    fR=f(x,y)
    for i in range(0,n):
        k1[i]=h*fR[i]
    for i in range(0,n):
        y1[i]=y[i]+k1[i]/2
    k2=h*f(x+h/2,y1)    
    for i in range(0,2):
        y[i]=y[i]+(k1[i]+2*k2[i])/3
    return y

while (t<b):
    if((t+h)>b):
        h=b-t
    y=rk2(t,h,2)
    t=t+h
    rate(30)
    funct1.plot(pos=(t,y[0]))
    funct2.plot(pos=(t,y[1]))
    
        
        
        
        