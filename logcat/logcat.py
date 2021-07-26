#coding:utf-8
import os
import time
import re
import multiprocessing
from logcat.log import *
from logcat.resultxml import *
from logcat.resultparam import *




def getlog():
    os.popen('adb logcat -b events -v time>>.\\logcat.txt')

def search(cycletimes=0,delay=1):
    resultlist=[]
    failtime=[]
    msg=''
    for i in range(int(cycletimes)):
            time.sleep(int(delay))
            getfile=open('.\\logcat.txt','r')
            content=getfile.read()
            getfile.close()
            key=r'\d\d\-\d\d+\s+\d\d\:\d\d\:\d\d\.\d+\s+I\/\w+\(\s+\d+\)\:\s+\[\d+\,false\]'
            #key=r'\d+\-\d+\s+(?:\d+\:){2}\d+\.\d+(?:\s+\d{5}){2}\s+D\s+\w+_\w+\s+\:\s+\w+_(?:\w+\s+){3}touch_up'
            reCompile=re.compile(key,re.S|re.M|re.X)
            rresult=reCompile.findall(content)
            if rresult:
                resultlist.append(len(rresult))
                #print len(rresult)
                #print resultlist
                #return (len(rresult))
                if int(len(rresult))!=int(resultlist[i-1]):
                    failtime.append(rresult[len(rresult)-1]+'\n')
    if len(resultlist)>0:
        for ft in failtime:
            msg+=str(ft)
        log.logger(msg)
        #print '解锁失败的时间为：\n'+msg
        failtimes=int(resultlist[len(resultlist)-1])-int(resultlist[0])
        log.logger('解锁失败次数为:'+str(failtimes))
        param.fail=failtimes
        #print '解锁总次数为:'+str(cycletimes)+',解锁失败次数为:'+str(failtimes)
    else:
        log.logger('解锁失败次数为:0')
        #print '解锁总次数为:'+str(cycletimes)+',解锁失败次数为:0'
    #inputresult(start,stop,total,failtimes)
    sys.exit(0)







if __name__=='__main__':
    print('指纹功能检测程序，是否开始检测(Y/N):')
    if input()=='Y':
        print('请输入需要解锁的次数:')
        cycle=input()
        print('请输入间隔多少时间获取一次结果：')
        delay=input()
        #print '请确认等待多少时间开始获取解锁结果：'
        #delayyime=input()
        '''if os.path.exists('.\\logcat.txt') is not True:
            result='fail,there is not have a txt'
            print result
        else:
            if os.path.getsize('.\\logcat.txt')>=10000000:
                os.rename('.\\logcat.txt','.\\logcat.txt.1')'''
        t1=multiprocessing.Process(target=getlog)
        t2=multiprocessing.Process(target=search,args=(cycle,delay,))
        t1.start()
        t2.start()
    else:
        print('程序退出')
