#!/usr/bin/env python
"""
 Copyright (C) 2014 onwards University of Deusto
  
 All rights reserved.
 
 This software is licensed as described in the file COPYING, which
 you should have received as part of this distribution.
 
 This software consists of contributions made by many individuals, 
 listed below:
 
 @author: Aitor Gómez Goiri <aitor.gomez@deusto.es>
"""

from distutils.core import setup

setup(name='rstatus',
      version='0.1',
      description='Python library to periodically write and read the system status in a Redis DB',
      author='Aitor Gómez-Goiri',
      author_email='aitor.gomez@deusto.es',
      url='https://github.com/mcloudpy/rstatus',
      packages=['rstatus'],
      install_requires=[
          'psutil==2.1.1',
          'redis==2.10.3',
      ],
      entry_points={
          'console_scripts': [
              'rproducer = rstatus.producer:main',
              'rconsumer = rstatus.consumer:main',
          ],
      },
)