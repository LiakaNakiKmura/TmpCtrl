# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:48:15 2020

@author: LiNaK
"""

# Standard module

# 3rd party's module
import numpy as np

# Original module  

class TempRange():
    
    def set_range(self, start, stop, step):
        self._start = start
        self._stop = stop
        self._step = step
    
    def get_list(self):
        return np.arange(self._start, self._stop, self._step)
