# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:41:07 2020

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
from src.ele_parts.ntc import (NTC_Parameter, NTCFuncClass, 
                               NTC_Sample1, NTC_Sample2)

@add_msg
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_attr_pairs = ((NTC_Parameter,('T0', 'R0', 'B')),
                         )


@add_msg
class TestNTC_func(ResistTempFuncTestMethods, unittest.TestCase):
    _cls = NTCFuncClass # targe Resist class inherit Parts class.
    _parameter_base_cls = NTC_Parameter # Abstract class for initial setting.
    _parameter_set_cls = NTC_Sample1 # initial setting for target class.
    _resit_temp_pairs = ((-30, 216729.001660428 ),
                         (25, 10000),
                         (80, 1203.301326499))

class NTC_Par_Test():
    '''
    Test for concrete NTC Parameter class.
    Each class contains the concrete T0, R0, B value and name.
    Each class inherate NTC_Parameter.
    '''
    _cls = NTC_Parameter # targe Resist class inherit Parts class.
    _name = ""
    _T0 = 25
    _R0 = 100000
    _B = 0
    
    def setUp(self):
        self.par = self._cls()
    
    def test_inherite(self):
        self.assertTrue(issubclass(self._cls, ResistParameter))
        self.assertTrue(issubclass(self._cls, NTC_Parameter))
    
    def test_parameters(self):
        for p, v in ((self.par.name, self._name),
                     (self.par.T0, self._T0),
                     (self.par.R0, self._R0),
                     (self.par.B, self._B)
                     ):
            self.assertEqual(p, v)
    

@add_msg
class TestNTC_Sample1(NTC_Par_Test, unittest.TestCase):
    _cls = NTC_Sample1 # targe Resist class inherit Parts class.
    _name = "NTC Sample1"
    _T0 = 25
    _R0 = 10000
    _B = 4050

@add_msg
class TestNTC_Sample2(NTC_Par_Test, unittest.TestCase):
    _cls = NTC_Sample2 # targe Resist class inherit Parts class.
    _name = "NTC Sample2"
    _T0 = 25
    _R0 = 20000
    _B = 5000


if __name__=='__main__':
    unittest.main() 