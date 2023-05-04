import unittest

from tire.carrigan_tire import CarriganTire


class CarriganTest(unittest.TestCase):
    def test_needs_service_true(self):
        
        arr = [0.1, 0.2, 0.9, 1.0, 1.1] 
        tire = CarriganTire(arr)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        
        arr = [0.1, 0.2, 0.4, 1.0, 1.1] 
        tire = CarriganTire(arr)
        self.assertTrue(tire.needs_service())