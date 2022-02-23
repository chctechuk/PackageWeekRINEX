# -*- coding: utf-8 -*-
"""
BKG
Created on Mon Aug 17 2020
@author: Dr Hui Zhi
"""

import os
import Email
import ftplib
from datetime import datetime
import weakref

class FTPRun():
    def __init__(self, config, IP, user, pw, remotePath):
        """
        Parameters
        ----------
        IP : str
            host address.
        user : str
            user name.
        pw : str
            password.
        remotePath : str
            ftp subfolder path.
        tarFile : str
            target file name.
        """
        self.config     = config
        self.IP         = IP
        self.user       = user
        self.pw         = pw
        self.remotePath = remotePath
        self.logFile    = '{}{}'.format(config['OFP'], '/logFile.txt')

    def ftp_connect(self):
        d   = datetime
        now = weakref.ref(d)().now().strftime('%Y-%m-%d %H:%M:%S')
        del d
        try:
            f   = ftplib
            ftp = weakref.ref(f)().FTP()
            del f
            ftp.set_debuglevel(0)
            ftp.connect(self.IP, 21)
            ftp.login(self.user, self.pw)
            print('{}\t{} {}'.format(now, self.IP, 'login successfully.'))
        except Exception:
            st = '{}\t{} {} {}'.format('Warning:', now, self.IP, 
                                       'login failed.\n')
            print(st)
            with open(self.logFile, 'a') as f:
                f.write(st)
        return ftp
        
    def download(self, locFolderPath):
        d   = datetime
        now = weakref.ref(d)().now().strftime('%Y-%m-%d %H:%M:%S')
        del d
        try:
            ftp = self.ftp_connect()
            ftp.cwd(self.remotePath)
            buf_size = 1024
            remoteFile = ftp.nlst()
            for f in remoteFile:
                fp    ='{}{}{}'.format(locFolderPath, '/', f) 
                lfile = open(fp, 'wb')
                ftp.retrbinary(
                    '{} {}{}{}'.format('RETR', self.remotePath, '/', f),                    
                    lfile.write, buf_size)
                lfile.close()
            ftp.quit()
            st1 = '{}\t{} {} {}'.format(
                now, 'Download day', os.path.split(locFolderPath[:-1])[1], 
                'task is done.\n')
            print(st1)
            with open(self.logFile, 'a') as f:
                f.write(st1)
        except Exception:
            st = '{}\t{} {} {}'.format(
                now, 'Download day', os.path.split(locFolderPath[:-1])[1], 
                'task is failed!\n')
            print(st)
            with open(self.logFile, 'a') as f:
                f.write(st)
            Email.emailAlarm(self.config).sendEmail()
            