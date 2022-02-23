# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 2020
@author: Dr Hui Zhi
"""

import os

def mkFolder(config):
    if not os.path.exists(config['OFP']):
        os.makedirs(config['OFP'])
    logF = '{}{}'.format(config['OFP'], '/logFile.txt')
    if not os.path.exists(logF):
        with open(logF, 'w'):
            pass
    