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

import argparse
import redis
from communication import StatusReceiver


def main():
    parser = argparse.ArgumentParser( description='Write system status in Redis database.' )
    parser.add_argument('-host', default='localhost', dest='host', help='Redis host.')
    parser.add_argument('-port', default=6379, dest='port', type=int, help='Redis port.')
    parser.add_argument('-db', default=0, dest='db_number', help='Redis DB number.')
    args = parser.parse_args()
    
    r = redis.StrictRedis(host=args.host, port=args.port, db=args.db_number)
    keys = ["cpu_percent"]
    sr = StatusReceiver(r, "testvm", keys)
    print sr.get_last_measures()



if __name__ == '__main__':
    main()