# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:58:03 2020

@author: LiNaK
"""

# Standard module
import abc

# 3rd party's module

# Original module  
from context import src  # path setting
from src.interface.intfc_com import (ResistParameter)


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
