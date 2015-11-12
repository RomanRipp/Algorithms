'''
Created on Nov 7, 2015

@author: root
'''
import unittest
import time
import csv
import numpy as np

import Fibonacci
import MergeSort
import Strassen

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


    '''
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

    def testInversionsCount1(self):
        array = [1,5,3,2,4]
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        self.assertEqual(count, 4, "Number of inversions incorrect")
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
        
    def testInversionsCount3(self):
        array = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        self.assertEqual(count, 590, "Number of inversions incorrect")
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")

    def testInversionsCount4(self):
        array = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        self.assertEqual(count, 2372, "Number of inversions incorrect")
        array.sort()
        print array
        self.assertEqual(array, sortedArray, "Arrays are not equal")
        
    def testProblemSet(self):
        array = []
        with open('../IntegerArray.txt', 'r') as file:
            array = list(file.read().splitlines())
        array = map(int, array)
        
        inverseCount = MergeSort.MergeSort()
        sortedArray,count = inverseCount.SortAndCountInversions(array)        
        print count
        
    def testProblemSetBruteForce(self):
        array = []
        with open('../IntegerArrayShort.txt', 'r') as file:
            array = list(file.read().splitlines())
        array = map(int, array)
                
        count = 0
        n = len(array)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if array[i] > array[j]:
                    count = count + 1
        
        print count
    '''
            
    def testStrassenMatrixMultiplication(self):
        matrix_size = 4
        '''
        A = np.linspace(0,24, 16).reshape([matrix_size, matrix_size])
        B = np.linspace(0,24, 16).reshape([matrix_size, matrix_size])
        '''
        A = np.matrix("1 2; 3 4")
        B = np.matrix("1 2; 3 4")
        
        print A 
        print B 
         
        strassen = Strassen.Strassen()
        C = strassen.multiply(A, B)
        print C
        print A * B

                    
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)