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
from src.interface.intfc_com import (Parts, ResistTempFunc, ResistParameter)
from src.ele_parts.parts_func import (NTC, PTC)

@add_msg
class TestPartsInterFace(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Parts,('get_value','set_parameter',
                                 'get_parameter_name')),
                         )
    


class ResistTestMethods():
    _cls = Parts # targe Resist class inherit Parts class.
    _parameter_names = ('',) # collect parameter names by get_parameter_names.
    _paradict_val_pairs = (({'':None},0),) 
    # tuple of pair of parameter name, value dict and collect resist value.  
    _initial_set = {} # initial setting for target class.
    
    def setUp(self):
        self.parts = self._cls(**self._initial_set)
    
    def test_inherite(self):
        self.assertTrue(issubclass(self._cls, Parts))
    
    def test_parameter_names(self):
        parameter_names = self.parts.get_parameter_name()
        self.assertCountEqual(parameter_names, self._parameter_names)
    
    def test_get_parameter(self):
        for paradict, val in self._paradict_val_pairs:
            self.parts.set_parameter(**paradict)
            assert_almost_equal(val, self.parts.get_value())
 
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
               
 
"""
class TestRTD(unittest.TestCase): pass
    # 5000ppm/degC, 3000Ohm
"""

@add_msg
class TestNTC(ResistTestMethods, unittest.TestCase):
    """
    Negative temperature coefficient thermistor.
    R(T) = R0*exp(B(1/T-1/T0))
    """
    _cls = NTC
    _parameter_names = ('temeperature_degC',)
    _initial_set = {'R0':10000,'T0':25, 'B':4050}
    _paradict_val_pairs = (({'temeperature_degC':-30},216729.001660428 ),
                           ({'temeperature_degC':25},10000 ),
                           ({'temeperature_degC':80},1203.301326499)

                           )

@add_msg
class TestPTC(ResistTestMethods, unittest.TestCase):
    _cls = PTC
    _parameter_names = ('temeperature_degC',)
    _paradict_val_pairs = () 
    # https://jp.mathworks.com/help/physmod/sps/ref/ptcthermistor.html


if __name__=='__main__':
    unittest.main() 