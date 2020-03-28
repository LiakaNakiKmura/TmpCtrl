# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:31:58 2020
@author: LiNaK
"""
# Standard module
import unittest

# 3rd party's module

# Original module  
from context import src # path setting
#from test_interface import TestForMethodExist
from testing_utility.unittest_util import TestForMethodExist
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# target
from src.interface.intfc_com import (Parts)

@add_msg
class TestPartsInterFace(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Parts,('get_value','set_parameter',
                                 'get_parameter_name')),
                         )

@add_msg
class TestNTC(unittest.TestCase):
    pass

if __name__=='__main__':
    unittest.main() 