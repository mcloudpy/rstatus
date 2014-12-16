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

import argparse
from redis import StrictRedis
from communication import StatusReceiver


def get_last_measures(host, port, db_number):
    r = StrictRedis(host=host, port=port, db=db_number)
    keys = ["cpu_percent", "swap_memory", "fake"]
    sr = StatusReceiver(r, keys)
    return sr.get_last_measures()


def show_measures(measures):
    for k, v in measures.iteritems():
        print "Hostname: %s" % k
        for kv in v:
            print "\t%s:" % kv
            print "\t\t%s" % v[kv]


def main():
    parser = argparse.ArgumentParser(description='Write system status in Redis database.')
    parser.add_argument('-host', default='localhost', dest='host', help='Redis host.')
    parser.add_argument('-port', default=6379, dest='port', type=int, help='Redis port.')
    parser.add_argument('-db', default=0, dest='db_number', help='Redis DB number.')
    args = parser.parse_args()
    m = get_last_measures(args.host, args.port, args.db_number)
    show_measures(m)


if __name__ == '__main__':
    main()