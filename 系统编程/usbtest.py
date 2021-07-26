#coding:utf-8

import os,sys
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime

addr=sys.path[0]
def usb():
    result=os.popen('adb shell mkdir /data/local/tmp/0aaaaaaa')
    logs('mkdir 0aaaaaaa result is '+str(result.read()))
    cord='adb push D:\\USB数据交互资源\\video.mp4'+' '+'/data/local/tmp/0aaaaaaa'
    cords = 'adb push D:\\USB数据交互资源\\videos.mp4' + ' ' + '/data/local/tmp/0aaaaaaa'
    cordmusic = 'adb push D:\\USB数据交互资源\\ruizhi.mp3' + ' ' + '/data/local/tmp/0aaaaaaa'
    adbresult=os.popen(cord)
    rr=adbresult.read()
    logs('push video result is '+str(rr))
    adbresults = os.popen(cords)
    rrs = adbresults.read()
    logs('push video result is ' + str(rrs))
    adbresultm = os.popen(cordmusic)
    rrm = adbresultm.read()
    logs('push music result is ' + str(rrm))
    installtaobao=os.popen('adb install D:\\USB数据交互资源\\taobao.apk')
    installreader=os.popen('adb install D:\\USB数据交互资源\\iReader.apk')
    installuc = os.popen('adb install D:\\USB数据交互资源\\UCMobile.apk')
    logs('install TaoBao result is '+str(installreader.read()))
    logs('install IReader result is '+str(installtaobao.read()))
    logs('install UC result is '+str(installuc.read()))
    #os.popen('adb install weixin.apk')
    rmvidwo=os.popen('adb shell rm -r /data/local/tmp/0aaaaaaa/video.mp4')
    logs('rm vidwo result is '+str(rmvidwo.read()))
    sleep(5)
    rmvideos = os.popen('adb shell rm -r /data/local/tmp/0aaaaaaa/videos.mp4')
    logs('rm videos result is ' + str(rmvideos.read()))
    sleep(5)
    rmmusic = os.popen('adb shell rm -r /data/local/tmp/0aaaaaaa/ruizhi.mp3')
    logs('rm videos result is ' + str(rmmusic.read()))
    sleep(5)
    rmdirresult=os.popen('adb shell rmdir /data/local/tmp/0aaaaaaa')
    logs('rmdir 0aaaaaa result is '+str(rmdirresult.read()))
    uninstalltaobao=os.popen('adb uninstall com.taobao.taobao')
    uninstallread=os.popen('adb uninstall com.chaozh.iReaderFree')
    uninstalluc=os.popen('adb uninstall com.UCMobile')
    logs('uninstall TaoBao result is '+str(uninstalltaobao.read()))
    logs('uninstall IReader result is '+str(uninstallread.read()))
    logs('uninstall UC result is '+str(uninstalluc.read()))

def logs(msg):
    output=open('D:\\USBTestReult\\log.txt','a')
    output.write(str(datetime.now())+'    '+str(msg)+'\n')
    print(str(datetime.now())+'    '+str(msg))
    output.close()

usb()