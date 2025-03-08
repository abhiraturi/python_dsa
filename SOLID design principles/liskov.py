'''
Before LSP (Violation)

class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly!")

'''
'''

# Derived classes should be substitutable for their base class without altering behavior.


This statement is the Liskov Substitution Principle (LSP) in object-oriented programming.
It means that if a class (subclass/child) extends another class (base/parent), the subclass should be able to replace the parent without causing unexpected issues or breaking functionality.

🔹 Key Idea:
If a function, method, or module is designed to work with a base class, it should also work seamlessly when given a derived class, without requiring modifications or extra conditions.


Why?
Proper Abstraction:

The base class Bird is now an abstract class (ABC), enforcing common behavior (eats()).
Bird does not assume that all birds can fly, avoiding the LSP violation.
Separation of Concerns:

Birds that can fly inherit from FlyingBird.
Birds that cannot fly inherit from NonFlyingBird.
This ensures that each subclass only implements behaviors that make sense for it.
No Unexpected Behavior:

Calling .fly() on a FlyingBird works as expected.
Calling .fly() on a NonFlyingBird does not raise an exception—it just clearly states that the bird cannot fly.
'''

from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def eats(self):
        pass


class NonFlyingBird(Bird):
    def eats(self):
        print("I am eating")

    def fly(self):
        print("I cannot fly")


class FlyingBird(Bird):
    def eats(self):
        print("I am eating")

    def fly(self):
        print("I can fly")


def main():
    penguin=NonFlyingBird()
    penguin.eats()
    penguin.fly()

    eagle=FlyingBird()
    eagle.eats()
    eagle.fly()


if __name__=='__main__':
    main()