import random
import threading
import time

'''In file ex10-2.py, you find parts of an implementation to simulate a zoo. The zoo itself is represented by the class World 
and is populated with mice (represented by the class Mouse). Mice basically sleep and eat, but the access to food is restricted. 
At most two mice can eat at the same time, and the amount of food is limited (but replenished after 12 seconds).

Please implement the method day() in the class Mouse, following its the documentation.'''

class Mouse(threading.Thread):
    def __init__(self, world, name):
        threading.Thread.__init__(self)
        self.name = name
        self.world = world
        self.foodlevel = 1
    
    def day(self):
        time.sleep(random.randint(1, 5))# mouse can sleep for u to 5 seconds, otherwise it dies, because it doesn't eat
        if self.world.foodAvailable:
            mouse_thread = threading.Thread(target=self.world.food_lock.acquire)
            mouse_thread.start()
            mouse_thread.join()
            if self.world.foodAvailable:
                self.foodlevel += 1 # add one to food level of mouse
                self.world.foodAvailable -= 1 # subtract one from the world
            self.world.food_lock.release()#Increase the counter and return
            time.sleep(1)
        else:
            time.sleep(1)


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
        pass
    
    def run(self):
        while True:
            self.day()

class World(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.animals = []
        self.foodAvailable = 10
        max_mice = 2# making sure only two mice attempt to eat food
        self.food_lock = threading.Semaphore(max_mice)
    
    def addAnimal(self, animal):
        self.animals.append(animal)
    
    def day(self):
        """One day is passing. At the end of the day, 
        the food reserves are filled by a random integer.
        """
        time.sleep(12)
        for a in self.animals:
            a.foodlevel-=1
            self.animals = [a for a in self.animals if a.foodlevel >= 0]# self animals are all mice whose foodlevel is bogger than 0
            print("Animals left: " + str(len(self.animals)))
            if(len(self.animals)) == 0:
                print("All mice dead!")
                quit()

        for a in self.animals:
            print(a.name, ":", a.foodlevel)
            if a.foodlevel<= 0:
                print(a.name, " died")

        self.foodAvailable += random.randint(2, 10)
        print("Added to stack: ", self.foodAvailable)
    
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
