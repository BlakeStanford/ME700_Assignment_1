import numpy as np
import math

from BisectionMethod import BisectionMethod as bm

def ex1(x):
    ''''zeros at -2, 2'''
    return (x**2)-4


bm1 = bm(-3, 1, 0.000001, ex1)  #setup to find x=-2
print("Example 1: \n x = ", bm1.solve())

def ex2(x):
    '''zeros at -1.72706, 0'''
    return (3*x**3 - 2*x + 12)

bm2 = bm(-3, 1, 0.001, ex2)
print("Example 2: \n x = ", bm2.solve())

def ex3(x):
    '''zero at -8'''
    return (x+8)

bm3 = bm(-15, 3, 0.0001, ex3)
print("Example 3: \n x = ", bm3.solve())

def ex4(x):
    '''mechanics example from class, x=0.697'''
    return 2*(math.sqrt(1**2+x**2)-1)*x/(math.sqrt(1**2+x**2)) - 0.25 

bm4 = bm(0, 2, 0.0001, ex4)
print("Example 4: \n x = ", bm4.solve())

def ex5(x):
    '''Part of a statics problem from ME301 dealing with tension in cable. x= 100.1 '''
    return 300-2*0.8751*116.6-x

bm5 = bm(-150,150,0.001,ex5)
print("Example 5: \n x = ", bm5.solve())
