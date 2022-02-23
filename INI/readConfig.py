# -*- coding: utf-8 -*-
"""
Read Config File
Created on Wed Sep 29 2021
@author: Dr Hui Zhi
"""

import configparser

def readConfig(configFile='config_pwr.ini'):
    """
    Parameters
    ----------
    configFile : file
        configFile is config file name with extension.

    Returns
    -------
    config : dict
    """
    config = {}
    cfg    = configparser.ConfigParser(
        inline_comment_prefixes='#', allow_no_value=True)
    cfg.read(configFile)
    
    config['OFP'] = cfg.get('Input Configuration', 'OutputFolderPath')

    config['DOP'] = cfg.getint('Process Configuration', 'DayOfPackage')
    config['NOW'] = cfg.getint('Process Configuration', 'NumOfWeeks')

    config['EA']  = [
        x.strip() for x in cfg.get(
            'Output Configuration', 'EmailAlarm').split(',')]
    
    return config
