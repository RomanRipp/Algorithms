'''
Created on Nov 7, 2015

@author: root
'''

'''
1,2,3,4,5,6,7
0,1,2,3,5,8,13...

'''    
 
class Fibonacci:

    cache = []

    def Get(self, n):
        if n < 1: return 0
        if n < 2: return 1
        return self.Get(n-1) + self.Get(n-2)

    def MGet(self, n):
        if n < len(self.cache):
            return self.cache[n]
        if n < 1: return 0
        if n < 2: return 1
        last = self.MGet(n-2) + self.MGet(n-1)
        self.cache.append(last)
        return last


