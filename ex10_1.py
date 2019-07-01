import random
import time
import threading

class MergeSort(threading.Thread):
    def __init__(self, l):
        threading.Thread.__init__(self)
        self.list = l
        self.result = []
        self.start()
        self.join()


    def run(self):
        if len(self.list) <= 1:  # base case
            self.result.extend(self.list)
        else:  # recursion
            self.r = []
            splitPoint = round(len(self.list) / 2)

            # parallelize calls to sort() here
            x1 = MergeSort(self.list[0:splitPoint])
            x2 = MergeSort(self.list[splitPoint:])
            p1 = x1.result
            p2 = x2.result

            while (len(p1) > 0 and len(p2) > 0):
                if p1[0] > p2[0]:
                    self.r.append(p2.pop(0))
                else:
                    self.r.append(p1.pop(0))
            while len(p1) > 0:
                self.r.append(p1.pop(0))
            while len(p2) > 0:
                self.r.append(p2.pop(0))
            self.result.extend(self.r)

    def getresult(self):
        return self.result

def sort(l):
    result = MergeSort(l)
    return result.result



if __name__ == "__main__":
    for i in [1, 10, 100, 1000, 10000, 100000]:
      t = time.process_time()
      s = sort(random.sample(range(1, 999999), i))
      print(str(i) + ": " + str(time.process_time() - t))
      print(s)

