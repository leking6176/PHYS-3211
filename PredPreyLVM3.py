#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:25:35 2019

LVM Predation Efficiency

@author: Lauren King
"""


a=0.2
b=0.1
m=0.4
K=500
ka=0.2


"""
a= birth rate
b= population constant
e= eating rate
m= mortality rate
"""


y=np.arange(0,400.001,.01)
t=np.arange(0,400.001,.01)

prey=np.arange(0,400.001,.01)
predator=np.arange(0,400.001,.01)

predstep=0
preystep=0
prey[0]=2.0
predator[0]=1.3



h=.01

i=1


while i < len(t):
    preystep=a*prey[i-1]*(1-prey[i-1]/K)-(b*prey[i-1]*predator[i-1])/(1+b*prey[i-1]*th)
    predstep=m*predator[i-1]*(1-(predator[i-1]/(ka*prey[i-1)))
    prey[i]=preystep*h+prey[i-1]
    predator[i]=predstep*h+predator[i-1]
    i=i+1
  