from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, arr):
        self.arr= arr

    def needs_service(self):
        return sum(self.arr) >= 3
