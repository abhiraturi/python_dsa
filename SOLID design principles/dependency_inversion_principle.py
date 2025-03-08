'''
Before DIP principle

class Keyboard:
    def connect(self):
        print("Keyboard connected")

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()  # Direct dependency

'''

'''
Implementing DIP principle for above code now

Dependency Inversion Principle (DIP):
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.

'''

from abc import ABC, abstractmethod

class InputDevice(ABC):
    @abstractmethod
    def connect(self):
        pass


class Keyboard(InputDevice):
    def connect(self):
        print(f"Keyboard Connected")


class Mouse(InputDevice):
    def connect(self):
        print(f"Mouse connected")


class Computer:
    def __init__(self,device:InputDevice) -> None:
        self.device=device

    def connect_device(self):
        self.device.connect()
        
def main():
    keyboard=Keyboard()
    mouse=Mouse()

    # connect keyboard
    comp=Computer(keyboard)
    comp.connect_device()

    # connect mouse
    comp=Computer(mouse)
    comp.connect_device()
    

if __name__=='__main__':
    main()

