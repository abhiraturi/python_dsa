''''
Lets use interface for comprehension example
'''

from abc import ABC, abstractmethod

class Comprehension(ABC):
    @abstractmethod
    def using_comprehension(self):
        pass 


class CalculateListSquare(Comprehension):
    def using_comprehension(self,lst):
        lst_square=[i*i for i in lst]
        print(f"square of the list {lst} is {lst_square}")

class CalculateSetSquare(Comprehension):
    def using_comprehension(self,set):
        set_square={i*i for i in set}
        print(f"square of the set {set} is {set_square}")

class CalculateDictionarySquare(Comprehension):
    def using_comprehension(self,dict):
        dict_square={key: value*value for key,value in dict.items()}
        print(f"square of the dictionary values for {dict} is {dict_square}")

def main():
    lst=CalculateListSquare()
    lst.using_comprehension([1,2,3])

    set1=CalculateSetSquare()
    set1.using_comprehension({1,2,3})
    
    dict=CalculateDictionarySquare()
    dict.using_comprehension({'a':1,'b':2,'c':3})


if __name__=='__main__':
    main()