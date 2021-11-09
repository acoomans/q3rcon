import unittest
from project import MyClass


class TestProject(unittest.TestCase):

    def setUp(self):
        self.myclass = MyClass()

    def testMessage(self):
        self.assertTrue('hello' in self.myclass.message)
