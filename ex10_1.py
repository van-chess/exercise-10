import random
import time

def sort(l):
    if len(l) <= 1: # base case
        return l
    else: # recursion
        r = []
        splitPoint = round(len(l)/2)
        # parallelize these calls
        p1 = sort(l[0:splitPoint])
        p2 = sort(l[splitPoint:])
        
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
    for i in [1, 10, 100, 1000, 10000, 100000]:
      t = time.process_time()
      s = sort(random.sample(range(1, 999999), i))
      print(str(i) + ": " + str(time.process_time() - t))