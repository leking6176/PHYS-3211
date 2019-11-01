#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:35:00 2019

Exercise 20

@author: Lauren King
"""
#from visual.graph import gdisplay
#from visual.graph import gcurve
#import visual.graph as g

import numpy as np
import scipy as sc




t=np.arange(0,10.001,.01)

y1=zeros((2),float)
y=zeros((2),float)
fReturn=zeros((2),float)
k1=zeros((2),float)
y2=zeros((2),float)

xpos=np.arange(0,10.001,.01)


vel=np.arange(0,10.001,.01)

vtemp=0
xtemp=0


print(y)
y[0]=0
y[1]=.001
h=.01

def f(k,x,p):
    fReturn=-k*(x**(p-1))
    return fReturn

#graph1= gdisplay(x=0,y=0,width=400,height=400)
#funct1=gcurve(color=color.yellow)
#graph2=gdisplay(x=400,y=0,width=400,height=400)
#funct2=gcurve(color=color.red)

def rk2(m,x,v,k,p,h):
    vel[0]=v
    xpos[0]=x
    vtemp=v
    xtemp=x
    #k1= [0]*(n)
    #k2= [0]*(n)
    #fR= [0]*(n)
    #y1= [0]*(n)
    #fR=f(x,p)
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
        
    #for i in range(0,n):
    #    y1[i]=y[i]+k1[i]/2.
   # k2=h*f(x+h/2.,2)    
   # for i in range(0,2):
   #     y[i]=y[i]+(k1[i]+2*k2[i])
  #  return y


xarr=np.arange(0,10.0001,.01)
xarr[0]=.001

yarr=np.arange(0,10.0001,.01)
yarr[0]=.001

i=1

h=.01
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
    
    return y,x
#while (x<b):
#    if((t+h)>b):
#        h=b-t
#    y=rk2(.001,.01,2)
#    x=x+h
    #rate(30)
    #funct1.plot(pos=(x,y[0]))
    #funct2.plot(pos=(x,y[1]))
#plt.plot(x,y[0])    
#plt.plot(x,y[1])    

m=2
v0=0
x0=2
k=10
h=.01

a=rk2(m,x0,v0,k,2,h)
b=euler(m,x0,v0,k,2,h)
#print(a)
print(b)
plt.plot(t,a[0])
plt.plot(t,a[1])

plt.show()

plt.plot(t,b[0])
plt.plot(t,b[1])


#plt.plot(t,xpos)

    
        
        
        
        