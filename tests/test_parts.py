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
print(src)
#from test_interface import TestForMethodExist
from testing_utility.unittest_util import TestForMethodExist
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# target
import sys
print(sys.path)
from src.interface.intfc_com import (Parts)
#import src.parts
#from src.parts.parts_func import (NTC, PTC)

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
            
'''
@add_msg
class TestNTC(ResistTestMethods, unittest.TestCase):
    """
    Negative temperature coefficient thermistor.
    R(T) = R0*exp(B(1/T-1/T0))
    """
    _cls = NTC
    _parameter_names = ('temeperature_degC',)
    _paradict_val_pairs = (({'temeperature_degC':-30},216729.001660428 ),
                           ({'temeperature_degC':25},10000 ),
                           ({'temeperature_degC':80},1203.301326499)
                           )
    _initial_set = {'Resist_at_T2':10000,'T2':25, 'B_const':4050}

@add_msg
class TestPTC(ResistTestMethods, unittest.TestCase):
    _cls = PTC
    _parameter_names = ('temeperature_degC',)
    _paradict_val_pairs = () 
    # https://jp.mathworks.com/help/physmod/sps/ref/ptcthermistor.html
'''

if __name__=='__main__':
    unittest.main() 