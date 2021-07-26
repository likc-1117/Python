'''
Created on 2019年11月15日

@author: likecan
'''
import time
from Appium_PO_Model.Utils.Base_Driver import base_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Appium_PO_Model.Utils.Get_Config import get_config
class get_element_config(object):
    '''
    classdocs
    '''


    def __init__(self,device_param):
        self.driver = base_driver().get_driver(device_param)
        self.get_element_config = get_config('..\\Config\\LocalElement.ini')
        
        
    def get_local_by_element(self,element):
        '''
        从指定元素配置文件中获取指定节点下的元素信息，并返回元素对象
        '''
        #get_page_ini = get_config('..\\Config\\LocalElement.ini')
        element_vlue = self.get_element_config.get_config_by_key(element)
        element_value_type = element_vlue.split('#')[0]
        element = element_vlue.split('#')[1].replace('!',':')#使用configparser读取配置文件时，由于在配置文件中默认了冒号与等号功能相同，因此需要将配置文件中的元素信息中的冒号改成感叹号，此处再更改回来
        try:
            if element_vlue:
                if element_value_type == 'id':
                    return self.driver.find_element_by_id(element)
                elif element_value_type == 'classname':
                    return self.driver.find_element_by_class_name(element)
                elif element_value_type == 'text':
                    return self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+str(element)+'")')
                elif element_value_type == 'xpath':
                    return self.driver.find_element_by_xpath(element)
                elif element_value_type == 'accessibility':
                    return self.driver.find_element_by_accessibility_id(element)
                elif element_value_type == 'desc':
                    return self.driver.find_element_by_android_uiautomator('new UiSelector().description("'+str(element)+'")')
                elif element_value_type == 'content':
                    return str(element)
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    def back(self):
        self.driver.press_keycode(4)
        
    def home(self):
        self.driver.keyevent('KEYCODE_HOME')

    def get_webview(self,web_element):
        time.sleep(10)
        web_view = self.driver.contexts  # 获取当前界面的所有子界面信息
        print(web_view)
        self.driver.switch_to.context(web_view[1])
        self.driver.find_element_by_link_text(web_element).click()
        self.driver.switch_to.context(web_view[0])
        self.driver.find_element_by_id('com.android.browser:id/back').click()

    def get_tost(self, tost_message):  # 使用xpath定位
        tost_element = ('xpath', "//*[contains(@text," + tost_message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(
            ec.presence_of_element_located(tost_element))  # 在10秒中内每间隔0.1秒去识别tost_element所指向的元素
        
        
