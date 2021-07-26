# -*- coding: utf-8 -*-
'''
Created on 2019年9月18日

@author: likecan
'''
import os
import datetime

logaddr = os.path.split(os.path.realpath(__file__))[0]


class log:

    @staticmethod
    def logger(*logcontent):
        logs = 'log:'
        if len(logcontent) <= 0:
            print('log empty ')
        else:
            for i in range(len(logcontent)):
                logs += str(logcontent[i]) + ';'
                log.outputlog(logs)
            print(logs)

    @staticmethod
    def scriptresult(result, *variable):
        logs = 'result:value:' + str(result) + ';'
        for i in range(len(variable)):
            log.outputlog(logs)
            logs += str(variable[i]) + ';'
        print(logs)

    @staticmethod
    def outputlog(msg):
        if os.path.exists(logaddr + '\\logs') is False:
            os.makedirs(logaddr + '\\logs')
        if os.path.exists(logaddr + '\\logs\\olog.txt') is True:
            if os.path.getsize(logaddr + '\\logs\\olog.txt') >= 10000000:
                os.rename(logaddr + '\\logs\\olog.txt', logaddr + '\\logs\\olog.txt.1')
        output = open(logaddr + '\\logs\\olog.txt', 'a')
        output.write(str(datetime.datetime.now()) + ' ' + str(msg) + '\n')
        output.close()
