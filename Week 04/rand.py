#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:10:47 2019

@author: Lauren King
"""
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
#
def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        print("Seed value set to NONE, defaulting to system time.")
        seed=float((datetime.datetime.now().strftime("%s")))

        #%Y%m%d%H%M%s
    else:
        pass

    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    randarr1=rand[0:N]
    randarr2=rand[0:N]
    randarr3=rand[0:N]
    randarr4=rand[0:N]
    randarr5=rand[0:N]
    array=np.arange(N)
    plt.plot(array,randarr1)
    plt.plot(array,randarr2)
    plt.plot(array,randarr3)
    plt.plot(array,randarr4)
    plt.plot(array,randarr5)
    return plt.show()

