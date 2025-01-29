import numpy as np

class BisectionMethod:
    '''
    Recursive implementation of the Bisection Method. 
    Takes as inputs:
    low, high: low and high value of ranges to search for 0 within
    tol: desired tolerance in accuracy of answer
    func: desired function for which to find a 0
    '''
    def __init__(self, low:float, high:float, tol:float, func):
        self.low = low
        self.high = high
        self.tol = tol
        self.func = func
        self.mid = None
    
    

    def find_midpoint(self):
        '''Update self.mid to the midpoint of self.high and self.low'''
        self.mid = (self.low+self.high)/2

    def solve(self):
        '''Recursively returns a 0 of a function'''
        self.find_midpoint()
        f_mid = self.func(self.mid)
        f_low = self.func(self.low)
    
        #base case
        if abs(self.mid-self.low) < self.tol or abs(f_mid) < self.tol:
            return self.mid
        #recursive case
        else:
            if (f_mid >= 0 and f_low >= 0) or (f_mid < 0 and f_low < 0):
                #0 in upper half of range
                self.low = self.mid
                return self.solve()
            else: #0 in lower half of range
                self.high = self.mid
                return self.solve()


