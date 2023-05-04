import unittest

from tire.octoprime_tire import OctoprimeTire


class OctoprimeTest(unittest.TestCase):
    def test_needs_service_true(self):
        
        arr = [0.1, 2.2, 0.9, 1.0, 1.1] 
        tire = OctoprimeTire(arr)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        
        arr = [0.1, 0.1, 0.6, 1.0, 0.1] 
        tire = OctoprimeTire(arr)
        self.assertTrue(tire.needs_service())