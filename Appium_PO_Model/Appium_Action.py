'''
Created on 2020年4月10日

@author: likecan
'''
from appium import webdriver
class appium_action(object):
    '''
    classdocs
    '''


    def __init__(self):
        phone_caps = {}
        phone_caps['platformName'] = 'Android'
        #phone_caps['automationName'] = 'UiAutomator2'
        phone_caps['deviceName'] = 'HJS5T19522018628'
        phone_caps['appPackage'] = 'com.android.settings'
        phone_caps['appActivity'] = 'com.android.settings.facechecker.unlock.FaceUnLockSettingsActivity'
        phone_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',phone_caps)
        
        
    def swip_to_element(self):
        message = 'new UiSelector().description("PIN 码区域")'
        screen_size = self.driver.get_window_size()
        print(screen_size)
        self.driver.unlock()
        self.driver.swipe(screen_size['width'] / 2, screen_size['height'] / 2, screen_size['width'] / 2, screen_size['height'] / 10)
        self.driver.find_element_by_android_uiautomator(message).send_keys('111111')
#         self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiObject(new UiSelector().text("生物识别和密码")))')
#         self.driver.drag_and_drop(self.driver.find_element_by_android_uiautomator('new UiSelector().text("WLAN")'), self.driver.find_element_by_android_uiautomator(message))
#         self.driver.drag_and_drop(self.driver.find_element_by_accessibility_id('com.android.settings:id/dashboard_container'), self.driver.find_element_by_android_uiautomator(message))
#         self.driver.find_element_by_name('蓝牙').click()

    def html_view(self):
        web_element = self.driver.find_element_by_id('android:id/statusBarBackground')
        print(web_element)
        
        
        
        
appium_ac = appium_action()
appium_ac.html_view()