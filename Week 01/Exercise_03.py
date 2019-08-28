# -*- coding: utf-8 -*-
"""
Exercise 03: Chapter 03, Kinder & Nelson

A common way to determine the value of a function is to sum over a series. 
For example, the Maclaurin series for sin(x) is

    sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid between n = 0 
and n = N, where N ≥ 0. This will serve as your algorithm for summing 
the series.

One problem with the algorithm is that we do not know which value 
of N is suitable when calcualting the series. Instead of guessing, have 
your code proceed with the summation until the Nth term contributes a 
negligible amount to the final summation, say 1 part in 10**8.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(x) to 
      derive the equation in the README. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of x, the series converges.
   6. Which value for N was required to reach the desired precision and
      obtain convergence?
   7. Compare your results to the value determined using NumPy's sine 
      function.
   8. Steadily increase x and write down the relative error between your
      calculated value for sin(x) and the NumPy function's value. 
   9. What do you notice about the relative error?
  10. Will there be a time when the series does not converge? Make a plot
      of the relative error vs x to support your answer.

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

i=1
w=1
add=1
c=1
a=1
fact=1
reducenum=0
d=0
g=0
N=27
totalsum=0
x=567
xorig=x



while x > (2*(np.pi)):
    reducenum= x-(2*(np.pi))
    x=reducenum
    

while (i <= N):
    if a != 1:
        while (a > 1):
            fact= fact*a*(a-1)
            a=a-2
#            print("while loop 2 a=" , a)
#           print("while loop 2 fact=" , fact)
    add=float((x**i)/fact)
 #   print("while loop 1 mid add=" , add)
    if d==0:
        totalsum=float(add)
        d=1
    elif d==1:
        totalsum=float(totalsum-add)
        d=2
    elif d==2:
        totalsum=float(totalsum+add)
        d=1
        
#    print("while loop 1 mid d=" , d) 
    
    i=i+2
    a=i 
    fact=1
    
#    print("while loop 1 end totalsum=" , totalsum)
#    print("while loop 1 end add=" , add)
#    print("while loop 1 end i=" , i)
#    print("while loop 1 end a=" , a)
      
#print("The number estimated by the program is " + str(totalsum))   
act=np.sin(xorig)
#print("The real value calculated is " + str(act))   
error= abs(((act-totalsum)/act)*100)
print("The percent error is " + str(error) + "%")

fact=1
b=1

if error > (10**(-15)):
    totalsum=0

while error > (10**(-15)):
    print("through loop")
    N=N+1
    while (w <= N):
        if b != 1:
            while (b > 1):
                fact= fact*b*(b-1)
                b=b-2
#           print("while loop 2 a=" , a)
#           print("while loop 2 fact=" , fact)
        add=float((x**w)/fact)
 #   print("while loop 1 mid add=" , add)
        if g==0:
            totalsum=float(add)
            g=1
        elif g==1:
            totalsum=float(totalsum-add)
            g=2
        elif g==2:
                totalsum=float(totalsum+add)
                g=1
        
#    print("while loop 1 mid d=" , d) 
    
        w=w+2
        b=w 
        fact=1
        error= ((act-totalsum)/act)*100
    
#    print("while loop 1 end totalsum=" , totalsum)
#    print("while loop 1 end add=" , add)
#    print("while loop 1 end i=" , i)
#    print("while loop 1 end a=" , a)
    
    
    
print("The number estimated by the program is " + str(totalsum))   

print("The real value calculated is " + str(act))   

print("The percent error is " + str(error) + "%")    

"""
At around N=11 we can see that desired precision is reached and the percent error
is around 1.9*10^-8 % while x=1

While N=11 the value of x will be increased and the percent error recorded
for x=1, error is 1.8993938788946215e-08% 
for x=2, error is 0.00014196266710436812%
for x=3, error is 0.1739044005149504%
for x=4, error is 1.3216206639516588%
for x=5, error is 18.217603718511477%
This data shows that as x increases so does the percent error. To adjust for this N needs
to increase.
When N= 29 and x=5, the percent error is 2.138905307067674e-09% which is much better than
it was when N was set to 11

The plot show how drastic this error increases when the value of x increases and N remains
the same. It supports how the series does not converge when N is small and x is big.

"""
plt.plot([1,2,3,4,5],[1.8993938788946215e-07,0.014196266710436812,17.39044005149504,132.16206639516588,1821.7603718511477 ])
plt.show()
