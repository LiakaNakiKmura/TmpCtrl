# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:31:58 2020
@author: LiNaK
"""
# Standard module
import unittest

# 3rd party's module
from numpy.testing import assert_almost_equal

# Original module  
from context import src  # path setting
#from test_interface import TestForMethodExist
from testing_utility.unittest_util import TestForMethodExist
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# target
from src.interface.intfc_com import (ResistTempFunc, ResistParameter)

@add_msg 
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((ResistTempFunc,('get_func')),
                         )
    _class_attr_pairs = ((ResistParameter,('name')),
                         )

class ResistTempFuncTestMethods():
    '''
    Test for Maker of function for R(T)
    ResistTempFunc is the Maker.
    ResistParameter is the parameter for Maker. ResistParameter is set for 
    initializing the Maker.
    Maker is fixed with kinds of resistance such as resistance, thermistor,
    RTD.
    each resisntance's charactoristics are set in ResisParameter such as
    resistance value.
    '''
    
    _cls = ResistTempFunc # targe Resist class inherit Parts class.
    _parameter_base_cls = ResistParameter # Abstract class for initial setting.
    _parameter_set_cls = ResistParameter # initial setting for target class.
    _temp_resist_pairs = (())
    # pairs of resistance and temperature. ((t0, r0), (t1,r1),...)
    
    def setUp(self):
        self._resist_temp_func = self._cls(self._parameter_set_cls)
    
    def test_inherite(self):
        self.assertTrue(issubclass(self._cls, ResistTempFunc))
        self.assertTrue(issubclass(self._parameter_set_cls, 
                                   self._parameter_base_cls))
    
    def test_func_val(self):
        func = self._resist_temp_func.get_func()
        for t, r in self._resit_temp_pairs:
            assert_almost_equal(r, func(t))
               
class Resist_Parameter_Test():
    '''
    Test for concrete ResistParameter class.
    Each class contains the concrete some values and name.
    Each class inherate each ResistParameter that is for each kinds resisntance.
    '''
    _each_resist_prameter_cls = None # ResitPrameter class that is blongs to
    # concrete ResitaFunc
    
    _target_cls = ResistParameter # targe Resist class inherit Parts class.
    _name_value_pairs = {'name': '',
                         'val_name': 0} # value name and value pairs.
    
    def setUp(self):
        self.pararameter = self._target_cls()
    
    def test_inherite(self):
        self.assertTrue(issubclass(self._target_cls, ResistParameter))
        self.assertTrue(issubclass(self._target_cls, 
                                   self._each_resist_prameter_cls))
    
    def test_value_name_exist(self):
        for k in self._name_value_pairs.keys():
            self.assertTrue(hasattr(self._target_cls, k))
    
    def test_parameter_values(self):
        for n, v in self._name_value_pairs.items():
            self.assertEqual(getattr(self.pararameter, n), v)
    
class ResistList():pass
class TempRangeClass():pass

"""
class TestRTD(unittest.TestCase): pass
    # 5000ppm/degC, 3000Ohm
"""

if __name__=='__main__':
    unittest.main() 