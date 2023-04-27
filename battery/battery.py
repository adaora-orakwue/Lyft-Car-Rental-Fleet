from abc import ABC

#Battery needs its own class since we pass it into the Car Object.We make it abstract
#since type of  will battery be defined in subclasses
class Battery(ABC):
    def needs_service(self):
        pass