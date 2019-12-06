#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:01:30 2019

Exam 3 van der Pol's Equation Problem

@author: Lauren King
"""

t=np.arange(0,100.001,.01)

e=np.arange(0,100.001,.01)
de=np.arange(0,100.001,.01)
d2e=np.arange(0,100.001,.01)

h=0.01

i=1

e[0]=3
de[0]=2
d2e[0]=4

g=1
s=2
w=3
tau=4


estep=0
destep=0
d2estep=0

esum=0
desum=0
d2esum=0

while i<len(t):
    d2e=-(w**2)*e[i-1]-(1/tau)*de[i-1]+(g-s*(e[i-1]**2))*de[i-1]
    destep=d2e*h
    de[i]=de[i-1]+destep
    e[i]=de[i]*h+e[i-1]
    i=i+1
    
plt.plot(t,e)
plt.show()

plt.plot(e,de)
plt.show()    