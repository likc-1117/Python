# -*- coding: utf-8 -*-
'''
Created on 2019年9月18日

@author: likecan
'''
import unittest
import selenium,time,os
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class auto_ui_script():
    
    
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '9'
        self.desired_caps['deviceName'] = 'D5F0218514006030'
        self.desired_caps['appPackage'] = 'com.android.contacts'
        # desired_caps['app'] = 'F:// debug.apk'
        self.desired_caps['autoLaunch'] = False
        self.desired_caps['appActivity'] = '.activities.PeopleActivity'
        self.desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        
    
    def power_on_off(self,on_off = 1):
        screen_size = self.driver.get_window_size('current')
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.9
        stop_x = screen_size['width'] * 0.5
        stop_y = screen_size['height'] * 0.3
        if on_off == 0:
            self.driver.keyevent(26, None)
            time.sleep(2)
            self.driver.swipe(start_x, start_y, stop_x, stop_y,500)
        else:
            self.driver.press_keycode(26)
        self.driver.implicitly_wait(5)
        
        
    def mute(self):
        self.driver.long_press_keycode(25)