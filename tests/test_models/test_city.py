#!/usr/bin/python3
""" Test city """

import unittest
from models import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """ Tests city """

    def test_City_dict(self):
        """ City_dict """
        city = City()
        self.assertTrue('id' in city.to_dict())
        self.assertTrue('created_at' in city.to_dict())
        self.assertTrue('updated_at' in city.to_dict())
        self.assertTrue('__class__' in city.to_dict())

    def test_save_City(self):
        """ save_city """
        city = City()
        self.assertEqual(city.created_at, city.updated_at)

    def test_inst(self):
        """ test_inst"""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
