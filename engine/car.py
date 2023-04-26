from abc import abstractmethod

from engine.servicable import Serviceable
from engine.engine import Engine


class Car(Serviceable):
    def __init__(self,):
        self.engine = Engine()
        
   
    def needs_service(self):
        if self.engine.needs_service():
            return True
