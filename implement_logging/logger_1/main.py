import logger
from abc import ABC, abstractmethod


# Example usage
_logger = logger.setup_stdout_logger()


class People(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def gender(self):
        pass

    @abstractmethod
    def hobby(self):
        pass


class Abhi(People):

    def name(self,name):
        if name:
            _logger.info(f"Hello, my name is {name}")
        
        else:
            _logger.error("Name cannot be None")
        
    
    def gender(self,gender):
        if gender:
            _logger.info(f"My gender is {gender}")
      
        else:
             _logger.error("Gender cannot be None")
            


    def hobby(self,hobby):
        if hobby:
            _logger.info(f"My hobby is {hobby}")

        else:
            _logger.error("Hobby cannot be None")
            

def main():
    abhi=Abhi()
    abhi.name("Abhishek Raturi")
    abhi.gender("Male")
    abhi.hobby("Playing chess")


    artee=Abhi()
    artee.name("")
    artee.gender("")
    artee.hobby("Playing chess")

if __name__=='__main__':
    main()