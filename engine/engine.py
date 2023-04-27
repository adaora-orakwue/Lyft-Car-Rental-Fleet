
from abc import ABC


#Engine needs its own class since we pass it into the Car Object. We make it abstract
#since type of engine will be defined in subclasses
class Engine(ABC):
    
    def needs_service(self):
        pass
        
    