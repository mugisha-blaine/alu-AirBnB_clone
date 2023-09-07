#!/usr/bin/python3
""" unit test for class State """

from models.state import State
import os
import unittest


class TestStateDocs(unittest.TestCase):
    """ Test docstring in the class """

    def test_doc_class(self):
        """ Test document class """
        doc = State.__doc__
        self.assertIsNotNone(doc)

    def test_doc_methods_class(self):
        """ Test document methods Class """
        l_method = ["save", "__init__", "__str__", "to_dict"]
        for key in State.__dict__.keys():
            if key is l_method:
                doc = key.__doc__
                self.assertIsNotNone(doc)


class TestState(unittest.TestCase):
    """ Test creation objects and use methods """

    @classmethod
    def setUpClass(cls):
        ''' new_state up '''
        cls_state = State()
        cls_state.name = "Tunis"
        cls_state.save()
        cls_state_str = cls_state.to_dict()

    def test_create_object(self):
        """ Test created instance """
        new_state = State()
        self.assertIsInstance(new_state, State)

    def test_method_save(self):
        """ Test save method """
        new_state = State()
        current = new_state.updated_at
        new_state.save()
        new = new_state.updated_at
        self.assertNotEqual(current, new)

    def test_hasMethods(self):
        """test the instance have the methods"""
        new_state = State()
        self.assertTrue(hasattr(new_state, '__str__'))
        self.assertTrue(hasattr(new_state, '__init__'))
        self.assertTrue(hasattr(new_state, 'to_dict'))
        self.assertTrue(hasattr(new_state, 'save'))

    def test_add_attributes(self):
        """ add attributes to object"""
        new_state = State()
        new_state.name = "Tunis"
        list = [new_state.name]
        expected = ["Tunis"]
        self.assertEqual(expected, list)


if __name__ == '__main__':
    unittest.main()
