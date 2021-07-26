# -*- coding: utf-8 -*-
'''
Created on 2019年8月1日

@author: likecan
'''
import mock
from Self_InterfaceTest_System.InterfaceTest_Main.InterfaceTest_Main import interfacetest_main
from Self_InterfaceTest_System.Data_Config.Data_Read import data_read,casetype
from Self_InterfaceTest_System.Data_Config.Check_Return_Data import check_return_data
from Self_InterfaceTest_System.Local_Response.local_response import local_response

class script_demo:
    
    def __init__(self,datafile_path,datafile_name,case_type):
        self.local_resp = local_response('ddddd')
        self.check_result = check_return_data()
        d_read = data_read(datafile_path,datafile_name,case_type)
        self.case_content = d_read.data_read_excel()
        
        
    def script_run(self):
        test_return = None
        for case_data in self.case_content:
            interface_main = interfacetest_main(case_data['URL'],case_data['Type'],case_data['Data'],case_data['Header'])
            net_test_result = interface_main.net_send()
            case_data['实际结果'] = net_test_result
            test_return = check_return_data(case_data['预期结果'],case_data['实际结果'])
        print(self.case_content)
        return test_return
    
    def interface_return_test(self):
        for case_data in self.case_content:
            interface_main = interfacetest_main(case_data['URL'],case_data['Type'],case_data['Data'],case_data['Header'])
            interface_main.net_send = self.local_resp.local_res()
            net_test_result = interface_main.net_send()
            case_data['实际结果'] = net_test_result
            print(case_data)
            if self.check_result.check_return_data_by_str(case_data['预期结果'],case_data['实际结果']):
                print('测试通过')
            else:
                print('测试失败')
        print(self.case_content)
                

demo  = script_demo('C:\\Users\\likecan\\Desktop\\','接口测试用例.xlsx',casetype.INTERFACE_DATA_TEST)
demo.interface_return_test()