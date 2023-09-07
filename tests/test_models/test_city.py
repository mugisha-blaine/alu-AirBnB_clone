#!/usr/bin/python3
""" Test city """

import unittest
from models import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """ Tests city """

    def test_City_dict(self):
        """ City_dict """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('__class__' in self.city.__dict__)

    def test_save_City(self):
        """ save_city """
        city = City()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_inst(self):
        """ test_inst"""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
