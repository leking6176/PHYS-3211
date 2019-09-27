#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:55:52 2019

Exam 1 Hi-Ho Cherry-O

@author: Lauren King
"""
import numpy as np

tree=10
basket=0

spin=rand.random()*7

print("Old Game: Equal Probabilities")

while basket < 10:
    if spin <=1:
        basket +=1
        tree -= 1
        spin=rand.random()*7
        print("1 Cherry")
    elif spin <=2:
        basket +=2
        tree -= 2
        spin=rand.random()*7
        print("2 Cherries")
    elif spin <=3:
        basket +=3
        tree -= 3
        spin=rand.random()*7
        print("3 Cherries")
    elif spin <=4:
        basket +=4
        tree -= 4
        spin=rand.random()*7
        print("4 Cherries")
    elif spin <=5:
        if basket == 0:
            spin=rand.random()*7
        elif basket == 1:
            basket= 0
            tree= 10
            spin=rand.random()*7
        elif basket >= 2:
            basket -=2
            tree+=2
            spin=rand.random()*7
        print("Dog")
    elif spin <=6:
        if basket == 0:
            spin=rand.random()*7
        elif basket == 1:
            basket= 0
            tree= 10
            spin=rand.random()*7
        elif basket >= 2:
            basket -=2
            tree+=2
            spin=rand.random()*7
        print("Bird")
        print(basket)
    elif spin <= 7:
        basket=0
        tree=10
        spin=rand.random()*7
        print("Spilled Basket")
    

tree=10
basket=0

spin=rand.random()*11
print(" ")
print("New Game: Not Equal Probabilities")

while basket < 10:
    if spin <=2:
        basket +=1
        tree -= 1
        spin=rand.random()*11
        print("1 Cherry")
    elif spin <=4:
        basket +=2
        tree -= 2
        spin=rand.random()*11
        print("2 Cherries")
    elif spin <=6:
        basket +=3
        tree -= 3
        spin=rand.random()*11
        print("3 Cherries")
    elif spin <=8:
        basket +=4
        tree -= 4
        spin=rand.random()*11
        print("4 Cherries")
    elif spin <=9:
        if basket == 0:
            spin=rand.random()*11
        elif basket == 1:
            basket= 0
            tree= 10
            spin=rand.random()*11
        elif basket >= 2:
            basket -=2
            tree+=2
            spin=rand.random()*11
        print("Dog")
    elif spin <=10:
        if basket == 0:
            spin=rand.random()*11
        elif basket == 1:
            basket= 0
            tree= 10
            spin=rand.random()*11
        elif basket >= 2:
            basket -=2
            tree+=2
            spin=rand.random()*11
        print("Bird")
        print(basket)
    elif spin <= 11:
        basket=0
        tree=10
        spin=rand.random()*11
        print("Spilled Basket")
        