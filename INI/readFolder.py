#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read Folder
Created on Wed Jul 21 2021
@author: Dr Hui Zhi
"""

import os

def readFolder(path):
    """
    Parameters
    ----------
    config : dict

    Returns
    -------
    filepath : list
    filedir : list
    filename : list
    filename_m : list
    folderpath : list
    """
    filepath   = []      # file path
    filedir    = []      # folder path - file located
    filename   = []      # file name with extension
    filename_m = []      # file name without externsion
    folderpath = []      # subfolder path
    for (root, dirs, files) in os.walk(path, topdown=False):
        for name in files:
            filepath.append(os.path.join(root, name))
            filedir.append(os.path.join(root))
            filename.append(name)
            filename_m.append(os.path.splitext(name)[0])
        for folder in dirs:
            folderpath.append(os.path.join(root, folder))
    return filepath, filedir, filename, filename_m, folderpath
