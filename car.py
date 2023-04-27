from servicable import Serviceable


class Car(Serviceable):
    
    #each car has an engine and battery so we initialize them here
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
   
    def needs_service(self):
        return self.engine.needs_service or self.battery.need_service()
