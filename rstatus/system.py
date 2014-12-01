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
    def __init__(self, method_names, params_for_calls=None):
        # params = { 'interval':1, 'percpu': True }
        #self.call = [ ["cpu_percent", params] ]
        self.call = []

        if params_for_calls is None:
            for method_name in method_names:
                self.call.append([method_name, {}])
        else:
            for method_name, params in zip(method_names, params_for_calls):
                self.call.append([method_name, params])

    def get_measure(self):
        for method_name, params in self.call:
            method_to_call = getattr(psutil, method_name)
            yield method_name, method_to_call(**params)


class FakeStatusGetter(object):
    def get_measure(self):
        yield 'fake', True