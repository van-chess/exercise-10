import random
import unittest
import threading
from ex10_1 import sort

maxNumberOfThreads = 1
runMonitor = True

# not very elegant ...
def maxThreadNumber():
    global maxNumberOfThreads
    while runMonitor:
        if threading.active_count() > maxNumberOfThreads:
            maxNumberOfThreads = threading.active_count()

class TestMethods(unittest.TestCase):


    def testSort(self):
        global runMonitor
        self.assertEqual(sort([]), [])
        self.assertEqual(sort([2,3,4,1]), [1,2,3,4])
        self.assertEqual(sort([2,3,1]), [1,2,3])
        self.assertEqual(sort([1, 2, 3]), [1,2,3])
        self.assertEqual(sort([7, 4, 1,5,2,9]), [1,2,4,5,7,9])
        
        # starts a separate monitor thread that stores the 
        # number of running threads
        t = threading.Thread(target=maxThreadNumber)
        t.start()
        # run a sorting
        self.assertEqual(sort([7, 4, 1,5,2,9]), [1,2,4,5,7,9])
        # monitor thread can stop now
        runMonitor = False
        # wait for the monitor thread to actually stop
        t.join()
        # the number of threads running at a time should be higher than 2
        # (i.e., at least one other thread has been created at some point)
        self.assertGreater(maxNumberOfThreads, 2)
    

if __name__ == '__main__':
    unittest.main()
