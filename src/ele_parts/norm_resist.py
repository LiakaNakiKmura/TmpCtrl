# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:23:54 2020

@author: LiNaK
"""

# Standard module
import abc


# Original module  
from context import src  # path setting
from src.interface.intfc_com import (ResistTempFunc, ResistParameter)

class NormResistParameter(ResistParameter): 
    _R = None
    
    @property
    def R(self):
        return self._R

class ResistFuncClass:pass

class R10Ohm(NormResistParameter):
    _name = '10Ohm'
    _R = 10