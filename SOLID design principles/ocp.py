'''
Before OCP (Violation)

class Discount:
    def apply_discount(self, amount, discount_type):
        if discount_type == "percentage":
            return amount * 0.9
        elif discount_type == "fixed":
            return amount - 10
        else:
            return amount  # No discount

'''

#  Using OCP, to add new discount type will be easier (lets use abstraction and interface)
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self,amount):
        pass

class PercentageDiscout(Discount):
    def apply(self,amount):
        return amount*0.9


class FixedDiscount(Discount):
    def apply(self,amount):
        return (amount - 10)

class NoDiscount(Discount):
    def apply(self,amount):
        return amount


def main():
    amount=100

    no_discount=NoDiscount()
    fixed_discount=FixedDiscount()
    percent_discount=PercentageDiscout()

    print(f"Amount before any discount is :  {amount}")
    print(f"Amount after percentage discount is :  {percent_discount.apply(amount)}")
    print(f"Amount after fixed discount is :  {fixed_discount.apply(amount)}")
    print(f"Amount after no discount is :  {no_discount.apply(amount)}")


if __name__=='__main__':
    main()


