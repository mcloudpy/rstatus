# -*- coding: utf-8 -*-
'''
 Copyright (C) 2014 onwards University of Deusto
  
 All rights reserved.
 
 This software is licensed as described in the file COPYING, which
 you should have received as part of this distribution.
 
 This software consists of contributions made by many individuals, 
 listed below:
 
 @author: Aitor Gómez Goiri <aitor.gomez@deusto.es>
'''

import psutil
# print psutil.cpu_percent(interval=1, percpu=True) # example


class StatusGetter(object):
  
  def __init__(self):
    params = { 'interval':1, 'percpu': True }
    self.call = [ ["cpu_percent", params] ]
  
  def get_pair(self):
    for method_name, params in self.call:
      #method_name = self.call[0][0]
      #params = self.call[0][1]
      methodToCall = getattr(psutil, method_name)
      yield method_name, methodToCall( **params )