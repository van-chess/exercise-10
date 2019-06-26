import random
import threading
import time


class Mouse(threading.Thread):
    def __init__(self, world, name):
        threading.Thread.__init__(self)
        self.name = name
        self.world = world
        self.foodlevel = 1
    
    def day(self):
        """One day for a mouse passes. In each day, 
        a mouse sleeps for a random amount of time.
        After that, the mouse makes two attempts at eating.
        Only two mice can eat at the same time (the others)
        have to wait. If a mouse waits for more than 6 seconds, 
        it starves.
        An attempt consists of the following:
        - make sure that at most two mice make the attempt
        - check if food is available
        - if food is available: Subtract one food from world 
          and add it to the mouse
        - if no food is available, the mouse leaves the food 
          place immediately.
        - The attempt takes one second, even if unsuccessful.
        """
        time.sleep(random.randint(1, 5))  # regular sleep
        ts = time.time()
        if self.world.foodAvailable:
            sub = threading.Thread(target=self.world.food_lock.acquire)
            sub.start()
            sub.join()
            if self.world.foodAvailable:
                self.foodlevel += 1
                self.world.foodAvailable -= 1
            self.world.food_lock.release()
        rest = 1 - time.time() - ts
        rest = rest if rest >= 0 else 0
        time.sleep(rest)

    def run(self):
        while True:
            self.day()


class World(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.animals = []
        self.foodAvailable = 10
        self.food_lock = threading.Semaphore(2)
    
    def addAnimal(self, animal):
        self.animals.append(animal)
    
    def day(self):
        """One day is passing. At the end of the day, 
        the food reserves are filled by a random integer.
        """
        time.sleep(12)
        for a in self.animals:
            a.foodlevel -= 1
        self.animals = [a for a in self.animals if a.foodlevel >= 0]  # kill all the weak mice
        print("Animals: " + str(len(self.animals)))
        for a in self.animals:
            print(a.name, ":", a.foodlevel)
        self.foodAvailable += random.randint(2, 10)
    
    def run(self):
        """The thread runs indefinitely, until someone crashes 
        the program.
        """
        while True:
            self.day()


if __name__ == "__main__":
    w = World()
    w.start()
    for i in range(20):
        a = Mouse(w, "Mouse " + str(i))
        w.addAnimal(a)
        a.start()
