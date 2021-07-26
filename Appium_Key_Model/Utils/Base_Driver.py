#coding = utf-8


from appium import webdriver
from Appium_PO_Model.Utils.Get_Config import get_config
from Appium_PO_Model.Utils.Device_Config import device_config
class base_driver(object):
    

    
    def __android_driver(self,device_param):
        device_infor = device_config()
        phone_caps = {}
        get_package_config = get_config('..\\Config\\App_Package_Activity.ini')
        app_package_infor = get_package_config.get_app_information(device_param['package_type'],device_param['app_name'])
        phone_caps['platformName'] = 'Android'
        #phone_caps['automationName'] = 'UiAutomator2'
        phone_caps['deviceName'] = device_param['device_name']
        if device_param['package_type'] == 'package':
            phone_caps['appPackage'] = app_package_infor[0]
            phone_caps['appActivity'] = app_package_infor[1]
        else:
            phone_caps['app'] = app_package_infor[0]
        phone_caps['noReset'] = True
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%str(device_infor.get_device_infor_from_config(phone_caps['deviceName'])['port']),phone_caps)
        return driver
    
    
    def __ios_driver(self):
        pass
    
    
    
    def get_driver(self,device_param):
        return self.__android_driver(device_param)

