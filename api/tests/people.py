__author__ = 'jeanmarie'

from unittest import TestCase

class People(TestCase):
    def testCreate(self):
        users = [{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]
        self.assertEqual(True,True)
