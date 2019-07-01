import random
import threading
import time

class Mouse(threading.Thread):
    def __init__(self, world, name):
        threading.Thread.__init__(self)
        self.name = name
        self.world = world
        self.foodlevel = 1
        self.alive = True
    
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
        sleeping_time = random.randint(1,2)
        time.sleep(sleeping_time)
        self.attempts = 2
        eat_timer = threading.Timer(6, self.starving)
        eat_timer.start()
        
        if self.attempts >=1:
            attempt_timer = threading.Timer(1, self.world.food_sem.release)
            self.world.food_sem.acquire()
            attempt_timer.start()
            if self.world.foodAvailable >=1:
                self.world.foodAvailable -= 1
                self.foodlevel += 1
                eat_timer.cancel()
                self.attempts -= 1

        
    def starving(self):
        self.foodlevel = 0
        self.alive = False
    
    def run(self):
        while self.alive:
            self.day()


        

class World(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.animals = []
        self.foodAvailable = 10
        self.food_sem = threading.Semaphore(2)
    
    def addAnimal(self, animal):
        self.animals.append(animal)
    
    def day(self):
        """One day is passing. At the end of the day, 
        the food reserves are filled by a random integer.
        """
        time.sleep(12)
        for animal in self.animals:
            if animal.foodlevel == 0:
                self.animals.remove(animal)
                
        print("Animals: " + str(len(self.animals)))
        self.foodAvailable += random.randint(0,10)
    
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

