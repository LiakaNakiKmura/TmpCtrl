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
from test_ele_parts.test_parts import (ResistTempFuncTestMethods,
                                       Resist_Parameter_Test,
                                       ResistFuncFactoryTest)

# target
from src.interface.intfc_com import (ResistParameter)
from src.ele_parts.ntc import (NTC_Parameter, NTCFuncClass, 
                               NTC_FuncFactory, 
                               NTC_Sample1, NTC_Sample2)

@add_msg
class TestNTC_func(ResistTempFuncTestMethods, unittest.TestCase):
    _cls = NTCFuncClass # targe Resist class inherit Parts class.
    _parameter_base_cls = NTC_Parameter # Abstract class for initial setting.
    _parameter_set_cls = NTC_Sample1 # initial setting for target class.
    _resit_temp_pairs = ((-30, 216729.001660428 ),
                         (25, 10000),
                         (80, 1203.301326499))

@add_msg
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_attr_pairs = ((NTC_Parameter,('T0', 'R0', 'B')),
                         )

class NTC_Par_Test2(Resist_Parameter_Test):
    _each_resist_prameter_cls = NTC_Parameter
    _name_value_pairs = {'name': '',
                         'T0': 0,
                         'R0': 1000,
                         'B': 0} # value name and value pairs.    

@add_msg
class TestNTC_Sample1(NTC_Par_Test2, unittest.TestCase):
    _target_cls = NTC_Sample1
    _name_value_pairs = {'name': 'NTC Sample1',
                         'T0': 25,
                         'R0': 10000,
                         'B': 4050} # value name and value pairs.

@add_msg
class TestNTC_Sample2(NTC_Par_Test2, unittest.TestCase):
    _target_cls = NTC_Sample2
    _name_value_pairs = {'name': 'NTC Sample2',
                         'T0': 25,
                         'R0': 20000,
                         'B': 5000} # value name and value pairs.

@add_msg
class TestNTC_FuncFactory(ResistFuncFactoryTest, unittest.TestCase):
    _Maker = NTC_FuncFactory
    pass


if __name__=='__main__':
    unittest.main() 