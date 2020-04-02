   
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 00:12:46 2019
@author: LiNaK
"""

# Standard module
import abc

# 3rd party's module

# Original module  

class Parts(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get_value(self):
        pass

    @abc.abstractmethod
    def set_parameter(self):
        pass

    @abc.abstractmethod
    def get_parameter_name(self):
        pass

class ResistTempFunc(metaclass = abc.ABCMeta):
    '''
    ResistTempFunc is the Maker of function for calucurate resistance at 
    desired temperature: R(T).
    ResistTempFunc needs ResistParameter to set parameters to calcurate.
    ResistTempFunc is fixed with kinds of resistance such as resistance, 
    thermistor,RTD.
    '''
    def __init__(self, _CLS):
        self._parameter = _CLS() 
    
    @abc.abstractmethod
    def get_func(self):
        pass

class ResistParameter(metaclass = abc.ABCMeta):
    '''
    ResistParameter is used for ResistTempFunc to be initialized.
    R(T) func is costrated with concrete value from ResistPrameter.
    This class is connected to concrete values such as 100Ohm or 1000Ohm.
    This class will be inherated to each resitance kinds such as resistance, 
    thermistor,RTD. Then base class for each resintance kinds is inherated.
    The inherated class has abstract parameters to constract ResistTempFunc.
    Concrete class inferate the class. Concrete value set on there.
    '''
    _name = ''
    # Over write "_name" string in inherited classes.
    
    @property
    def name(self):
        return self._name