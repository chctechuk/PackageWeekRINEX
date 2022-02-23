# -*- coding: utf-8 -*-
"""
Package LICC Receiver RINEX Data for Week
Created on Wed Feb 23 2022
@author: Dr Hui Zhi
"""

import sys
sys.dont_write_bytecode = True
import os
import INI
import FTP
import Core
import time
import convert
from datetime import datetime

def main():
    flag = 1
    while flag:
        today = datetime.now().weekday()
        if today==config['DOP']:
            if int(time.strftime('%H%M')) > int('0300'):
                for i in range(config['NOW']*7):
                    tarYear  = '%04d'%convert.convert(i).outPreDaybyDate()[0]
                    tarDay   = '%03d'%convert.convert(i).outPreDaybyDate()[1]
                    savePath = '{}{}{}{}{}{}'.format(
                        config['OFP'], '/', tarYear, '/', tarDay, '/')
                    if not os.path.exists(savePath):
                        os.makedirs(savePath)
                        FTP.FTPRun(
                            config, INI.settings.IP, INI.settings.User,
                            INI.settings.PW, INI.settings().RP(i)
                            ).download(savePath)
                        fPath = INI.readFolder(savePath)[0]
                        for x in fPath:
                            if x:
                                Core.cGZIP(config, x)
                    else:
                        time.sleep(3600)
            else:
                time.sleep(3600)
        else:
            time.sleep(int(86400/4))
# %%
if __name__ == '__main__':
    INI.logo()
    INI.validity()
    config = INI.readConfig('config_pwr.ini')
    INI.mkFolder(config)
    main()
    