'''
you can use simple functions without abstract classes and methods which works fine, 
but there's no guarantee that all vehicles will have start_engine() and stop_engine(). 
Someone might create a new class without these methods, breaking the expected behavior.

So, in order to force that new classes or all subclasses should have start and stop engine function 
you can use interface and abstract classes which will error out if you miss any of these start ans stop engine functions
in any sub classes, so you have better control.



With just functions you will have more flexibility but less control.

With interface you have more control.
'''

from abc    import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car_Vehicle(Vehicle):
    def start_engine(self):
        print("Starting car engine")

    def stop_engine(self):
        print("Stopping car engine")


def main():
    car1=Car_Vehicle()
    car1.start_engine()
    car1.stop_engine()


if __name__=="__main__":
    main()
