'''
Created on Nov 12, 2015

@author: root
'''

import numpy as np

class Strassen:
    '''
    classdocs
    '''
    
    def split(self, A):
        #check if square
        m, n = np.shape(A)
        if (m != n) or ((n % 2) != 0.0):
            raise IOError("matrix is invalid") 
            
        #n = n - 1
        start = 0
        middle = n / 2
        end = n
            
        a = A[start : middle, start : middle]
        b = A[start : middle, middle : end]
        c = A[middle : end, start : middle] 
        d = A[middle : end, middle : end]
        
        return a, b, c, d
    
    def multiply(self, A, B):
        #check input dimensions
        if np.shape(A) != np.shape(B):
            raise IOError("matrices have inconsistent size")
        
        return self.multiply_recursive(A, B)
    
    def multiply_recursive(self, A, B):

        if np.shape(A) != np.shape(B):
            raise IOError("matrices have inconsistent size")
        
        m, n = np.shape(A)        
        if m == 1 and n == 1:
            return A * B
        
        a, b, c, d = self.split(A)
        e, f, g, h = self.split(B)
        
        '''
        a, b   e, f
        c, d   g, h
        '''
        
        p1 = self.multiply_recursive(a, (f-h))
        p2 = self.multiply_recursive((a+b), h)
        p3 = self.multiply_recursive((c+d), e)
        p4 = self.multiply_recursive(d, (g-e))
        p5 = self.multiply_recursive((a+d), (e+h))
        p6 = self.multiply_recursive((b-d), (g+h))
        p7 = self.multiply_recursive((a-c), (e+f))
        
        k = p5 + p4 - p2 + p6
        l = p1 + p2
        m = p3 + p4
        o = p1 + p5 - p3 - p7
        
        kc = np.hstack((k,l))
        mo = np.hstack((m,o))
        return np.vstack((kc,mo))
        
        
        
        