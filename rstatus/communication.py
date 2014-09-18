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

class RedisClient(object):
  
  def __init__(self, redis_connection):
    self._conn = redis_connection


class StatusSender(RedisClient):
  
  def __init__(self, redis_connection, machine_id, status_getter, slots_limit=10):
    super(StatusSender, self).__init__(redis_connection)
    self._machine = machine_id
    self._limit = slots_limit
    self._status_getter = status_getter
  
  def store(self):
    for item in self._status_getter.get_pair():
      # print pair # debug
      name = item[0]
      value = item[1]
      #self._conn.set( name, value )
      self._conn.lpush( name, value ) # prepend last measured value
      self._conn.ltrim( name, 0, self._limit-1 ) # max last N values (first elements in the list) are stored


class StatusReceiver(RedisClient):
  
  def __init__(self, redis_connection, machine_id, status_keys):
    super(StatusReceiver, self).__init__(redis_connection)
    self._machine = machine_id
    self._status_keys = status_keys
 
  def get_last_measures(self):
    measures = {}
    for key in self._status_keys:
      measures[key] = self._conn.lpop( key ) # get last value
    return measures