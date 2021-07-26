#coding = utf-8

import unittest,sys,HTMLTestRunner,datetime,random,time,threading,psutil,gc,memory_profiler,os
sys.path.append('./')
from Interface_Test_Main.Interface_Main import interface_case

class case_unittest(unittest.TestCase):
    add_result = None
    
    
    @classmethod
    def setUpClass(cls):
        cls.i_case = interface_case()
        cls.login_result = cls.i_case.login() 
    
    
    def setUp(self):
        self.assertEqual(self.login_result.ok,True,'login failed')
        
    
    
    
    
    def test_add_new_device(self):
        device_name = 'Device_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        device_status = ['IDLE','OFFLINE','BUSY','ERROR']#设备状态
        self.add_result = self.i_case.add_new_device(self.login_result,device_name,random.choice(device_status))
        self.assertTrue(self.add_result[0],'create new device result :%s'%self.add_result[1])
        self.assertDictContainsSubset(self.add_result[2],self.add_result[1],self.add_result)
        
    
    def test_clear_devices(self):
        search_result = []
        while True:
            search_result = self.i_case.search(self.login_result)
            print(search_result)
            if search_result[0]:
                if not search_result[1]:
                    break
                for device_infor in search_result[1]:
                    print(device_infor['id'])
                    del_result = self.i_case.del_device_by_id(self.login_result,device_infor['id'])
                    self.assertTrue(del_result.ok,del_result.text)
        self.assertTrue(not search_result[1],'设备未全部删除即退出')
     
     
           
    def test_add_new_script(self):
        script_name = 'Script_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        print(script_name)
        self.add_result = self.i_case.add_script(self.login_result,script_name)
        self.assertTrue(self.add_result[0],'创建失败')
        self.assertEqual(self.add_result[1]['name'],self.add_result[2]['name'],self.add_result[2])
        self.assertEqual(self.add_result[1]['user']['id'],self.add_result[2]['user']['id'],self.add_result)
        self.assertEqual(len(self.add_result[1]['file']),len(self.add_result[2]['file']),self.add_result)
    
    
    
    def test_view_script(self):
        search_result = self.i_case.goto_script_page(self.login_result)
        self.assertTrue(search_result[0],search_result)
        self.assertTrue(search_result[1],search_result)
        check_script_infor = random.choice(search_result[1])
        view_result = self.i_case.view_script_by_id(self.login_result,check_script_infor['id'])
        self.assertTrue(view_result[0],view_result)
        self.assertDictContainsSubset(check_script_infor,view_result[1],str(search_result[1])+':'+str(view_result[1]))
        
    
    def test_clear_all_script(self):
        search_result = None
        while True:
            search_result = self.i_case.goto_script_page(self.login_result)
            self.assertTrue(search_result[0],search_result)
            if not search_result[1]:
                break
            for script_info in search_result[1]:
                print(script_info['id'])
                self.i_case.del_script(self.login_result,script_info['id'])
        self.assertEqual(not search_result[1],True,'设备未全部删除即退出')
    
    
    def test_add_new_task(self):
        task_name = 'Task_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        print(task_name)
        script = self.i_case.goto_script_page(self.login_result)
        self.assertTrue(script[0],script)
        if not script[1]:
            self.test_add_new_script()
            script = self.i_case.goto_script_page(self.login_result)
            self.assertTrue(script[0],script)
        need_script = random.choice(script[1])
        load_result = self.i_case.load_exit_script(self.login_result,need_script['file']['id'])
        self.assertTrue(load_result[0],load_result)
        self.add_result = self.i_case.add_task(self.login_result,task_name,load_result[1])
        print(self.add_result)
        self.assertTrue(self.add_result[0],self.add_result)
        self.assertEqual(self.add_result[1]['name'],self.add_result[2]['name'],self.add_result)
        self.assertEqual(len(self.add_result[1]['contents']),len(self.add_result[2]['contents']),self.add_result)
        self.assertEqual(self.add_result[0],True,'创建失败')
        
    
    def test_clear_all_task(self):
        search_result = []
        while True:
            search_result = self.i_case.goto_task_page(self.login_result)
            print(search_result)
            self.assertTrue(search_result[0],search_result)
            if not search_result[1]:
                break
            for task_info in search_result[1]:
                print(task_info['id'])
                self.i_case.del_task(self.login_result,task_info['id'])
        self.assertEqual(not search_result[1],True,'设备未全部删除即退出')
        
    
    def test_view_task(self):
        search_result = self.i_case.goto_task_page(self.login_result)
        if search_result[0] and search_result[1]:
            check_task_infor = random.choice(search_result[1])
            view_result = self.i_case.view_task_by_id(self.login_result,check_task_infor['id'])
            if view_result[0]:
                if view_result[1]['id'] == check_task_infor['id'] and view_result[1]['name'] == check_task_infor['name'] and view_result[1]['user'] == check_task_infor['user']:
                    view = True
                self.assertEqual(view,True,str(search_result[1])+':'+str(view_result[1]))
            else:
                self.assertEqual(view_result[0],True,'查询失败')
                
    
    def test_add_new_task_instance(self):
        device_serial = None
        task_instance_name = 'TaskInstance_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        search_result = self.i_case.search(self.login_result)
        self.assertTrue(search_result[0],search_result)
        account = self.i_case.check_all_account(self.login_result)
        self.assertTrue(account[0],account)
        for device_info in search_result[1]:
            if device_info['status'] == 'IDLE':
                device_serial = device_info['serial']
                break
        add_result = self.i_case.add_task_instance(self.login_result,task_instance_name,device_serial,random.choice(account[1]))
        self.assertTrue(add_result[0],add_result)
        self.assertEqual(add_result[1]['name'],add_result[2]['name'],add_result)
        self.assertEqual(add_result[1]['mode'],add_result[2]['mode'],add_result)
        self.assertEqual(add_result[1]['count'],add_result[2]['count'],add_result)
        self.assertEqual(add_result[1]['executeTime'],add_result[2]['executeTime'],add_result)
        self.assertEqual(add_result[1]['spacingIntervalTime'],add_result[2]['spacingIntervalTime'],add_result)
        self.assertEqual(add_result[1]['status'],add_result[2]['status'],add_result)
        self.assertEqual(add_result[1]['user']['id'],add_result[2]['user']['id'],add_result)
        
    
    def test_clear_all_task_instance(self):
        search_result = []
        while True:
            search_result = self.i_case.goto_task_instances_page(self.login_result)
            print(search_result)
            self.assertTrue(search_result[0],search_result)
            if not search_result[1]:
                break
            for task_instance_info in search_result[1]:
                print(task_instance_info['id'])
                self.i_case.del_task_instance(self.login_result,task_instance_info['id'])
        self.assertEqual(not search_result[1],True,'设备未全部删除即退出')
        
    
    def test_view_task_instance(self):
        search_result = self.i_case.goto_task_instances_page(self.login_result)
        self.assertTrue(search_result[0],search_result)
        if search_result[1]:
            check_task_infor = random.choice(search_result[1])
            view_result = self.i_case.view_task_instance_by_id(self.login_result,check_task_infor['id'])
            self.assertTrue(view_result[0],view_result)
            self.assertEqual(view_result[1]['id'] , check_task_infor['id'],view_result)
            self.assertEqual(view_result[1]['name'] , check_task_infor['name'],view_result)
                
    
    def test_add_new_record(self):
        device_serial = None
        record_name = 'TaskInstance_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        search_result = self.i_case.search(self.login_result)
        self.assertTrue(search_result[0],search_result)
        task_instance_info = self.i_case.goto_task_instances_page(self.login_result)
        self.assertTrue(task_instance_info[0],task_instance_info)
        self.assertTrue(task_instance_info[1],task_instance_info)
        for device_info in search_result[1]:
            if device_info['status'] == 'IDLE':
                device_serial = device_info['serial']
                break
        add_result = self.i_case.add_record_once(self.login_result,record_name,device_serial,random.choice(task_instance_info[1]))
        self.assertEqual(add_result[0],True,add_result)
        self.assertEqual(add_result[1]['scriptName'],add_result[2]['scriptName'],add_result)
        self.assertEqual(add_result[1]['isSucceed'],add_result[2]['isSucceed'],add_result)
        self.assertEqual(add_result[1]['logFilePath'],add_result[2]['logFilePath'],add_result)
        self.assertEqual(add_result[1]['isDel'],add_result[2]['isDel'],add_result)
        self.assertEqual(add_result[1]['pass'],add_result[2]['pass'],add_result)
        self.assertEqual(add_result[1]['taskInstance']['id'],add_result[2]['taskInstance']['id'],add_result)
        self.assertEqual(add_result[1]['taskInstance']['user']['id'],add_result[2]['taskInstance']['user']['id'],add_result)
            
    
    def test_view_record(self):
        search_result = self.i_case.goto_record_page(self.login_result)
        self.assertTrue(search_result[0],search_result)
        self.assertTrue(search_result[1],search_result)
        check_task_infor = random.choice(search_result[1])
        view_result = self.i_case.view_record_by_id(self.login_result,check_task_infor['id'])
        self.assertTrue(view_result[0],view_result)
        self.assertEqual(view_result[1]['id'] , check_task_infor['id'],str(search_result[1])+':'+str(view_result[1]))
        self.assertEqual(view_result[1]['scriptName'] , check_task_infor['scriptName'],str(search_result[1])+':'+str(view_result[1]))
                
       
    def test_clear_all_record(self):
        search_result = []
        while True:
            search_result = self.i_case.goto_record_page(self.login_result)
            self.assertTrue(search_result[0],search_result)
            print(search_result)
            if not search_result[1]:
                break
            for record_info in search_result[1]:
                print(record_info['id'])
                self.i_case.del_record(self.login_result,record_info['id'])
            time.sleep(1)
        self.assertEqual(not search_result[1],True,'设备未全部删除即退出')
        
    
    def test_run_task(self):
        run_mode = ['CYCLE','TIME']
        if not self.add_result:
            task_id = random.choice(self.i_case.goto_task_page(self.login_result)[1])['id']
        else:
            task_id = self.add_result[1]['id']
        run_result = self.i_case.run_task(self.login_result,task_id,random.choice(run_mode),random.randint(1,30))
        task_instance_list = self.i_case.goto_task_instances_page(self.login_result)
        # self.assertEqual(run_result[1]['id'],task_instance_list[1]['id'],run_result)
def get_suite():
    test_case_suite = unittest.TestSuite()
    # print(gc.isenabled())
    # gc.collect()
    # info = psutil.virtual_memory()
    # print('内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    # print('总内存：', info.total/(1024*1024*1024))
    # print('内存占比：', info.percent)
    # test_case_suite.addTest(case_unittest('test_add_new_device'))
    # test_case_suite.addTest(case_unittest('test_add_new_script'))
    # test_case_suite.addTest(case_unittest('test_view_script'))
    # test_case_suite.addTest(case_unittest('test_add_new_task'))
    # test_case_suite.addTest(case_unittest('test_view_task'))
    # test_case_suite.addTest(case_unittest('test_add_new_task_instance'))
    # test_case_suite.addTest(case_unittest('test_view_task_instance'))
    # test_case_suite.addTest(case_unittest('test_add_new_record'))
    # test_case_suite.addTest(case_unittest('test_view_record'))
    # test_case_suite.addTest(case_unittest('test_clear_devices'))
    # test_case_suite.addTest(case_unittest('test_clear_all_script'))
    # test_case_suite.addTest(case_unittest('test_clear_all_task'))
    # test_case_suite.addTest(case_unittest('test_clear_all_record'))
    # test_case_suite.addTest(case_unittest('test_clear_all_task_instance'))
    test_case_suite.addTest(case_unittest('test_run_task'))
    #test_case_suite.addTests([mtbf_test_case('test_dail'),mtbf_test_case('test_send_sms'),mtbf_test_case('test_check_sms')])
    #unittest.TextTestRunner().run(test_case_suite)
    html_file = '.\\report_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+'.html'
    fp = open(html_file,mode='a',errors = 'ignore')
    HTMLTestRunner.HTMLTestRunner(fp).run(test_case_suite)




if __name__ == '__main__':
    #unittest.main()
    get_suite()