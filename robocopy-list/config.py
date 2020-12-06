import os

CONFIG_FILE = "config.txt"
FILE_LIST = "filelist"
SRC_PATH = "srcPath"
DES_PATH = "desPath"

def getSettings():
    file = open(CONFIG_FILE)
    lines = file.read().splitlines()
    lines = [x for x in lines if str(x) != "nan"]
    return {s.split("=")[0]:s.split("=")[1] for s in lines}

def toPath(str):
    return str.replace("\\", "/")

def getSrcPath():
    return toPath(getSettings()[SRC_PATH])

def getDesPath():
    return toPath(getSettings()[DES_PATH])

def getFileList():
    fileListFileName = getSettings()[FILE_LIST]
    srcPath = getSettings()[SRC_PATH]
    desPath = getSettings()[DES_PATH]
    file = open(fileListFileName)
    lines = file.read().splitlines()
    lines = [x for x in lines if str(x) != "nan"]
    srcFiles = [os.path.join(srcPath, x) for x in lines]
    srcFiles = [os.path.normpath(x) for x in srcFiles]
    desFiles = [os.path.join(desPath, x) for x in lines]
    desFiles = [os.path.normpath(x) for x in desFiles]
    files = list(zip(srcFiles, desFiles))
    return files
