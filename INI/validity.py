# -*- coding: utf-8 -*-
"""
Validity
Created on Wed Aug  5 2020
@author: Dr Hui Zhi
"""

import os
import time
import sys
from datetime import datetime

def validity():
    start = '2021-01-01 00:00:00'
    end   = '2022-12-31 23:59:59'
    now   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timeArray_now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
    timeStamp_now = int(time.mktime(timeArray_now)) 
    timeArray_s = time.strptime(start, "%Y-%m-%d %H:%M:%S")
    timeArray_e = time.strptime(end, "%Y-%m-%d %H:%M:%S")
    timeStamp_s = int(time.mktime(timeArray_s))
    timeStamp_e = int(time.mktime(timeArray_e))
    if timeStamp_now in range(timeStamp_s, timeStamp_e):
        pass
    else:
        print('This software is expired.')
        os.system('pause')
        sys.exit()
        