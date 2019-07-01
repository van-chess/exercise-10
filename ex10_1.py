import random
import time
import threading


class MergeSort(threading.Thread):
    def __init__(self, list):
        threading.Thread.__init__(self)
        self.list = list
        self.start()

        
    def run(self):
        if len(self.list) <= 1: # base case
            self.result = self.list
        else: # recursion
            r = []
            splitPoint = round(len(self.list)/2)
            
            self.result = []
            # parallelize calls to sort() here
            p1 = MergeSort(self.list[0:splitPoint])
            p2 = MergeSort(self.list[splitPoint:])
            
            p1.join()
            p2.join()

            while(len(p1.result) > 0 and len(p2.result) > 0):
                if p1.result[0] > p2.result[0]:
                    self.result.append(p2.result.pop(0))
                else:
                    self.result.append(p1.result.pop(0))
            while len(p1.result) > 0:
                self.result.append(p1.result.pop(0))
            while len(p2.result) > 0:
                self.result.append(p2.result.pop(0))

    
    def getResult(self):
        return self.result

def sort(l):
    thread = MergeSort(l)
    thread.join()
    return thread.getResult()


def sort_orig(l):
    if len(l) <= 1: # base case
        return l
    else: # recursion
        r = []
        splitPoint = round(len(l)/2)

        # parallelize calls to sort() here
        p1 = sort_orig(l[0:splitPoint])
        p2 = sort_orig(l[splitPoint:])
        print(p1)
        print(p2)

        while(len(p1) > 0 and len(p2) > 0):
            if p1[0] > p2[0]:
                r.append(p2.pop(0))
            else:
                r.append(p1.pop(0))
        while len(p1) > 0:
            r.append(p1.pop(0))
        while len(p2) > 0:
            r.append(p2.pop(0))
        return r

if __name__ == "__main__":
    '''
    for i in [1, 10, 100, 1000, 10000, 100000]:
      t = time.process_time()
      s = sort(random.sample(range(1, 999999), i))
      print(str(i) + ": " + str(time.process_time() - t))
      
    '''
test_list = [7, 4, 1,5,2,9]
#print(sort_orig(test_list))
print(sort(test_list))
