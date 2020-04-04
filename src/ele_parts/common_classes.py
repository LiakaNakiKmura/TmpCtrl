# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:21:44 2020

@author: LiNaK
"""

# Standard module

# 3rd party's module

# Original module  
from context import src  # path setting
from src.interface.intfc_com import (ResistFuncMaker, ResistTempFunc)

class ResistFuncMaker_Com(ResistFuncMaker):
    _para_cls_list =()
    _func_cls = ResistTempFunc
    
    def get_kind_list(self):
        self._make_list()
        return self._name_list.keys()
        
    def get_resist(self, name):
        return self._func_cls(self._name_list[name])
    
    def _make_list(self):
        self._name_list = {}
        for Para in self._para_cls_list:
            p = Para()
            self._name_list[p.name] = Para
