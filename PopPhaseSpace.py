#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:35:18 2019

Pop Phase-Space

@author: Lauren King
"""

import numpy as np
psum1=0
psum2=0
psum3=0
psum4=0


h=0.01
a=[1.0,0.72,1.53,1.27]
b=[[1.0,1.09,1.52,0.0],
   [0.0,1.0,0.44,1.36],
   [2.33,0.0,1.0,0.47],
   [1.21,0.51,0.35,1.0]]

p_i=[0.3013,
   0.4586,
   0.1307,
   0.3557]

t=np.arange(0,1000.001,.01)

pop=[np.arange(0,1000.001,.01),np.arange(0,1000.001,.01),np.arange(0,1000.001,.01),np.arange(0,1000.001,.01)]

pop[0][0]=p_i[0]
pop[1][0]=p_i[1]
pop[2][0]=p_i[2]
pop[3][0]=p_i[3]

dp1=0
dp2=0
dp3=0
dp4=0

w=1
while w<len(t):
    q=0
    while q<4:
        psum1=psum1+((b[0][q])*pop[q][w-1])
        q=q+1
    dp1=a[0]*pop[0][w-1]*(1-psum1)*h
    pop[0][w]=dp1+pop[0][w-1]
    q=0
    while q<4:
        psum2=psum2+((b[1][q])*pop[q][w-1])
        q=q+1
    dp2=a[1]*pop[1][w-1]*(1-psum2)*h
    pop[1][w]=dp2+pop[1][w-1]
    q=0
    while q<4:
        psum3=psum3+((b[2][q])*pop[q][w-1])
        q=q+1
    dp3=a[2]*pop[2][w-1]*(1-psum3)*h
    pop[2][w]=dp3+pop[2][w-1]
    q=0
    while q<4:
        psum4=psum4+((b[3][q])*pop[q][w-1])
        q=q+1
    dp4=a[3]*pop[3][w-1]*(1-psum4)*h
    pop[3][w]=dp4+pop[3][w-1]
    
    dp1=0
    psum1=0
    dp2=0
    psum2=0
    dp3=0
    psum3=0
    dp4=0
    psum4=0
    w=w+1
    
    
#plt.plot(t,pop[0])
#plt.plot(t,pop[1])
#plt.plot(t,pop[2])
#plt.plot(t,pop[3])

#plt.show()

plt.plot(pop[0],pop[1])
plt.title("Species 1 vs Species 2")
plt.xlabel("Species 1")   
plt.ylabel("Species 2") 
plt.show()

plt.plot(pop[1],pop[2])
plt.title("Species 2 vs Species 3")
plt.xlabel("Species 2")   
plt.ylabel("Species 3") 
plt.show()

plt.plot(pop[2],pop[3])
plt.title("Species 3 vs Species 4")
plt.xlabel("Species 3")   
plt.ylabel("Species 4") 
plt.show()

plt.plot(pop[3],pop[0])
plt.title("Species 4 vs Species 1")
plt.xlabel("Species 4")   
plt.ylabel("Species 1") 
plt.show()

plt.plot(pop[3],pop[1])
plt.title("Species 4 vs Species 2")
plt.xlabel("Species 4")   
plt.ylabel("Species 2") 
plt.show()

plt.plot(pop[2],pop[0])
plt.title("Species 3 vs Species 1")
plt.xlabel("Species 3")   
plt.ylabel("Species 1") 
plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(pop[0],pop[1],pop[2])
plt.title("Species 1 vs Species 2 vs Species 3")
ax.set_xlabel('Species 1')
ax.set_ylabel('Species 2')
ax.set_zlabel('Species 3')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(pop[0],pop[1],pop[3])
plt.title("Species 1 vs Species 2 vs Species 4")
ax.set_xlabel('Species 1')
ax.set_ylabel('Species 2')
ax.set_zlabel('Species 4')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(pop[0],pop[2],pop[3])
plt.title("Species 1 vs Species 3 vs Species 4")
ax.set_xlabel('Species 1')
ax.set_ylabel('Species 3')
ax.set_zlabel('Species 4')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(pop[1],pop[2],pop[3])
plt.title("Species 2 vs Species 3 vs Species 4")
ax.set_xlabel('Species 2')
ax.set_ylabel('Species 3')
ax.set_zlabel('Species 4')
plt.show()
