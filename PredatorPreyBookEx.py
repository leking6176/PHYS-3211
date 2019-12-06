#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:07:14 2019

Predator Prey Book Example

@author: Lauren King
"""


tmin=0
tmax=500
y=zeros((2),float)
ntimes=1000
y[0]=2.0
y[1]=1.3
h=(tmax-tmin)/ntimes
t=tmin

def f(t,y,F):
    F[0]=0.2*y[0]*(1-(y[0]/(20.0)))-0.1*y[0]*y[1]
    F[1]=-0.1*y[1]+0.1*y[0]*y[1];
    

def rk4(t,y,h,neqs):
    F=zeros((neqs),float)
    ydumb=zeros((neqs),float)
    k1=zeros((neqs),float)
    k2=zeros((neqs),float)
    k3=zeros((neqs),float)
    k4=zeros((neqs),float)
    f(t,y,F)
    for i in range(0,neqs):
        k1[i]=h*F[i]
        ydumb[i]=y[i]+k1[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0,neqs):
        k2[i]=h*F[i]
        ydumb[i]=y[i]+k2[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0,neqs):
        k3[i]=h*F[i]
        ydumb[i]=y[i]+k3[i]
    f(t+h,ydumb,F)
    for i in range(0,neqs):
        k4[i]=h*F[i]
        y[i]=y[i]+(k1[i]+2.*(k2[i]+k3[i])+k4[i])/6.
        
graph1= gdisplay(x=0,y=0,width=500,height=400,\
                 title='Prey p(green) and predator P(yellow) vs time', xtitle=
                 't',\
                 ytitle= 'P, p', xmin=0,xmax=500,ymin=0,ymax=3.5)

funct1= gcurve(color=color.yellow)
funct2= gcurve(color=color.green)
graph2= gdisplay(x=0,y=400,width=500,height=400,title='Predator P vs prey p',
                 xtitle='P', ytitle= 'p', xmin=0,xmax=2.5,ymin=0,ymax=3.5)
funct3= gcurve(color=color.red)

for t in arange(tmin,tmax+1,h):
    funct1.plot(pos=(t,y[0]))
    funct2.plot(pos=(t,y[1]))
    funct3.plot(pos=(y[0],y[1]))
    rate(60)
    rk4(t,y,h,2)
    
    
    