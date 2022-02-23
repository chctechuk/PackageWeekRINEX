#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compress files
Created on Tue Sep  7 2021
@author: Dr Hui Zhi
"""

import INI
import os
import gzip

def cGZIP(config, filePath):
    # file into .gz
    newPath = filePath + '.gz'
    try:
        with open(filePath, 'rb') as f:
            with gzip.open(newPath, 'wb') as g:
                g.write(f.read())
        os.remove(filePath)
        st1 = '{} {}'.format(filePath, 'compress successfully.')
        INI.logRecord(config, st1)
    except Exception:
        st2 = '{} {} {}'.format('Error: ', filePath, 'compress failed.')
        INI.logRecord(config, st2)
    