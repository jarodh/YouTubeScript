#!/usr/bin/env python

import os
from os import listdir
from os import path
from os.path import isfile, join
from pathlib import Path

import sys
import subprocess

def getNewestFile(filepath, filtype):
    mypath = str(Path(filepath))
    newestFile = ""
    if path.exists(mypath):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(filtype)]

        defaultTime = path.getmtime(join(mypath, onlyfiles[0]))
        newestFile = onlyfiles[0]
        for file in onlyfiles:
            if path.getmtime(join(mypath, file)) > defaultTime:
                newestFile = file
                defaultTime = path.getmtime(join(mypath, file))

    retval = "";
    if newestFile != "":
        retval = join(mypath, newestFile)
        
    return retval


def populateArguments():
    fileType = sys.argv[2]
    filePath = getNewestFile(sys.argv[1], fileType)
    name = Path(filePath).name.replace(fileType, "").replace(".", "")
    dirpath = os.path.join(str(os.getcwd()), "upload_video.py")

    variables = {'directoryPath':dirpath,'filePath':filePath,'name':name}

    command = "python3 {directoryPath} --file=\"{filePath}\" --title=\"{name}\" --category=\"22\" --privacyStatus=\"public\" --description=\"{name}\"".format(**variables)
    print("Command: ",command)    
    subprocess.call(command, shell=True)

populateArguments()
