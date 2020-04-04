# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:23:54 2020

@author: LiNaK
"""

# Standard module



# Original module  
from context import src  # path setting
from src.interface.intfc_com import (ResistTempFunc, ResistParameter)

class FixResistParameter(ResistParameter): 
    _R = None
    
    @property
    def R(self):
        return self._R

class FixResistFuncClass(ResistTempFunc):
    '''
    Fixed Resistance. The resitance of this class will not be changed. 
    '''
    def __init__(self, Parameter):
        self.para = Parameter()
        
    def get_func(self):
        return lambda x: self.para.R

class R10Ohm(FixResistParameter):
    _name = '10Ohm'
    _R = 10