#!/usr/bin/python3

import unittest
from models.base import Base
import json


class Test_base_class(unittest.TestCase):
    '''unittests for base class'''
    def test_base_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(15)
        b4 = Base(11)
        b5 = Base(89)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 15)
        self.assertEqual(b4.id, 11)
        self.assertEqual(b5.id, 89)
        b6 = Base("A string")
        self.assertEqual(b6.id, "A string")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
