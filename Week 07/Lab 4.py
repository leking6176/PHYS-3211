#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:38:21 2019

Lab 4

@author: Lauren King
"""
import numpy as np
import scipy as sc

def j(a1,a2,a3,t1,t2,t3):
    j=[[0,0,0,3,4,4,0,0,0],
       [3,4,-5,0,0,0,0,0,0],
       [t1,-t2,0,0,0,0,np.sin(a1),-np.sin(a2),0],
       [0,0,0,t1,-t2,0,np.cos(a1),-np.cos(a2),0],
       [0,t2,t3,0,0,0,0,np.sin(a2),np.sin(a3)],
       [0,0,0,0,t2,-t3,0,np.cos(a2),-np.cos(a3)],
       [2*np.sin(a1),0,0,2*np.cos(a1),0,0,0,0,0],
       [0,2*np.sin(a2),0,0,2*np.cos(a2),0,0,0,0],
       [0,0,2*np.sin(a3),0,0,2*np.cos(a3),0,0,0]]
    return j


       