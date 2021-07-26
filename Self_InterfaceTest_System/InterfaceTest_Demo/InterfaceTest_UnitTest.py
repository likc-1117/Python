'''
Created on 2019年8月5日

@author: likecan
'''
import unittest,HTMLTestRunner,mock
from Self_InterfaceTest_System.InterfaceTest_Main.InterfaceTest_Main import interfacetest_main
from Self_InterfaceTest_System.Data_Config.Data_Read import data_read
from Self_InterfaceTest_System.Data_Config.CaseType import casetype


class interface_run_unittest(unittest.TestCase):
    
    
    
    #加上@classmethod之后表示此方法(名字恒定)为类的方法，即在类开始之前执行
    @classmethod
    def setUpClass(cls):
        super(interface_run_unittest, cls).setUpClass()
        cls.d_read = data_read('C:\\Users\\likecan\\Desktop\\','接口测试用例.xlsx',casetype.INTERFACE_DATA_TEST)
        cls.case_content = cls.d_read.data_read_excel()
        
    @classmethod
    def tearDownClass(cls):
        super(interface_run_unittest, cls).tearDownClass()
    #默认情况下每个用例函数执行之前都会被执行setup和teardown
    def setUp(self):
        print('testcase start------>')
    def tearDown(self):
        print('-------->testcase end')

    #测试用例函数的名字需要以test开头
    def test_interface_demo(self):
        for case_data in self.case_content:
            interface_main = interfacetest_main(case_data['URL'],case_data['Type'],case_data['Data'],case_data['Header'])
            net_test_result = interface_main.net_send()
            case_data['实际结果'] = net_test_result
            self.assertEqual(case_data['实际结果'], True, '测试成功')
        print('test result :/n')
        print(self.case_content)
        
    
    def test_interface_reponse(self):
        mock_data = mock.Mock(return_value='ddddddddd')
        print(mock_data)
        for case_data in self.case_content:
            interface_main = interfacetest_main(case_data['URL'],case_data['Type'],case_data['Data'],case_data['Header'])
            interface_main.net_send = mock_data
            net_test_result = interface_main.net_send()
            case_data['实际结果'] = net_test_result
            self.assertEqual(case_data['实际结果'], 'ddddddddd', '测试成功')
        print('test result :/n')
        print(self.case_content)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    report_fp = open('..//report//Report.html','wb')
    suite = unittest.TestSuite()
    #suite.addTest(interface_run_unittest('test_interface_demo'))
    suite.addTest(interface_run_unittest('test_interface_response'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_fp,title='First_Report')
    runner.run(suite)
    #unittest.TextTestRunner().run(suite)