# Exercise 10

## Part 1: Parallelize `mergesort`

In file `ex10-1.py`, you find the merge sort implementation we discussed June 18. Recursive algorithms that follow the "divide and conquer" approach have a "natural" way of being parallelized: By running the recursion steps in separate threads. In this case, each call to `sort()` may start to threads that work on parts of the data.

**Remark (added June 26)**: There is no straightforward way to implement this in a way that `sort()` remains a function. The reason is that we don't get direct access to the return value of the function in a thread. It seems this should be possible [using a queue](https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python), but this requires changes in how the function is designed. It is, however, straightforward to implement this as a class. To this end, you'll need to do the following things:

1. Make a class MergeSort (the name doesn't matter), which takes the list that is to be sorted as an argument when initialized.
2. The existing code for the function (in `sort()`) basically goes into the `run()` method of the class. However, whenever something is returned, it is instead stored as a variable in the object (e.g., `self.result`).
3. Add a new method called `getResult()` that just returns the result value.
4. Finally, in order for the tests to succeed, add a new function to the file that is called `sort()`, that internally creates the MergeSort object, and starts it as a thread.

One more note: If you then run the code in the main part of `ex10_1.py`, you'll get errors when the list is more than 1000 elements long: `RuntimeError: can't start new thread`. The reason is that there is an upper limit on how many threads a process can create, and due to the recursion, a thread can only finish when all sub-threads have been finished. So this approach of recursive parallelization works only for relatively short lists. But is very fast :-)


## Part 2: Zoo Simulation

In file `ex10-2.py`, you find parts of an implementation to simulate a zoo. The zoo itself is represented by the class `World` and is populated with mice (represented by the class `Mouse`). Mice basically sleep and eat, but the access to food is restricted. At most two mice can eat at the same time, and the amount of food is limited (but replenished after 12 seconds).

Please implement the method `day()` in the class `Mouse`, following its the documentation.

