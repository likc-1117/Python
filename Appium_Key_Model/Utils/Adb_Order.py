'''
Created on 2019年10月14日

@author: likecan
'''
#coding=utf-8

import re
from os import popen,system
class adb_order():


    
    def get_current_package_and_activity(self):
        '''
        获取当前打开的应用的包名和类名
        '''
        adb_print = popen('adb shell dumpsys window | findstr mCurrentFocus')
        adb_print_str = adb_print.read()
        re_str = r'com.+vity'
        re_find_result = re.findall(re_str,adb_print_str)
        app_information = []
        if  re_find_result:
            print(re_find_result)
            for package_activity in re_find_result:
                print(package_activity)
                if 'Main' in package_activity:
                    continue
                app_dict = {'appPackage':package_activity.split('/')[0],'appActivity':package_activity.split('/')[1]}
                app_information.append(app_dict)
        return app_information
    
    def get_device_name(self):
        '''
        获取设备串号
        '''
        adb_device = popen('adb devices')
        adb_device_print = adb_device.read()
        device_name = []
        if adb_device_print.count('device') > 1:
            re_str = r'.*\t'
            re_find = re.findall(re_str, adb_device_print)
            if re_find:
                for i in range(len(re_find)):
                    device_name.append(re_find[i][:-1])
        print(device_name)
        return device_name
                    
    
    def cmd_command(self,command):
        system(command)
        
        
    def check_port_is_used(self,port):
        '''
        判断给定的端口是否被使用
        '''
        port_check = popen('netstat -ano | findstr %s'%str(port)).readlines()
        if len(port_check) > 0:
            return True
        else:
            return False
        

