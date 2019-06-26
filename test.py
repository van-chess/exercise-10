import random
import unittest
import threading
from ex10_1 import sort

maxNumberOfThreads = 1
sortRunning = True

def maxThreadNumber():
    global maxNumberOfThreads
    while sortRunning:
        if threading.active_count() > maxNumberOfThreads:
            maxNumberOfThreads = threading.active_count()

class TestMethods(unittest.TestCase):


    def testSort(self):
        global sortRunning
        self.assertEqual(sort([]), [])
        self.assertEqual(sort([2,3,4,1]), [1,2,3,4])
        self.assertEqual(sort([2,3,1]), [1,2,3])
        self.assertEqual(sort([1, 2, 3]), [1,2,3])
        self.assertEqual(sort([7, 4, 1,5,2,9]), [1,2,4,5,7,9])
        
        t = threading.Thread(target=maxThreadNumber)
        t.start()
        self.assertEqual(sort([7, 4, 1,5,2,9]), [1,2,4,5,7,9])
        sortRunning = False
        t.join()
        self.assertGreater(maxNumberOfThreads, 1)
    

if __name__ == '__main__':
    unittest.main()
