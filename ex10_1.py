import random
import time
import threading


class MergeSort(threading.Thread):
    def __init__(self, l):
        threading.Thread.__init__(self)
        self.l = l
        self.start()


    def run(self):
        if len(self.l) <= 1:
            self.result = self.l
        else:
            split_point = round(len(self.l)/2)

            self.result = []
            p1 = MergeSort(self.l[:split_point])
            p2 = MergeSort(self.l[split_point:])

            p1.join()
            p2.join()

            l1 = p1.result
            l2 = p2.result

            while len(l1) > 0 and len(l2) > 0:
                if l1[0] > l2[0]:
                    self.result.append(l2.pop(0))
                else:
                    self.result.append(l1.pop(0))

            while len(l1) > 0:
                self.result.append(l1.pop(0))
            while len(l2) > 0:
                self.result.append(l2.pop(0))




def sort(l):
    s = MergeSort(l)
    s.join()
    return s.result


if __name__ == "__main__":
    for i in [1, 10, 100, 1000, 10000]:
        unsorted = random.sample(range(1, 999999), i)
        print("unsorted", unsorted)
        t = time.process_time()
        s = sort(unsorted)
        print(str(i) + ": " + str(time.process_time() - t))
        print("sorted:", s)
