#coding = utf-8

from Uiautomator.Utils.Basic_Handle import *



device = basic_handle().connect_device(adb_handle().get_device_name())

device(text='去浏览').click_exists(5)
if device(text='任务完成').exists(timeout=12):
    device.press('back')