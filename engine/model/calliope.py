from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        #service theshold is every two years
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

        #if two years has passed or the milage is + 30000 miles or more 
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
