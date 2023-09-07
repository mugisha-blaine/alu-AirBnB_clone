#!/usr/bin/python3
"""Test BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def test_save_BaseModel(self):
        """test save_Basemodel"""
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
        '''test to json'''

    def test_kwarg(self):
        basemodel = BaseModel()
        self.assertEqual(basemodel.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == "__main__":
    unittest.main()
