#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:22:07 2019

Physical Pendulum

@author: Lauren King
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def f(m,ang):
    f=-m*g*np.sin(ang)
    return f

m=2
l=1
v0=0
ang0=(np.pi)/3

vlist=[v0]
anglist=[ang0]


x0=np.sin(ang0)*l
y0=np.cos(ang0)*l

ylist=[y0]
xlist=[x0]


g=9.8

h=.01
t=0.0

tlist=[t]

i=0
while i<1000:
    t=t+h
    v0= v0+ (h/m)*f(m,ang0)
    ang0= ang0+v0*h
    vlist.append(v0)
    anglist.append(ang0)
    tlist.append(t)
    i=i+1
    

q=0
while q<1000:
    a=np.sin(anglist[q])*l
    b=np.cos(anglist[q])*l
    xlist.append(a)
    ylist.append(b)
    q=q+1
    
xvel=[0]
yvel=[0]  

k=1
while k<=1000:
    xvel.append(np.cos(anglist[k])*vlist[k])
    yvel.append(np.sin(anglist[k])*vlist[k])
    k=k+1
    
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(xvel,yvel)
ax=fig.add_subplot(111)
ax.set_xlabel('X Direction Velocity')
ax.set_ylabel('Y Direction Velocity')   
plt.show()
    
period= 2*np.pi*np.sqrt(l/g)    
  

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(tlist,anglist)
ax=fig.add_subplot(111)
ax.set_xlabel('Angle')
ax.set_ylabel('Time')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(tlist,xlist)
ax=fig.add_subplot(111)
ax.set_xlabel('Time')
ax.set_ylabel('X Position')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(tlist,ylist)
ax=fig.add_subplot(111)
ax.set_xlabel('Time')
ax.set_ylabel('Y Position')

plt.show()
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(xlist,ylist)
ax=fig.add_subplot(111)
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
plt.show()

stop=0
i=1
while stop==0:
    if anglist[i]>= anglist[0]:
        stop=1
        print("Calculated time period: "+ str(tlist[i]))
    else:
        stop=0
        i=i+1

print("Theoretical time period: "+str(period))

anglist2=[0]



w=0
while w<1000:
    anglist2.append((anglist[w]-anglist[w+1])/h)
    w=w+1


plt.plot(anglist,anglist2)



"""
Attempt at air resistance

def fair(r,vel):
    fair=.5*1.2*np.pi*(r**2)*.5*(vel**2)
    return fair
i=0


v0=0
ang0=np.pi/2
x0=np.sin(ang0)*l
y0=np.cos(ang0)*l
yairlist=[y0]
xairlist=[x0]
vairlist=[0]
tairlist=[0.0]
angairlist=[ang0]
v0=0
ang0=np.pi/2


while i<1000:
    t=t+h
    fsum=f(m,ang)-fair(.01,v0)
    v0= v0+ (h/m)*fsum
    ang0= ang0+v0*h
    vairlist.append(v0)
    angairlist.append(ang0)
    tairlist.append(t)
    i=i+1
    
q=0
while q<1000:
    a=np.sin(angairlist[q])*l
    b=np.cos(angairlist[q])*l
    xairlist.append(a)
    yairlist.append(b)
    q=q+1    
        
plt.plot(tairlist,angairlist)
plt.show()

plt.plot(tairlist,xairlist)
#plt.show()

plt.plot(tairlist,yairlist)     

"""