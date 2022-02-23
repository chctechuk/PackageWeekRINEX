# -*- coding: utf-8 -*-
"""
write in log file
Created on Wed Sep  8 2021
@author: Dr Hui Zhi
"""

from datetime import datetime

def logRecord(config, words):
    logFile = '{}{}'.format(config['OFP'], '/logFile.txt')
    now     = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st1     = '{}\t{}\n'.format(now, words)
    print(st1)
    with open(logFile, 'a') as f:
        f.write(st1)
    