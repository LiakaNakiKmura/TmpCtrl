# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:04:42 2017
Utilitys for unit testing 

@author: sasamura
"""
# Original module  
from context import src # path setting

import types

def startstop_msg(func, comment=""):
    # This is the decorator to print that a wrapped function is called and 
    # finished. Unittest function is decorated this function to check the
    # timing for debugging.
    def wrap(*args, **kwds):
        def prt_msg(msg):
            # print msg with line and function name.
            print ('-'*3 + comment+ func.__name__ + ' ' +  msg + '-'*3)
        prt_msg('is started')
        func(*args, **kwds)
        prt_msg('is completed')
    return wrap

def cls_startstop_msg(class_):
    '''
    The decorator decrating unittest subclass.
    When unittest is excuted start, stop message is added to test method. 
    '''
    class class_w(class_):
        for method in dir(class_):
            attr = getattr(class_, method)
            if method[:4] == 'test' and type(attr) is types.FunctionType :
                # if method name is starte with 'test', add message.
                new_method = startstop_msg(attr, class_.__name__+'.')
                setattr(class_, method, new_method)
    return class_w


class TestForMethodExist():
    '''
    Check that class has specified method for especially abstract class.
    _class_method_pairs is set as ((class1, mrthod1),(class2, method2)...)
    _class_attr_pairs is set as ((class1, attribute1),(class2, attribute2)...)
    '''

    _class_method_pairs =(())
    _class_attr_pairs = (())

    def test_class_method_pairs(self):
        judge_func =lambda cl,m: self.assertTrue(callable(getattr(cl,m)))
        self.check_sth_in_cls(self._class_method_pairs, judge_func)

    def test_class_attr_pairs(self):
        judge_func =lambda cl,a: self.assertTrue(hasattr(cl,a))
        self.check_sth_in_cls(self._class_attr_pairs, judge_func)

    def check_sth_in_cls(self, cls_sth_pairs, judge_func):
        '''
        Both of expression can be adapted for cls_sth_pairs:
            1.((class1, (sth1, sth2)),(class2, (sth1,sth2)))
            2.((class1, sth1),(class2, sth2))
        'judge_func' means judgment function
        '''
        for cl, sth in cls_sth_pairs:
            if isinstance(sth, list) or isinstance(sth, tuple):
                for s in sth:
                    judge_func(cl, s)
            else:
                judge_func(cl, sth)


if __name__ == '__main__':
    @startstop_msg
    def func():
        print('a')
        
    func()
    # print like follwing
    # ----------func is started----------
    # a
    # ----------func ie completed----------
    
    @cls_startstop_msg
    class cls():
        test_value = 4
        def A(self):
            print('A')
            
        def test_B(self):
            print('B')
            
    c = cls()
    # print(c.__dir__())
    c.A()
    # A
    c.test_B()
    #  ----------test_B is started----------
    # B
    # ----------test_B ie completed----------