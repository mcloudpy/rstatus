# -*- coding: utf-8 -*-
"""
 Copyright (C) 2014 onwards University of Deusto
  
 All rights reserved.
 
 This software is licensed as described in the file COPYING, which
 you should have received as part of this distribution.
 
 This software consists of contributions made by many individuals, 
 listed below:
 
 @author: Aitor Gómez Goiri <aitor.gomez@deusto.es>
"""

import psutil
# print psutil.cpu_percent(interval=1, percpu=True) # example


class StatusGetter(object):
    def __init__(self, method_names, params_for_calls=None, select_for_calls=None):
        # params = { 'interval':1, 'percpu': True }
        # self.call = [ ["cpu_percent", params] ]
        assert params_for_calls is None or len(params_for_calls) == len(method_names), \
            "There must be as many params as method names (None values are allowed!)"
        assert select_for_calls is None or len(select_for_calls) == len(method_names), \
            "There must be as many selects as method names (None values are allowed!)"

        self.call = []
        i = 0
        for method_name in method_names:
            params = params_for_calls[i] if params_for_calls else {}
            sel = select_for_calls[i] if select_for_calls else {}
            self.call.append([method_name, params, sel])
            i += 1

    def get_measure(self):
        for method_name, params, sel in self.call:
            method_to_call = getattr(psutil, method_name)
            name = method_name
            ret = method_to_call(**params)
            if sel:
                name = name + "." + sel
                ret = getattr(ret, sel)  # select an attribute from the return
            yield name, ret


class FakeStatusGetter(object):
    def get_measure(self):
        yield 'fake', True