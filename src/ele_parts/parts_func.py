# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:09:39 2020

@author: LiNaK
"""

# Standard module

# 3rd party's module
import numpy as np

# Original module  
from src.interface.intfc_com import (Parts)
# comment
a=0

class NTC(Parts): 
    '''
    Negative temperature coefficient thermistor.
    Resistance has the following relation.
       R(T) = R0*exp(B(1/T-1/T0))
    R0, B, T0 is needed to be set.
    Return resistance at T.
    '''
    _parameter_names = ('temeperature_degC',)
    def __init__(self, Resist_at_T2, B_const,  T2 = 25):
        self._r0 = Resist_at_T2
        self._b = B_const
        self._t0_degC = T2 # 25 degreeC is the reference temperature usually.
        self._temp_degC =None # target temperature of thermistor. 
    
    def get_value(self):
        T1 = self._temp_degC + 273 # FIXME: Make absolute temperature class.
        R0 = self._r0
        T0 = self._t0_degC + 273
        B = self._b
        return R0*np.exp(B*(1/T1- 1/T0))

    def set_parameter(self,temeperature_degC):
        self._temp_degC = temeperature_degC
    
    def get_parameter_name(self):
        return self._parameter_names

class PTC(Parts):
    _parameter_names = ('temeperature_degC',)
    
    def get_value(self):
        return []
        pass

    def set_parameter(self):
        pass

    def get_parameter_name(self):
        return self._parameter_names