# coding = utf-8

import uiautomator2 as u2
import subprocess, re, threading
from os import popen


class adb_handle(object):

    def run_weditor(self, dump_screen_tool=1):
        print('########请选择需要使用的获取界面信息的工具，请输入序号1或者2##############')
        print('1.uiautomatorviewer')
        print('2.weditor')
        if dump_screen_tool == '2':
            weditor = subprocess.Popen('python -m weditor', stdout=subprocess.PIPE, shell=True)
            weditor.stdout.read()
        elif dump_screen_tool == '1':
            ui_viewer_pre = subprocess.Popen('D:\\android-sdk-windows\\tools\\uiautomatorviewer_android.bat',
                                             stdout=subprocess.PIPE, shell=True)
            ui_viewer_pre.stdout.read()
            ui_viewer = subprocess.Popen('D:\\android-sdk-windows\\tools\\uiautomatorviewer.bat',
                                         stdout=subprocess.PIPE, shell=True)
            ui_viewer.stdout.read()

    def get_device_name(self):
        '''
        获取设备串号
        '''
        adb_device = popen('adb devices')
        adb_device_print = adb_device.read()
        device_name_list = []
        if adb_device_print.count('device') > 1:
            re_str = r'.*\t'
            re_find = re.findall(re_str, adb_device_print)
            if re_find:
                for i in range(len(re_find)):
                    device_name_list.append(re_find[i][:-1])
        return device_name_list

    def get_current_package(self) -> list:
        '''
        获取当前app的包名类名,返回[packagename,activityname]
        '''
        package_activity_name = popen('adb shell dumpsys window | findstr mCurrent')
        package_activity = package_activity_name.readlines()[1].lstrip().split(' ')[2][:-2].split('/')
        return package_activity

class my_thread(threading.Thread):
    '''
    从多线程中获取返回值
    '''

    def __init__(self, func, *args, **kwargs):
        super(my_thread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)


class basic_handle(object):

    def connect_device(self, device_info: str):
        '''
        通过adb连接设备，确保数据线连接到了pc（adb devices）
        '''
        device = u2.connect_usb(device_info)
        return device

    def connect_device_by_wifi(self, segment: str):
        '''
        通过wifi连接设备，确保手机与pc在同一网段
        param segment:传入一个ip，e.g.:192.168.30.
        '''
        return u2.connect_wifi(segment)
        # device = u2.Device
        # ip_thread_list = []
        # for i in range(1, 256):
        #     ip = segment + str(i)
        #     t = my_thread(u2.connect_wifi, ip)
        #     ip_thread_list.append(t)
        # try:
        #     for t in ip_thread_list:
        #         t.start()
        #     for t in ip_thread_list:
        #         t.join()
        #     for t in ip_thread_list:
        #         if t.result is not None:
        #             device = t.result
        # except u2.exceptions.ConnectError as e:
        #     print(e)
        # return device

    def back_home_page(self, device: u2.Device):
        """
        返回手机主界面
        """
        for back_num in range(5):
            print('press back')
            device.press('back')
        for home_num in range(3):
            print('press home')
            device.press('home')


class resources:
    def __init__(self, device: u2.Device):
        self.device = device

    def get_memory_info(self):
        return self.device.device_info['memory']

    def get_cpu_info(self):
        return self.device.device_info['cpu']

    def get_battery_info(self):
        return self.device.device_info['battery']



import time
a_device = adb_handle()
while 1:
    device_list = a_device.get_device_name()
    if not device_list:
        import datetime
        print('***********************************'+str(datetime.datetime.now())+'****找不到设备串号了****************************')
        break
    print('可以找到设备串号{}'.format(device_list))
    time.sleep(30)
