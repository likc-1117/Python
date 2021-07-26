#coding:utf-8


import os,sys

def checkadb():
    adbreturn=os.popen('adb devices')
    if adbreturn.read().count('device')>1:
        os.popen('adb push ')
    print('False')
    return 'False'


print(os.path)
print(os.getcwd())