#coding:utf-8


import re
import os,sys
from random import randint


fileaddr=sys.path[0]
def ratenum():
    fileopen=open('D:\\HWP10-30si4500-5000ΩRectangle.txt','r')
    content=fileopen.read()
    key=r'is\s+\d+'
    recomplie=re.compile(key,re.S|re.M|re.X)
    result=recomplie.findall(content)
    key2=r'\d+'
    r=re.compile(key2,re.S|re.M|re.X)
    intresult=r.findall(str(result))
    with open('D:\\resultresultresult.txt','w') as wresult:
        for num in intresult:
            wresult.write(num+'\n')
ratenum()

with open('D:\\HWP10-30si4500-5000ΩRectangle.txt','r') as readfile:
    content=readfile.readlines()
    print(len(content))