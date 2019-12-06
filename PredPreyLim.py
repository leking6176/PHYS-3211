#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:51:40 2019

Predator Prey Euler

@author: Lauren King
"""

a=0.2
b=0.1
e=1.0
m=0.1
k=20

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
    preystep=a*prey[i-1]*(1-prey[i-1]/k)-b*prey[i-1]*predator[i-1]
    predstep=e*b*prey[i-1]*predator[i-1]-m*predator[i-1]
    prey[i]=preystep*h+prey[i-1]
    predator[i]=predstep*h+predator[i-1]
    i=i+1
  

plt.plot(t,predator)
plt.plot(t,prey)
ax.plot(t, predator, label='Predator')
ax.plot(t, prey, label='Prey')
plt.title("Predator-Prey Relation")
plt.xlabel("Time")   
plt.ylabel("Population") 
ax.legend()
plt.show()
    
plt.show()
plt.plot(predator,prey)
plt.title("Phase Space Plot")
plt.xlabel("Predator Population")   
plt.ylabel("Prey Population")