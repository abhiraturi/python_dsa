'''
Before ISP:

class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Working...")

    def eat(self):
        print("Eating...")

class RobotWorker(Worker):
    def work(self):
        print("Working...")

    def eat(self):
        raise Exception("Robots don't eat!")

'''

#  implementing ISP now for the above code

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eats(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker,Eats):
    def work(self):
        print("Working...")

    def eat(self):
        print("Eating...")

class RobotWorker(Worker):
    def work(self):
        print("Working...")


def main():
    human=HumanWorker()
    human.eat()
    human.work()


    robot=RobotWorker()
    robot.work()

if __name__=='__main__':
    main()
