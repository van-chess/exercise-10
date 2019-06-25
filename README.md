# Exercise 10

## Part 1: Parallelize `mergesort`

In file `ex10-1.py`, you find the merge sort implementation we discussed June 18. Recursive algorithms that follow the "divide and conquer" approach have a "natural" way of being parallelized: By running the recursion steps in separate threads. In this case, each call to `sort()` may start to threads that work on parts of the data.

## Part 2: Zoo Simulation

In file `ex10-2.py`, you find parts of an implementation to simulate a zoo. The zoo itself is represented by the class `World` and is populated with mice (represented by the class `Mouse`). Mice basically sleep and eat, but the access to food is restricted. At most two mice can eat at the same time, and the amount of food is limited (but replenished after 12 seconds).

Please implement the method `day()` in the class `Mouse`, following its the documentation.

