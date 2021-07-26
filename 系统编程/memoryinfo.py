#coding:utf-8

from time import sleep
import re,os,string,psutil
from datetime import datetime
from random import randint

def countProcessMemoey():
    taklistresult=''
    pattern = re.compile(r'([^\s]+)\s+(\d+)\s.*\s([^\s]+\sK)')
    cmd = 'tasklist '
    result = os.popen(cmd).read()
    resultList = result.split("\n")
    for srcLine in resultList:
        if 'Mobot' not in str(srcLine) :
            continue
        srcLine = "".join(srcLine.split('\n'))
        m = pattern.search(srcLine)
        if m == None:
            continue
        #由于是查看python进程所占内存，因此通过pid将本程序过滤掉
        if str(os.getpid()) == m.group(2):
            continue
        ori_mem = m.group(3).replace(',','')
        ori_mem = ori_mem.replace(' K','')
        ori_mem = ori_mem.replace(r'\sK','')
        memEach = int(ori_mem)
        taklistresult+=('ProcessName:  '+m.group(1)+'  PID: '+m.group(2)+'  Memory '+m.group(3)+'\n')
    return taklistresult

def cpumemory():
    outputlog('CPU :'+str(psutil.cpu_percent(interval=1)))
    outputlog('Total Memory :'+str(psutil.swap_memory()))

def outputlog(msg):
    if os.path.exists('D:\\resource.txt') is True:
        if os.path.getsize('D:\\resource.txt')>=100000000:
            os.rename('D:\\resource.txt','D:\\resource.txt.'+str(randint(1000000)))
    output=open('D:\\resource.txt','a')
    output.write(str(msg)+'\n')
    output.close()
    print(msg)





print(str(os.popen('taskkill /f /t /im python.exe').read()).encode(encoding='utf-8'))