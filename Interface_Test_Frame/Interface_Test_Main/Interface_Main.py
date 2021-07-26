#coding = utf-8


import requests,random,re
import json
import sys
sys.path.append('./')
from Data.Case_Item import case_item_handle
from Data.Case_Document_Handle import case_doucument_handle,data_handle
from Json_File_Handle.Json_File_Read import json_file_read



class interface_main(object):
    
    def __init__(self):
        self.jfr = json_file_read()
        
    
        
    
    def interface_request(self,case_id,url,data,method,header,cookie = None,has_dependent = None,dependent_item = None):
        
        #获取测试用例中的普通数据
        if has_dependent:#如果有依赖
            print('Noneddddd')
            dependent_case_result = self.jfr.read_content_from_json(case_id,'Dependent_Result')#将依赖用例的结果数据获取到
            if not dependent_item :
                if not dependent_case_result.ok:#如果没有依赖数据的字段，即是需要判断依赖用例是否执行成功即可
                    return None
            elif dependent_item:#需要依赖用例结果数据中的某个字段
                data[dependent_item] = dependent_case_result[dependent_item]
        request_result = getattr(requests,method.lower())(url,data=json.dumps(data),headers=header)
        print('result:%s'%request_result.text)
        self.jfr.send_request_result_data_to_json(case_id,request_result.text)
        return request_result

    
class interface_case():
    def __init__(self):
        self.case_read = case_doucument_handle()
        self.data_h = data_handle()
        self.jfr = json_file_read()
        self.item_handle = case_item_handle()
        self.im = interface_main()
    
    
    
    def get_row(self,case_id):
        '''
        根据测试用例id返回当前测试用例在excel中的行号
        '''
        row = self.case_read.get_row_num(case_id)
        if self.case_read.get_cell_content(row,self.item_handle.is_run()).lower() == 'no':#判断此用例是否需要执行
            return None
        return row    
    
    def get_header(self,case_id,header_dependent = None):
        '''
        从header文档中获取header，并修改header中Authorization（用户信息，此值来自于登陆接口运行后的返回值）
        '''
        header = self.jfr.read_content_from_json(case_id,'Header')
        if header_dependent:#修改header中Authorization的值
            header['Authorization'] = 'Bearer %s'%str(header_dependent)
        print('header:%s'%header)
        return header
    
    def get_data(self,case_id):
        '''
        获取接口传输数据，数据从一个json文件中获取
        '''
        data = self.jfr.read_content_from_json(case_id,'Request_Data')
        print('data：%s'%data)
        return data
    
    
    def get_url(self,case_id):
        '''
        从测试用例文档（excel文件）中获取接口地址
        '''
        url = self.case_read.get_cell_content(self.get_row(case_id),self.item_handle.request_url())
        print('url:%s'%url)
        return url
    
    
    def get_method(self,case_id):
        '''
        从测试用例文档（excel文件）中获取接口类型
        '''
        method = self.case_read.get_cell_content(self.get_row(case_id),self.item_handle.request_type())
        print(method)
        return method
    
    def get_cookie(self,case_id):
        '''
        从cookie文档（json文件）中获取cookie数据
        '''
        cookie = self.jfr.read_content_from_json(case_id,'Cookie')
        print('cookie:%s'%cookie)
        return cookie
    
    def has_dependent(self,case_id):
        '''
        从测试用例文件（excel文件）中获取用例id对应的这个用例是否有依赖测试用例
        '''
        has_dependent = self.case_read.get_cell_content(self.get_row(case_id),self.item_handle.dependent_case_id())
        print('has_dependent:%s'%has_dependent)
        return has_dependent
    
    def dependent_item(self,case_id):
        '''
        获取依赖的内容
        '''
        dependent_item = self.case_read.get_cell_content(self.get_row(case_id),self.item_handle.dependent_data_item())
        print('dependent_item:%s'%dependent_item)
    
    
    
    def login(self):
        '''
        平台登陆，是接下来所有操作的先决条件，此函数的返回值用于修改每一个接口的header中的Authorization
        '''
        case_id = 'login'
        login_result = self.im.interface_request(case_id,self.get_url(case_id),self.get_data(case_id),self.get_method(case_id),self.get_header(case_id))
        return login_result#返回登陆结果
        
        
    def search(self,login_result):
        '''
        检索设备页的内容，只检索设备页的第一分页
        '''
        case_id = 'Search'
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取header数据
        search_result = self.im.interface_request(case_id,self.get_url(case_id),self.get_data(case_id),self.get_method(case_id),header)
        return (search_result.ok,json.loads(search_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def add_new_device(self,login_result,device_name,device_status):
        '''
        增加新设备
        '''
        case_id = 'Add_New_Device'#增加设备用例的id
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取header数据
        data = self.get_data(case_id)#获取接口传输数据
        data['name'] = device_name#根据函数传入的设备名称（device_name）修改data中的name的值
        data['status'] = device_status#从device_status中随机取一个值作为data中的status的值
        add_device_result = self.im.interface_request(case_id,self.get_url(case_id),data,self.get_method(case_id),header)#接口测试语句
        return (add_device_result.ok,json.loads(add_device_result.text),data)#返回接口测试结果
    
    def del_device_by_id(self,login_result,device_id):
        '''
        根据设备id号删除设备
        '''
        case_id = 'Del_Device'#此接口用例的id号
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        url = self.get_url(case_id)+str(device_id)
        print(url)
        del_device_result = self.im.interface_request(case_id,url,self.get_data(case_id),self.get_method(case_id),header)
        return del_device_result
    
    def goto_script_page(self,login_result):
        '''
        刷新脚本页，并返回脚本页第一分页的所有脚本信息
        '''
        case_id = 'Goto_ScriptPage'
        url = self.get_url(case_id)#获取接口地址
        data = self.get_data(case_id)#获取接口数据
        method = self.get_method(case_id)#获取接口类型
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取接口header
        goto_script_page_result = self.im.interface_request(case_id,url,data,method,header)
        return (goto_script_page_result.ok,json.loads(goto_script_page_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def goto_add_script_page(self,login_result):
        '''
        进入新增脚本页
        '''
        case_id = 'Goto_AddScriptPage'
        url = self.get_url(case_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        goto_add_script_page_result = self.im.interface_request(case_id,url,data,method,header)
        return (goto_add_script_page_result.ok,json.loads(goto_add_script_page_result.text))
    
    
    def add_script(self,login_result,script_name):
        '''
        新增脚本
        '''
        case_id = 'Add_New_Script'
        url = self.get_url(case_id)
        data = self.get_data(case_id)
        data['name'] = script_name#根据传入的脚本名字修改data中name的值
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        add_result = self.im.interface_request(case_id,url,data,method,header)
        return (add_result.ok,json.loads(add_result.text),data)#返回接口测试结果
    
    
    
    
    def goto_record_page(self,login_result):
        '''
        刷新记录页，并返回记录页第一分页的内容
        '''
        case_id = 'Record'
        url = self.get_url(case_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        search_result = self.im.interface_request(case_id,url,data,method,header)
        return (search_result.ok,json.loads(search_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    def view_record_by_id(self,login_result,record_id):
        '''
        根据记录id号查看对应的记录内容
        '''
        case_id = 'Check_Record'
        url = self.get_url(case_id)+str(record_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        header['Referer'] = re.sub(r'/\d+/','/%s/'%str(record_id),header['Referer'])#根据记录id号修改header中的Referer的值,例如Referer的值为"http://192.168.30.36:8090/task-instance-detail-result/1450/view"时即查看1450号记录的内容
        view_result = self.im.interface_request(case_id,url,data,method,header)
        return (view_result.ok,json.loads(view_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def add_record_once(self,login_result,record_name,device_serial,taskinstace):
        '''
        增加一条新的记录
        '''
        case_id = 'Add_Record'
        url = self.get_url(case_id)
        data = self.get_data(case_id)#data的值需要修改
        data['scriptName'] = record_name#根据传入的记录名（record_name）修改data中的scriptName（记录名）的值
        if not device_serial:#检测是否传入的设备串号
            data.pop('device')#如果美哟传入设备串号，则去掉data中原有的device项
        else:
            data['device'] = device_serial
        if not taskinstace:#检测是否为该条新增记录指定了对应的任务实例
            data.pop('taskInstance')#如果没有指定任务实例，则去掉data中原有的taskInstance项
        else:
            data['taskInstance'] = taskinstace
        data['pass'] = random.choice([True,False])#随机为data中的pass项（即脚本是否通过）赋值
        data['isDel'] = random.choice([True,False])#随机为data中的isDel项（即是否删除）赋值
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        add_result = self.im.interface_request(case_id,url,data,method,header)
        return (add_result.ok,json.loads(add_result.text),data)#接口返回值
    
    
    def edit_record(self,login_result,new_script_name = None):
        '''
        修改记录
        '''
        case_id = 'Edit_Record'
        url = self.get_url(case_id)
        data = self.get_data(case_id)#data的值需要修改
        data['scriptName'] = new_script_name
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        edit_result = self.im.interface_request(case_id,url,data,method,header)
        return edit_result
    
    def view_task_by_id(self,login_result,task_id):
        '''
        根据任务id查看此任务内容
        '''
        case_id = 'Check_Task'
        url = self.get_url(case_id)+str(task_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        header['Referer'] = re.sub(r'/\d+/','/%s/'%str(task_id),header['Referer'])#根据任务id号修改header中的Referer的值,例如Referer的值为""http://192.168.30.36:8090/task/156/view""时即查看156号任务的内容
        view_result = self.im.interface_request(case_id,url,data,method,header)
        return (view_result.ok,json.loads(view_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def edit_task(self,login_result,new_task_name = None):
        '''
        修改任务内容
        '''
        case_id = 'Edit_Record'
        url = self.get_url(case_id)+str(record_id)
        data = self.get_data(case_id)#data的值需要修改
        data['scriptName'] = new_task_name
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        edit_result = self.im.interface_request(case_id,url,data,method,header)
        return edit_result
    
    
    def add_task(self,login_result,task_name = 'Task',contents = None):
        '''
        新增一条任务
        '''
        case_id = 'Add_Task'
        url = self.get_url(case_id)
        data = self.get_data(case_id)#data的值需要修改
        data['name'] = task_name#根据传入的任务名修改data中name的值
        if not contents:
            data.pop('contents')
        else:
            add_content = random.sample(contents,random.randint(1,len(contents)-1))
            init_content_item = {"scriptName":"通用_打开应用程序","index":1,"count":1,"spacingIntervalTime":0,"scriptSetName":"U","scriptSetVersion":"1.0.0.2","script":None}
            for add_script in add_content:
                init_content_item['scriptName'] = add_script['name']
                init_content_item['script'] = add_script
                data['contents'].append(init_content_item)
        print(data)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        add_result = self.im.interface_request(case_id,url,data,method,header)
        return (add_result.ok,json.loads(add_result.text),data)
    
    def del_task(self,login_result,task_id):
        '''
        根据任务id删除此任务
        '''
        case_id = 'Del_Task'
        url = self.get_url(case_id)+str(task_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        del_result = self.im.interface_request(case_id,url,data,method,header)
        return del_result
    
    
    def del_record(self,login_result,record_id):
        '''
        根据记录id删除记录
        '''
        case_id = 'Del_Record'
        url = self.get_url(case_id)+str(record_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        del_result = self.im.interface_request(case_id,url,data,method,header)
        return del_result
    
    def del_script(self,login_result,script_id):
        '''
        根据脚本id删除脚本
        '''
        case_id = 'Del_Script'
        url = self.get_url(case_id)+str(script_id)
        print(url)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        del_result = self.im.interface_request(case_id,url,data,method,header)
        return del_result
    
    
    def goto_task_page(self,login_result):
        '''
        刷新任务页，并返回任务页第一分页的内容
        '''
        case_id = 'Goto_TaskPage'
        url = self.get_url(case_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        search_result = self.im.interface_request(case_id,url,data,method,header)
        return (search_result.ok,json.loads(search_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def goto_task_instances_page(self,login_result):
        '''
        刷新任务实例页，并返回任务实例页第一分页的内容
        '''
        case_id = 'Goto_TaskInstancePage'
        url = self.get_url(case_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        search_result = self.im.interface_request(case_id,url,data,method,header)
        return (search_result.ok,json.loads(search_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def view_task_instance_by_id(self,login_result,task_instance_id):
        '''
        根据任务实例的id查看此任务实例的内容
        '''
        case_id = 'Check_Task_Instance'
        url = self.get_url(case_id)+str(task_instance_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        header['Referer'] = re.sub(r'/\d+/','/%s/'%str(task_instance_id),header['Referer'])
        view_result = self.im.interface_request(case_id,url,data,method,header)
        return (view_result.ok,json.loads(view_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    def add_task_instance(self,login_result,task_instance_name,device_serial,user):
        '''
        新增任务实例
        '''
        case_id = 'Add_New_TaskInstance'
        task_status = ['IDLE','RUN','PAUSE','COMPLETE','ERROR']#任务状态
        task_mode = ['CYCLE','TIME']#任务模式：按次执行或者按时间执行
        url = self.get_url(case_id)#获取接口（url）
        data = self.get_data(case_id)#获取接口传输的数据
        data['name'] = task_instance_name#修改任务实例的名称
        data['mode'] = random.choice(task_mode)#随机从task_mode中选择一个值，并以此值修改传输数据中的内容
        data['count'] = random.randint(1,500)#随机给出运行次数
        data['executeTime'] = random.randint(0,20)#随机给出脚本间隔时间
        if not device_serial:#判断是否给出了任务关联的设备串号
            data.pop('deviceSerial')#如果没有给定设备串号，则需要保证传输数据中没有设备串号这一项
        else:
            data['deviceSerial'] = device_serial
        
        data['status'] = random.choice(task_status)#随机从task_status中选择一个值最为任务实例的状态
        data['user'] = user#规定当前任务所属的用户
        print(data)
        method = self.get_method(case_id)#获取此接口的类型
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取接口的header
        add_result = self.im.interface_request(case_id,url,data,method,header)#接口测试语句
        return (add_result.ok,json.loads(add_result.text),data)#返回接口测试结果
    
    def del_task_instance(self,login_result,task_instance_id):
        '''
        删除一个任务实例
        '''
        case_id = 'Del_TaskInstance'
        url = self.get_url(case_id)+str(task_instance_id)#从测试用例文档（excel文件）中获取接口地址，并与待删除的任务实例拼接
        print(url)
        data = self.get_data(case_id)#获取接口传输的数据
        method = self.get_method(case_id)#获取接口类型
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取接口header
        del_result = self.im.interface_request(case_id,url,data,method,header)#接口测试语句
        return del_result
        
    def check_all_account(self,login_result):
        '''
        查询所有的管理员
        '''
        case_id = 'Check_Account'
        url = self.get_url(case_id)#获取接口地址
        data = self.get_data(case_id)#获取接口传输数据
        method = self.get_method(case_id)#获取接口类型
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])#获取header
        search_result = self.im.interface_request(case_id,url,data,method,header)#接口测试语句
        return (search_result.ok,json.loads(search_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    
    
    def view_script_by_id(self,login_result,script_id):
        '''
        查看指定id号的脚本内容
        '''
        case_id = 'Check_Script'
        url = self.get_url(case_id)+str(script_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        header['Referer'] = re.sub(r'/\d+/','/%s/'%str(script_id),header['Referer'])
        view_result = self.im.interface_request(case_id,url,data,method,header)
        return (view_result.ok,json.loads(view_result.text))#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
    
    def run_task(self,login_result,task_id,run_mode,run_times_or_time):
        '''
        运行指定id的任务
        '''
        case_id = 'Run'
        idle_device = []
        search = self.search(login_result)#检索设备
        print(search)
        if search[0]:
            if not search[1]:#如果没有设备，则新建一个状态为IDLE的新设备
                self.add_new_device(login_result,'Device','IDLE')
                search = self.search(login_result)
            for device_info in search[1]:#将检索得到的所有设备中，状态为IDLE且具备串号的设备信息中的串号放到一个专门的列表中
                if device_info['status'] == 'IDLE' and device_info['serial']:
                    idle_device.append(device_info['serial'])
            if not idle_device:#如果所有检索到的设备的状态都不是IDLE，即检索得到的所有设备都不可用，则新建一个可用的新设备
                device_info = self.add_new_device(log_result,'Device','IDLE')
                idle_device.append(device_info['serial'])
            view_result = self.view_task_by_id(login_result,task_id)#根据任务id查看任务具体信息，并获得其中的脚本列表
            url = self.get_url(case_id)
            data = self.get_data(case_id)
            data['name'] = view_result[1]['name']
            data['mode'] = run_mode
            data['count'] = run_times_or_time
            data['deviceSerial'] = random.choice(idle_device)
            data['contents'] = view_result[1]['contents']#将任务的脚本列表赋值给接口数据中的contents关键字
            method = self.get_method(case_id)
            header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
            header['Referer'] = re.sub(r'/\d+/','/%s/'%str(task_id),header['Referer'])
            run_result = self.im.interface_request(case_id,url,data,method,header)
            return (run_result.ok,json.loads(run_result.text),data)#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
        return (search.ok,json.loads(search.text),None)
    
    
    def load_exit_script(self, log_result,script_file_id):
        '''
        读取已有的脚本的内容
        '''
        case_id = 'Load_Script'
        url = self.get_url(case_id)+str(script_file_id)
        data = self.get_data(case_id)
        method = self.get_method(case_id)
        header = self.get_header(case_id,json.loads(login_result.text)['id_token'])
        search_result = self.im.interface_request(case_id,url,data,method,header)
        return (search_result.ok,json.loads(search_result.text),data)#返回接口测试结果，此处返回一个tuple类型，第一个值为测试接口True/False，第二个值为接口返回数据
        
        


        
