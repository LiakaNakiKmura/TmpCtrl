# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:45:10 2020

@author: LiNaK
"""

# Standard module
import unittest

# 3rd party's module
import numpy as np
from numpy.testing import assert_array_equal

# Original module  
from context import src  # path setting

#from test_interface import TestForMethodExist
from testing_utility.unittest_util import TestForMethodExist
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# target
from src.com.com_parameter import (TempRange)

@add_msg 
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((TempRange,('set_range', 'get_list')),
                         )

class TempRangeClass(unittest.TestCase):
    def setUp(self):
        self.tr = TempRange()
        
    def test_get_range(self):
        _min = -40
        _max = 90
        _step = 10
        self.tr.set_range(_min, _max, _step)
        _correct_list = np.arange(_min, _max, _step)
        assert_array_equal(_correct_list, self.tr.get_list())

if __name__=='__main__':
    unittest.main() 