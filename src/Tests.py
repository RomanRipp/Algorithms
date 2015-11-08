'''
Created on Nov 7, 2015

@author: root
'''
import unittest
import time
import Fibonacci
import MergeSort

class Test(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def testBruteForceFibonacci(self):
        fib = Fibonacci.Fibonacci()                    
        for n in range(1, 10):
            fib.Get(n)
                
    def testMemoizedFibonacci(self):
        fib = Fibonacci.Fibonacci()    
        for n in range(1, 10):
            fib.MGet(n)
            
    def testMergeSort(self):
        array = [3,4,5,6,7,-3,1,4,5,6,8,9,0,-1]
        sortAlgorithm = MergeSort.MergeSort()
        sortedArray = sortAlgorithm.Sort(array)
        print sortedArray
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")

    def testMergeSortEmpty(self):
        array = []
        sortAlgorithm = MergeSort.MergeSort()
        sortedArray = sortAlgorithm.Sort(array)
        print sortedArray
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")

    def testInversionsCount(self):
        array = [1,3,5,2,4,6]
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        self.assertEqual(count, 3, "Number of inversions incorrect")
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")


    def testInversionsCount2(self):
        array = [6,5,4,3,2,1]
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        self.assertEqual(count, 15, "Number of inversions incorrect")
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)