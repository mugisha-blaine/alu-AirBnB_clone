#!/usr/bin/python3
""" Tests Amenity """

import unittest
import os
import datetime
from models import Amenity


class Test_Amenity(unittest.TestCase):
    """ Tests amenity """

    def test_Amenity_dict(self):
        """Amenity_dict"""
        amenity = Amenity()
        self.assertTrue('id' in amenity.to_dict())
        self.assertTrue('created_at' in amenity.to_dict())
        self.assertTrue('updated_at' in amenity.to_dict())
        self.assertTrue('__class__' in amenity.to_dict())

    def test_save_Amenity(self):
        """Amenity save"""
        amenity = Amenity()
        self.assertEqual(amenity.created_at, amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
