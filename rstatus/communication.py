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

import re


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
        for item in self._status_getter.get_measure():
            # print pair # debug
            name = "%s/%s" % (self._machine, item[0])
            value = item[1]
            print name, value
            # self._conn.set(name, value)
            self._conn.lpush(name, value)  # prepend last measured value
            self._conn.ltrim(name, 0, self._limit - 1)  # max last N values (first elements in the list) are stored


class StatusReceiver(RedisClient):
    def __init__(self, redis_connection, status_keys):
        """
        :param redis_connection:
        :param status_keys: Features which will be taken into account.
        :return:
        """
        super(StatusReceiver, self).__init__(redis_connection)
        self._status_keys = status_keys
        self._regex = re.compile("/", re.VERBOSE)

    def _put_in_dict(self, dictio, machine_id, feature_name, value):
        if machine_id not in dictio:
            dictio[machine_id] = {}
        dictio[machine_id][feature_name] = value

    def _get_whatever_measures(self, method_to_call, machine_ids=None):
        """
        :param machine_ids:
        :param number_measures: If None all the measures will be returned.
        :param method_to_call: Method from this class to be called to obtain the desired value from Redis DB.
        :return:
        """
        measures = {}
        for status_key in self._status_keys:
            if machine_ids is None:
                possible_features = self._conn.keys("*/%s" % status_key)
                for feature in possible_features:
                    values = method_to_call(feature)
                    machine_id, feature_name = self._regex.split(feature)
                    self._put_in_dict(measures, machine_id, feature_name, values)
            else:
                for machine_id in machine_ids:
                    values = method_to_call("%s/%s" % (machine_id, status_key))  # get last value
                    self._put_in_dict(measures, machine_id, status_key, values)
        return measures

    def get_last_measures(self, machine_ids=None):
        return self._get_whatever_measures(self._conn.lpop, machine_ids)

    def _get_all_measures_by_feature(self, feature):
        l = self._conn.llen(feature)
        return self._conn.lrange(feature, 0, l)

    def get_all_measures(self, machine_ids=None):
        """
        :param machine_ids:
        :param number_measures: If None all the measures will be returned.
        :return:
        """
        return self._get_whatever_measures(self._get_all_measures_by_feature, machine_ids)