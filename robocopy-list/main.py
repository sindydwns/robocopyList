import config
import time

import os
ERR_SRC_NOT_EXSIST = 1

def copy(src, des):
    if not os.path.isfile(src):
        return ERR_SRC_NOT_EXSIST
    srcPath = os.path.dirname(src)
    desPath = os.path.dirname(des)
    srcName = os.path.basename(src)
    desName = os.path.basename(des)
    cmd = f"robocopy {srcPath} {desPath} {srcName} /NDL >> log.txt"
    os.system(f"cmd /c {cmd}")
    os.rename(desPath + "/" + srcName, desPath + "/" + desName)
    mtime = time.ctime(os.path.getmtime(src))
    return mtime

def pathFilter(path):
    src = path[0].replace(r"\src\main\webapp", "");
    des = path[1].replace(r"\src\main\webapp", "");
    src = src.replace(r"\src\main\java", r"\WEB-INF\classes")
    des = des.replace(r"\src\main\java", r"\WEB-INF\classes")
    src = src.replace(r"\src\main\resources", r"\WEB-INF\classes")
    des = des.replace(r"\src\main\resources", r"\WEB-INF\classes")
    if os.path.splitext(src)[1] == ".java":
        src = os.path.splitext(src)[0] + ".class"
    if os.path.splitext(des)[1] == ".java":
        des = os.path.splitext(des)[0] + ".class"
    return (src, des, path[2])

items = config.getFileList()
items = [pathFilter(x) for x in items]
for item in items:
    result = copy(item[0], item[1])
    if result == ERR_SRC_NOT_EXSIST:
        print(f"NO FILE : {item[0]}")
    else:
        print(f"OKCOPY [{result}] {item[2]}")
input("")
