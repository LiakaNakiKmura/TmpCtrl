# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:44:43 2020

@author: LiNaK
"""

# Standard module
import unittest

# 3rd party's module
from numpy.testing import assert_almost_equal

# Original module  
from context import src  # path setting
from testing_utility.unittest_util import TestForMethodExist
from testing_utility.unittest_util import cls_startstop_msg as add_msg
from test_ele_parts.test_parts import (ResistTempFuncTestMethods)

# target
from src.interface.intfc_com import (ResistParameter)
from src.ele_parts.norm_resist import (NormResistParameter, ResistFuncClass, 
                               R10Ohm)

@add_msg
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_attr_pairs = ((NormResistParameter,('R',)),
                         )

"""
@add_msg
class TestNTC_func(ResistTempFuncTestMethods, unittest.TestCase):
    _cls = ResistFuncClass # targe Resist class inherit Parts class.
    _parameter_base_cls = NormResistParameter # Abstract class for initial setting.
    _parameter_set_cls = Resist_Sample1 # initial setting for target class.
    _resit_temp_pairs = ((-30, 216729.001660428 ),
                         (25, 10000),
                         (80, 1203.301326499))
"""

class NormResist_par_Test():
    '''
    Test for concrete NormResistParameter class.
    Each class contains the concrete R value and name.
    Each class inherate NormResistParameter.
    '''
    _cls = NormResistParameter # targe Resist class inherit Parts class.
    _name = ""
    _R = None
    
    def setUp(self):
        self.par = self._cls()
    
    def test_inherite(self):
        self.assertTrue(issubclass(self._cls, ResistParameter))
        self.assertTrue(issubclass(self._cls, NormResistParameter))
    
    def test_parameters(self):
        for p, v in ((self.par.name, self._name),
                     (self.par.R, self._R),
                     ):
            self.assertEqual(p, v)

   
@add_msg
class TestNTC_Sample1(NormResist_par_Test, unittest.TestCase):
    _cls = R10Ohm # targe Resist class inherit Parts class.
    _name = "10Ohm"
    _R = 10



if __name__=='__main__':
    unittest.main() 