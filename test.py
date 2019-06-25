import random
import unittest
from ex10_1 import sort

class TestMethods(unittest.TestCase):

    def testSort(self):
        self.assertEqual(sort([]), [])
        self.assertEqual(sort([2,3,4,1]), [1,2,3,4])
        self.assertEqual(sort([2,3,1]), [1,2,3])
        self.assertEqual(sort([1, 2, 3]), [1,2,3])
        self.assertEqual(sort([7, 4, 1,5,2,9]), [1,2,4,5,7,9])
    

if __name__ == '__main__':
    unittest.main()
