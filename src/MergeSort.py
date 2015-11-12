'''
Created on Nov 8, 2015

@author: root
'''

class MergeSort:
    '''
    classdocs
    '''

    def MergeAndCountInversions(self, a, b):
        merged = []
        ai = 0
        bi = 0
        invCount = 0
        for i in range(len(a) + len(b)):
            if (bi >= len(b)) or ((ai < len(a)) and (a[ai] <= b[bi])):
                merged.append(a[ai])
                ai = ai + 1     
            else:
                merged.append(b[bi])
                bi = bi + 1
                invCount = invCount + (len(a) - ai)
                                
        return merged,invCount

    def SortAndCountInversions(self, array):
        if len(array) <= 1:
            return array, 0
        a,b = self.Split(array)
        a,invCountA = self.SortAndCountInversions(a)
        b,invCountB = self.SortAndCountInversions(b)
        c,invCount = self.MergeAndCountInversions(a, b);
        invCount = invCountA + invCountB + invCount
        return c, invCount   

    def Split(self, array):
        half = len(array) / 2
        return array[:half], array[half:]
    
    def Merge(self, a, b):
        merged = []
        ai = 0
        bi = 0
        for i in range(len(a) + len(b)):
            if (bi >= len(b)) or ((ai < len(a)) and (a[ai] <= b[bi])):
                merged.append(a[ai])
                ai = ai + 1    
            else:
                merged.append(b[bi])
                bi = bi + 1
                                
        return merged

    def Sort(self, array):
        if len(array) <= 1:
            return array
        a,b = self.Split(array)
        a = self.Sort(a)
        b = self.Sort(b)
        return self.Merge(a, b);             
    