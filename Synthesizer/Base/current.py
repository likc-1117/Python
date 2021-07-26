# -*- coding: utf-8 -*-
'''
Created on 2019年9月18日

@author: likecan
'''
import socket, os, time, sys
from Synthesizer.Base.log import *


class current:
    path = os.path.split(os.path.realpath(__file__))[0] + '\\Config\\'

    @staticmethod
    def sendmsg(msg):
        data = 'fail'
        # localip=socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # s.settimeout(10)
            s.connect(('127.0.0.1', 8082))
            s.sendall(msg.encode(encoding='utf-8'))
            data = s.recv(1024)
            log.logger(data.decode())
        except socket.timeout:
            print('timeout')
        s.close()
        return data.decode()

    @staticmethod
    def externaldll(dllname, classname, methodname, *param):
        # print 'current.externaldll '+str(dllname)+';classname is '+str(classname)+';methodname is '+str(methodname)
        msg = 'External ' + str(dllname) + ' ' + str(classname) + ' ' + str(methodname) + ' '
        for i in range(len(param)):
            msg += param[i] + ' '
        data = current.sendmsg(msg[:-1])
        return data

    # 开始采集某一个过程的电流
    @staticmethod
    def startgetcurrent():
        log.logger('start power dissipation to get current value for single scene ')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'StartGetCurrent')
        log.logger('start result is ' + str(data))

    # 停止安捷伦采集电流
    @staticmethod
    def closegetcurrent():
        log.logger('stop power dissipation to get current value for single scene ')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'CloseGetCurrent')
        log.logger('stop result is ' + str(data))

    # 获取最大电流值
    @staticmethod
    def getmaxcurrentvalue():
        log.logger('get max current value for single scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetMaxCurrentValue')
        log.logger('max current value is ' + str(data))
        return data

    # 获取最小电流值
    @staticmethod
    def getmincurrentvalue():
        log.logger('get min current value for single scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetMinCurrentValue')
        log.logger('min current value is ' + str(data))
        return data

    # 获取平均电流
    @staticmethod
    def getaveragecurrentvalue():
        log.logger('get average current value for single scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetAverageCurrentValue')
        log.logger('average current value is ' + str(data))
        return data

    # 设置当前电压和电流
    @staticmethod
    def setcurrentsource(volt, amp):
        try:
            log.logger('set nominal voltage is ' + str(volt) + ';set maximum current is ' + str(amp))
            data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'SetCurrentSource', str(volt),
                                       str(amp))
            log.logger('set nominal voltage and maximum current is ' + str(data))
            if str(data) != '0':
                raise Exception('Set volt and amp Fail')
            time.sleep(0.5)
        except Exception as e:
            log.logger(e)
            sys.exit(0)

    # 初始化安捷伦的visaid和gpib采集卡地址
    @staticmethod
    def initcurrentsource(visaid, gpibaddr):
        try:
            log.logger('connect current instrument ,VIDAID is ' + str(visaid) + ',GPIBAddress is ' + str(
                gpibaddr) + ';and start get current value for multi-scene')
            data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'InitCurrentSource',
                                       str(visaid), str(gpibaddr))
            log.logger('connect result is ' + str(data))
            if str(data) != '0':
                raise Exception('Connect Fail')
            time.sleep(0.5)
        except Exception as e:
            log.logger(e)
            sys.exit(0)

    @staticmethod
    def closecurrentsource():
        log.logger('stop power dissipation to get current value for multi-scene ')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'CloseCurrentSource')
        log.logger('stop result is ' + str(data))

    # 采集整个大过程的平均电流
    @staticmethod
    def getallavgcurrentvalue():
        log.logger('get average current value for multi-scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetAllAvgCurrentValue')
        log.logger('average current value is ' + str(data))
        return data

    # 采集整个大过程的最大电流
    @staticmethod
    def getallmaxcurrentvalue():
        log.logger('get max current value for multi-scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetAllMaxCurrentValue')
        log.logger('max current value is ' + str(data))
        return data

    # 采集整个大过程的最小电流
    @staticmethod
    def getallmincurrentvalue():
        log.logger('get min current value for multi-scene')
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'GetAllMinCurrentValue')
        log.logger('min current value is ' + str(data))
        return data

    @staticmethod
    def setcurrentrange(currentrange):
        log.logger('set current range: ' + str(currentrange))
        data = current.externaldll('AgilentMeasurement.dll', 'AgilentDCSourceClient', 'SetCurrentRange',
                                   str(currentrange))
        log.logger('min current value is ' + str(data))
