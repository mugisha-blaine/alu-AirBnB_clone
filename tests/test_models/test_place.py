#!/usr/bin/python3
""" Test Place """

import unittest
from models import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """ Tests Place """

    def test_Place_dict(self):
        """ Place_dict """
        place = Place()
        self.assertTrue('id' in place.__dict__)
        self.assertTrue('created_at' in place.__dict__)
        self.assertTrue('updated_at' in place.__dict__)
        self.assertTrue('__class__' in place.__dict__)

    def test_save_Place(self):
        """ Save_Place """
        place = Place()
        self.assertNotEqual(place.created_at, place.updated_at)


if __name__ == '__main__':
    unittest.main()
