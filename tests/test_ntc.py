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

# target
from src.interface.intfc_com import (ResistTempFunc, ResistParameter)
from src.ele_parts.ntc import (NTC_Parameter, NTC_Sample1)

@add_msg
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_attr_pairs = ((NTC_Parameter,('T0', 'R0', 'B')),
                         )



class ResistTestMethods():
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
class TestNTC(ResistTestMethods, unittest.TestCase):
    _cls = NTC_Sample1 # targe Resist class inherit Parts class.
    _name = "NTC Sample1"
    _T0 = 25
    _R0 = 10000
    _B = 4050


    
"""
    _initial_set = {'R0':10000,'T0':25, 'B':4050}
    _paradict_val_pairs = (({'temeperature_degC':-30},216729.001660428 ),
                           ({'temeperature_degC':25},10000 ),
                           ({'temeperature_degC':80},1203.301326499)
                           )
"""

if __name__=='__main__':
    unittest.main() 