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

import yaml
import argparse


class ConfigReader(object):
    def __init__(self, filename):
        self.config = self._parse(filename)

    def _parse(self, filename):
        with open(filename, 'r') as fyml:
            return yaml.load(fyml.read())

    def get_methods(self):
        return [c['method'] for c in self.config]

    def get_params(self):
        ret = []
        for c in self.config:
            param_dict = {}
            if 'params' in c:
                for param in c['params']:
                    # param is a dictionary with a unique key and value
                    k = param.iterkeys().next()
                    v = param.itervalues().next()
                    param_dict[k] = v
            ret.append(param_dict)
        return ret

    def get_select(self):
        ret = []
        for c in self.config:
            if 'select' in c: # not a list!
                ret.append(c['select'])
            else:
                ret.append('')
        return ret

    def debug(self):
        for m, params, sel in zip(self.get_methods(), self.get_params(), self.get_select()):
            s = "." + sel if sel else ""
            printable_params = ""
            for param_key in params:
                printable_params += ", %s=%s" % (param_key, params[param_key])
            print "psutil.%s(%s)%s" % (m, printable_params[2:], s)  # without first ", "


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read config file and show its properties.')
    parser.add_argument('-config', default="../config.yml", dest='config',
                        help='Configuration file with the psutil methods to be called.')
    args = parser.parse_args()

    cr = ConfigReader(args.config)
    cr.debug()