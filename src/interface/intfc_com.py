   
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
    @abc.abstractmethod
    def get_func(self):
        pass

class ResistParameter(metaclass = abc.ABCMeta):
    _name = ''
    # Over write "_name" string in inherited classes.
    
    @property
    def name(self):
        return self._name