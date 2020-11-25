# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_init_name(self):
        place = Location('SLO', 35.3, -120.7)
        self.assertEqual('SLO', place.name)

    def test_init_lat(self):
        place = Location('SLO', 35.3, -120.7)
        self.assertEqual(35.3, place.lat)

    def test_init_lon(self):
        place = Location('SLO', 35.3, -120.7)
        self.assertEqual(-120.7, place.lon)

    def test_eq(self):
        place1 = Location('SLO', 35.3, -120.7)
        place2 = Location('SLO', 35.3, -120.7)
        self.assertEqual(place1, place2)

if __name__ == "__main__":
        unittest.main()
