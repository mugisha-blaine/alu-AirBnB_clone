#!/usr/bin/python3
""" unit test for class User """

from models import User
import unittest


class TestUser(unittest.TestCase):
    """Test Cases for User model
    """

    def test_email(self):
        """Test user mail"""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "ssam@gmail.com"
        self.assertEqual(user.email, "ssam@gmail.com")

    def test_password(self):
        """Test user password"""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "wosswobi"
        self.assertEqual(user.password, "wosswobi")

    def test_first_name(self):
        """Test user first_name"""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "sammy"
        self.assertEqual(user.first_name, "sammy")

    def test_last_name(self):
        """Test user last_name"""
        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "gbolahan"
        self.assertEqual(user.last_name, "gbolahan")


if __name__ == "__main__":
    unittest.main()
