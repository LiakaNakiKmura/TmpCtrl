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
from test_ele_parts.test_parts import (ResistTempFuncTestMethods,
                                       Resist_Parameter_Test,
                                       ResistFuncMakerTest)

# target
from src.interface.intfc_com import (ResistParameter)
from src.ele_parts.fix_resist import (FixResistParameter, FixResistFuncClass, 
                               R10Ohm, FixResistFuncMaker)

@add_msg
class TestFixResist_func(ResistTempFuncTestMethods, unittest.TestCase):
    _cls = FixResistFuncClass # targe Resist class inherit Parts class.
    _parameter_base_cls = FixResistParameter # Abstract class for initial setting.
    _parameter_set_cls = R10Ohm # initial setting for target class.
    _resit_temp_pairs = ((-30, 10),
                         (25, 10),
                         (80, 10))

@add_msg
class TestResistTempFuncInterFace(TestForMethodExist, unittest.TestCase):
    _class_attr_pairs = ((FixResistParameter,('R',)),
                         )

class FixResist_par_Test(Resist_Parameter_Test):
    _each_resist_prameter_cls = FixResistParameter
    _name_value_pairs = {'name': '',
                         'R': 0} # value name and value pairs.

@add_msg
class TestR10Ohm(FixResist_par_Test, unittest.TestCase):
    _target_cls = R10Ohm 
    _name_value_pairs =   {'name': '10Ohm',
                         'R': 10} # value name and value pairs.

@add_msg
class TestFixResist_FuncFactory(ResistFuncMakerTest, unittest.TestCase):
    _Maker = FixResistFuncMaker

if __name__=='__main__':
    unittest.main() 