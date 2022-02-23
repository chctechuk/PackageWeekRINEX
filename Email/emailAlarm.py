#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 2020
@author: Dr Hui Zhi
"""

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class emailAlarm():
    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            read ini variable.
        logFile : str
            logfile name.
        """
        self.config  = config
        self.logFile = '{}{}'.format(config['OFP'], '/logFile.txt')

    def sendEmail(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sender        = 'info@ichcgnss.co.uk'
        # sendername    = 'ichcgnss'
        username_smtp = 'AKIA3MFKQB5OM6RSBTJW'
        password_smtp = 'BI43KX+qCg0w7NXb1LrK2aCHHDtzzUgjTKZiG2W6K9cr'
        host = 'email-smtp.eu-west-2.amazonaws.com'
        port = 587
        subject = 'Package Week LICC Recevier RNIEX Files Warning'
        for x in self.config['EA']:
            if x:
                cmd = '{}\t{} {}\n'.format(
                    now, 'WARNING: Errors for PackageWeekRINEX_V1.0.exe',
                    'Please check on OCE cloud.')
                with open(self.logFile, 'a') as f:
                    f.write(cmd)
                msg            = MIMEText(cmd, 'plain', 'utf-8')
                msg['From']    = sender
                msg['To']      = x
                msg['Subject'] = subject
                try:
                    smtp_server = smtplib.SMTP(host, port, timeout=300)
                    # .SMTP change to .SMTP_SSL(when open TLS)
                    smtp_server.ehlo()
                    smtp_server.starttls() #.ehlo & .starttls are needed before .login
                    smtp_server.login(username_smtp, password_smtp)
                    smtp_server.sendmail(
                        sender, x, msg.as_string())
                    smtp_server.quit()
                    st1 = '{}\t{} {} {}\n'.format(
                        now, 'PackageWeekRINEX_V1.0 alarm email sent to', x,
                        'successfully.')
                    with open(self.logFile, 'a') as f:
                        f.write(st1)
                    print(st1)
                except smtplib.SMTPException:
                    st2 = '{}\t{}\n'.format(
                        now, 'Error: PackageWeekRINEX_V1.0 alarm email sent failed.')
                    with open(self.logFile, 'a') as f:
                        f.write(st2)
                    print(st2)
        
                        