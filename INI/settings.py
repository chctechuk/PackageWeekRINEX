# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 2020
@author: Dr Hui Zhi
"""

import convert

class settings():
    IP   = '18.135.43.119'
    User = 'ICHC'
    PW   = 'Gnss12345/'
    def __init__(self):
        pass
                
    def RP(self, preDays):
        # remote path
        return '{}{}{}{}{}'.format(
            '/LICCReceiverR3.02/logs/logs_1/rinex/', 
            '%04d'%convert.convert(preDays).outPreDaybyDate()[0], '/',
            '%03d'%convert.convert(preDays).outPreDaybyDate()[1], 
            '/LICC00GBR/')
    