# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:58:03 2020

@author: LiNaK
"""

# Standard module

# 3rd party's module
import numpy as np

# Original module  
from context import src  # path setting
from src.interface.intfc_com import (ResistTempFunc, ResistParameter,
                                     ResistFuncMaker)
from src.ele_parts.common_classes import (ResistFuncMaker_Com)

class NTCFuncClass(ResistTempFunc):
    def __init__(self, Parameter):
        par = Parameter()
        self._r0 = par.R0
        self._b = par.B
        self._t0_degC = par.T0 
        
    def get_func(self):
        T0 = self._t0_degC + 273 # FIXME: Make absolute temperature class.
        R0 = self._r0
        B = self._b
        def func(t1_degC):
            T1 = t1_degC + 273
            return R0*np.exp(B*(1/T1- 1/T0))
        return func

class NTC_Parameter(ResistParameter): 
    _T0 = 25
    _R0 = 0
    _B = 1
    
    @property
    def T0(self):
        return self._T0
    
    @property
    def R0(self):
        return self._R0
    
    @property
    def B(self):
        return self._B

class NTC_Sample1(NTC_Parameter):
    _name = "NTC Sample1"
    _T0 = 25
    _R0 = 10000
    _B = 4050

class NTC_Sample2(NTC_Parameter):
    _name = "NTC Sample2"
    _T0 = 25
    _R0 = 20000
    _B = 5000

class NTC_FuncFactory(ResistFuncMaker_Com):
    _kindlist = (NTC_Sample1, NTC_Sample2)
    _func_cls = NTCFuncClass
    _name = 'NTC thermistor'
