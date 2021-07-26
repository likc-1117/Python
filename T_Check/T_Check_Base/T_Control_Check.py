#coding=utf-8

from T_Check.T_Check_Base.Socket_Client import socket_client
from json import dumps,loads
from os import popen

class t_control_check:

    @staticmethod
    def operation_t_machine(action,t_sequence):
        if action==0:
            action='Check'
        elif action==1:
            action='Change'
        else:
            return 'UnKnow action'
        key = ['NAME', 'ID']
        value = [action,t_sequence]
        return_data=socket_client.sendmsg(dumps(dict(zip(key,value))))
        return loads(return_data)



    @staticmethod
    def t_script_run(device_id,instance):
        popen('adb -s '+str(device_id)+' shell uiautomator runtest T_Check.jar -e num '+str(instance)+' --nohup -c com.T_Check.Check_T_In_FileManager#test_c')





