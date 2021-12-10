import time
import os
import shutil

sec = time.time()
pathexist = os.path.exists("C:\Users\acer pc\Documents\Project of Python\Pro-99")
print(pathexist)
if(pathexist):
    list = os.walk(pathexist)
    ctime = os.stat(pathexist).st_ctime
    if(sec>ctime):
        os.remove(pathexist)
        shutil.rmtree(pathexist)
else:
    print("Not found")

