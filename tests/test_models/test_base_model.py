#!/usr/bin/python3
"""test BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def setUp(self):
        self.testbasemodel = BaseModel()

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_save_BaseModel(self):
        """test save_Basemodel"""
        base = BaseModel()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
        '''test to json'''

    def test_kwarg(self):
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == "__main__":
    unittest.main()
