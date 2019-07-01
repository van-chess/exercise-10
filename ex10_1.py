
'''
    1.Make a class MergeSort (the name doesn't matter), which takes the list that is to
    be sorted as an argument when initialized.
    2.The existing code for the function (in sort()) basically goes into the run() method of the class.
    However, whenever something is returned, it is instead stored as a variable in the object
    (e.g., self.result).
    3. Add a new method called getResult() that just returns the result value.
    4. Finally, in order for the tests to succeed, add a new function to the file that
    is called sort(), that internally creates the MergeSort object, and starts it as a thread.
'''
import random
import time
import threading

class MergeSort(threading.Thread):
    def __init__(self, l):
        threading.Thread.__init__(self)
        self.list = l
        self.result=[]# create empty list for storing result
        self.start()
        self.join()


    def run(self):
        if len(self.list) <= 1: # base case
            self.result = self.list
            return self.result
        else:
            split_point = round(len(self.list) / 2)
            self.r = []

            # parallelize calls to sort() here
            half1 = MergeSort(self.list[0:split_point])
            half2 = MergeSort(self.list[split_point:])
            p1 = half1.result
            p2 = half2.result


            while (len(p1) > 0 and len(p2) > 0):
                if p1[0] > p2[0]:
                    self.r.append(p2.pop(0))
                else:
                    self.r.append(p1.pop(0))
            while len(p1) > 0:
                self.r.append(p1.pop(0))
            while len(p2) > 0:
                self.r.append(p2.pop(0))
                return self.r

    def getResult(self):
        return self.result

#new function outside of class
def sort(l):
    s = MergeSort(l)
    s.join()
    return s.result


if __name__ == "__main__":
    for i in [1, 10, 100, 1000, 10000]:
        t = time.process_time()
        unsorted_list = random.sample(range(1, 999999), i)
        s = sort(unsorted_list)
        print(str(i) + ": " + str(time.process_time() - t))
        print("sorted list:", s)