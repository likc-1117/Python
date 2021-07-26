#coding:utf-8

import os,sys
import datetime,time

starttime=datetime.datetime.now()
time.sleep(5)
print(type((datetime.datetime.now()-starttime).seconds))