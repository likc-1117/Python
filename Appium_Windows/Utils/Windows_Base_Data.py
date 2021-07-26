# coding = utf-8
import time

from appium import webdriver
from selenium import webdriver as webd
import uiautomation as auto

app = auto.WindowControl(ClassName='Window', searchDepth=1)
print(app.Element)


class windows_base_data(object):

    def __init__(self):
        win_caps = {
            'app': 'E:\\Finger_SoftWare\\AutoProgram.exe'
            # 'appWorkingDir' : 'E:\\Mobot_English_Version\\Release',
            # 'app':'E:\\Mobot_English_Version\\Release\\Mobot.MSConvert.exe',
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=win_caps)

    def create_new_mode(self):
        try:
            time.sleep(5)
            element_xpath = '//TextBlock'
            print('goto click point:')
            return_text = self.driver.find_element_by_xpath(element_xpath)
            print(return_text)
            print(return_text.text)
        except Exception as e:
            print(e)
        finally:
            # pass
            self.driver.quit()

    def enter_setup_page(self):
        self.driver.find_element_by_name('Main button').click()
        self.driver.find_element_by_name('设备配置').click()
        self.driver.find_element_by_name('Main button').click()

    def enter_log_page(self):
        self.driver.find_element_by_name('Main button').click()
        self.driver.find_element_by_name('日志').click()
        self.driver.find_element_by_name('Main button').click()

    def enter_interface_page(self):
        self.driver.find_element_by_name('Main button').click()
        self.driver.find_element_by_name('接口测试').click()
        self.driver.find_element_by_name('Main button').click()

    def import_exist_config(self):
        self.driver.find_element_by_name('导入').click()
        # time.sleep(3)
        self.driver.find_element_by_name('Axis.config').click()
        # time.sleep(3)
        self.driver.find_element_by_name('打开(O)').click()
        # time.sleep(3)
        self.driver.find_element_by_name('OK').click()

    def edit_ip_and_port(self, server_ip=None, port=None):
        if server_ip:
            self.driver.find_element_by_accessibility_id('ipbox').clear()
            self.driver.find_element_by_accessibility_id('ipbox').send_keys(server_ip)
        if port:
            self.driver.find_element_by_accessibility_id('portbox').clear()
            self.driver.find_element_by_accessibility_id('portbox').send_keys(port)

    def edit_step(self, step=None):
        if step:
            self.driver.find_element_by_accessibility_id('PART_TextBox').clear()
            self.driver.find_element_by_accessibility_id('PART_TextBox').send_keys('1')
            self.driver.press_keycode(66)

    def connect_machine(self, control_port, warm_box_port=None):
        x_path = '//TabItem[4]/Button'
        button_content = self.driver.find_elements_by_xpath(x_path)
        print(button_content)
        button_content[-1].click()
        port_choise = self.driver.find_elements_by_class_name('ComboBox')
        # 控制板端口
        port_choise[0].click()
        self.driver.find_element_by_name(control_port).click()
        if warm_box_port:
            # 温箱端口
            port_choise[1].click()
            self.driver.find_element_by_name(warm_box_port).click()
        self.driver.find_element_by_name('连接').click()

    def check_is_connect_success(self):
        self.enter_log_page()
        pass
        # 每次连接前清空log文件夹下的所有文件，连接后去读取log文件夹下日志文件的内容，判断是否连接成功

    def set_step_legth(self):
        time.sleep(4)
        x_path = '//TabItem[4]/ListBoxItem'
        text_content = self.driver.find_elements_by_xpath(x_path)
        print(text_content)
        # text_content[-1].click()
        # self.driver.find_element_by_accessibility_id('PART_TextBox').clear()
        # self.driver.find_element_by_accessibility_id('PART_TextBox').send_keys('1')
        print(self.driver.find_elements_by_class_name('ComboBox'))
