from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, arr):
        self.arr= arr

    def needs_service(self):
        return any(num >= 0.9 for num in self.arr)
