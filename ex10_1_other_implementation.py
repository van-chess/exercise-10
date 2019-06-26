import random
import time
import threading


def sort(l):
    if len(l) <= 1: # base case
        return
    else:  # recursion
        splitPoint = round(len(l)/2)

        r = []

        # parallelize calls to sort() here
        p1 = l[:splitPoint]
        p2 = l[splitPoint:]
        t1 = threading.Thread(target=sort, args=[p1])
        t2 = threading.Thread(target=sort, args=[p2])
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        while len(p1) > 0 and len(p2) > 0:
            if p1[0] > p2[0]:
                r.append(p2.pop(0))
            else:
                r.append(p1.pop(0))

        while len(p1) > 0:
            r.append(p1.pop(0))
        while len(p2) > 0:
            r.append(p2.pop(0))

        for i, e in enumerate(r):
            l[i] = e


if __name__ == "__main__":
    for i in [1, 10, 100, 1000, 10000]:
        unsorted = random.sample(range(1, 999999), i)
        print("unsorted", unsorted)
        t = time.process_time()
        sort(unsorted)
        print(str(i) + ": " + str(time.process_time() - t))
        print("sorted:", unsorted)
