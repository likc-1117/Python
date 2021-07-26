# -*- coding: utf-8 -*- 
import os, sys, sqlite3, time, datetime
import xml.etree.ElementTree as et
from xml.dom.minidom import Document
import xlwt, xlrd
from xlutils.copy import copy
class run_task(object):
    
    
    def __init__(self,taskname = 'NewTest',taskdbaddr = 'E:\\Mobot Files\\tasks\\task.db',msaddr = 'E:\\TT.ms',taskxmladdr = 'D:\\task.xml'
                 ,resultaddr = 'D:\\',scriptlist = ('all',)):
        super().__init__()
        self.taskname = taskname#任务名称
        self.taskdbaddr = taskdbaddr#task.db的路径
        self.msaddr = msaddr#MS文件的路径
        self.taskxmladdr = taskxmladdr#task.xml的存放路径
        self.resultaddr = resultaddr#任务执行结果数据导出后，形成的文件的存放路径
        self.scriptlist=scriptlist#要创建的任务中包含的脚本的名字
    # Search scriptname in MS file  查询ms文件中所有的脚本的名称，并打印到D：\scriptlist.txt文档中，用于作为创建task.xml时的参考
    # scriptaddr    :        MS file location,such as 'D:\\MobotMaterial\\MTBF相关\\四合一的用例及资源\\mtbf测试\\MTBF测试模板V3.0.ms'
    # this def will return all scripts  in MS file
    #检查任务列表中的任务，如果任务名称重复，则重命名
    def checktaskname(self):
        opens=sqlite3.connect(self.taskdbaddr,isolation_level=None)#连接db数据库
        c=opens.cursor()#设置游标
        try:
            c.execute('SELECT TaskName FROM TaskMain WHERE TaskName LIKE "{}%"'.format(self.taskname))#执行sql语句
            tasknamelist=c.fetchall()#获取语句执行的结果
            listlen=len(tasknamelist)
        except Exception as e:
            print(e)
        finally:
            opens.close()#关闭数据库连接
            return self.taskname+str(listlen+1)
            
    
    def selectscript(self):
        '''
        从ms文件中读取所有的脚本名称
        '''
        opens = sqlite3.connect(self.msaddr, isolation_level=None)
        c = opens.cursor()
        try:
            c.execute('SELECT Name FROM TestCase WHERE TestType=0')
            tatalscriptlist = c.fetchall()
            with open('D:\\scriptlist.txt', 'w') as sl:
                for script in tatalscriptlist:
                    sl.writelines(str(script[0])+'\n')
            return tatalscriptlist
        except Exception as e:
            print(e)
        finally:
            opens.close()
            
    #查询数据库中制定任务中脚本的成功次数，失败次数和位置次数
    def opentaskdb(self,select_taskname,isall=''):
        successnum=0
        failnum=0
        unknownum=0
        opens = sqlite3.connect(self.taskdbaddr, isolation_level=None)
        c = opens.cursor()
        try:
            c.execute('SELECT TaskName FROM TaskExecuteResult WHERE TaskName LIKE "%{}%" ORDER BY StartDate DESC '.format(select_taskname))
            searchname = c.fetchall()
            if isall == 'all':
                c.execute('SELECT ScriptName,StartDate,EndDate,IsSucceed,remark FROM ScriptExecuteDetailResult ')
            else:        
                c.execute("SELECT ScriptName,StartDate,EndDate,IsSucceed,ID,remark FROM ScriptExecuteDetailResult WHERE ser_id in (SELECT ID FROM ScriptExecuteResut WHERE ter_id in(SELECT ID FROM TaskExecuteResult WHERE TaskName='{}') ) ".format(searchname[0][0]))
            runscriptlist = c.fetchall()
            print(runscriptlist)
            for result in runscriptlist:
                if result[3]=='成功':
                    successnum=successnum+1
                elif result[3]=='未知':
                    unknownum=unknownum+1
                else:
                    failnum=failnum+1
            return runscriptlist,successnum,failnum,unknownum
        except Exception as e:
            print(e)
        finally:
            opens.close()


    #查询数据库中指定任务下所有同名脚本的结果数据的平均值
    def averageresult(self,select_taskname):
        total=0
        avglist=[]
        opens = sqlite3.connect(self.taskdbaddr, isolation_level=None)
        c = opens.cursor()
        try:
            c.execute('SELECT TaskName FROM TaskExecuteResult WHERE TaskName LIKE "%{}%" ORDER BY StartDate DESC '.format(
                select_taskname))
            searchname = c.fetchall()
            for script in self.scriptlist:
                if not script:
                    continue
                c.execute("SELECT Value FROM ExecuteResult WHERE CaseId in (SELECT ID FROM ScriptExecuteDetailResult WHERE ScriptName='{}'"
                        " AND ser_id in (SELECT ID FROM ScriptExecuteResut WHERE ter_id in(SELECT ID FROM TaskExecuteResult "
                        "WHERE TaskName='{}')) AND IsSucceed='成功') ORDER BY Value DESC ".format(script,searchname[0][0]))
                runsrciptlist = c.fetchall()
                for i in range(1,len(runsrciptlist)-1):
                    #print(runsrciptlist[i][0])
                    total+=float(runsrciptlist[i][0])
                avglist.append(script+' 结果平均值为:'+str(total/(len(runsrciptlist)-2)))
            return avglist
        except Exception as e:
            print(e)
        finally:
            opens.close()
    #删除创建的任务
    def deltask(self):
        opens = sqlite3.connect(self.taskdbaddr, isolation_level=None)
        c = opens.cursor()
        try:
            c.execute('SELECT ID FROM TaskMain WHERE TaskName="{}"'.format(self.taskname))
            tasklist = c.fetchall()
            print(tasklist)
            for taskid in tasklist:
                c.execute("DELETE FROM TaskMain WHERE ID='{}'".format(taskid[0]))
                c.execute("DELETE FROM TaskDetail WHERE ID='{}'".format(taskid[0]))
        except Exception as e:
            print(e)
        finally:
            opens.close()


    #检查当前是否有任务在执行
    def checkprocessexist(self,newtaskname):
        opens = sqlite3.connect(self.taskdbaddr, isolation_level=None)
        c = opens.cursor()
        try:
            c.execute("SELECT state FROM TaskOrders WHERE TaskMain_ID IN (SELECT ID FROM TaskMain WHERE TaskName='{}')".format(newtaskname))
            taskstate=c.fetchall()
            if taskstate:
                if taskstate[-1][0]==2 or taskstate[-1][0]==3 or taskstate[-1][0]==6:
                    return True
            else:
                return False
        except Exception as e:
            print(e)
    def readresultexcel(self,excelname):
        excelr = xlrd.open_workbook(excelname)
        sheet = excelr.sheet_by_index(0)

    def createnode(self,doc, prenode, node, nodetxt=''):
        element = doc.createElement(node)
        if nodetxt is not '':
            elementxt = doc.createTextNode(nodetxt)
            element.appendChild(elementxt)
        prenode.appendChild(element)
        return element

    #删除指定目录下已有的task.xml，为创建新的xml做准备
    def deletexml(self):
        if os.path.exists(self.taskxmladdr):
            os.remove(self.taskxmladdr)



    # Create Task ,Param means:创建task.xml文件
    # msaddr    :    MS file address
    # taskname  :    the task name
    # *scriptlist  : Scripts that are expected to be added to the task
    def taskxml(self):
        # scriptlist=opensqlite(addr)
        self.deletexml()
        try:
            nodecontent = {'taskname':self.checktaskname(),'remark':'test','MSFilePaht':self.msaddr,'scriptItems':''}
            xmlnode = ''
            scriptnode = None
            doc = Document()
            root = doc.createElement('tasks')
            doc.appendChild(root)
            secnode = doc.createElement('task')
            root.appendChild(secnode)
            for node_name,node_data in nodecontent.items():
                xmlnode = self.createnode(doc, secnode, node_name, node_data)
            if not self.scriptlist:
                raise Exception('sciptlist is empty')
            else:
                if self.scriptlist[0] == 'all':
                    self.scriptlist = self.selectscript()
                for scriptname in self.scriptlist:
                    scriptnode = doc.createElement('scriptItem')
                    if type(scriptname) is str:
                        scriptnode.setAttribute('ScriptName', scriptname)
                    else:
                        scriptnode.setAttribute('ScriptName', scriptname[0])
                    scriptnode.setAttribute('ExecuteTime', '0')
                    scriptnode.setAttribute('LoopNum', '1')
                    scriptnode.setAttribute('TaskType', '1')
                    scriptnode.setAttribute('SpacingInterval', '1')
                    scriptnode.setAttribute('dateType', '')
                    scriptnode.setAttribute('SpacingIntervalDateType', '秒')
                    xmlnode.appendChild(scriptnode)
            with open(self.taskxmladdr, 'w', buffering=1024,encoding='utf-8') as f:
                doc.writexml(f, addindent='\t', newl='\n',encoding='utf-8')
            with open(self.taskxmladdr, 'w+', buffering=1024,encoding='utf-8') as fw:
                data = fw.readlines()
                fw.seek(0)
                fw.truncate()
                fw.writelines(data[1:])
        except Exception as e:
            print(str(e))
    
    

        
        
        
    
    
    
        
        

    #taskxml()
    #在执行器中创建任务，任务名称由本页前部的taskname变量决定
    def createtask(self):
        try:
            #deltask()
            #Common.executeCommand(ad, 'Mobot.StartTask.exe CreateTask ' + str(taskxmladdr))
            os.popen(sys.path[0]+'\\Mobot.StartTask.exe CreateTask ' + str(self.taskxmladdr))  # create task    ,at first,you shoud copy this .py file to the  folder under mobotsystem folder named Mobot.StartTask
        except Exception as e:
            print(str(e).encode('utf-8'))
    # Run Task,Cycle index is 100000,execution interval is 0执行任务
    def runtask(self,newtaskname,internal, cycletimes):
        os.popen(sys.path[0]+'\\Mobot.StartTask.exe StartTask ' + str(newtaskname) + ' ' + str(internal) + ' ' + str(cycletimes))
        starttime = datetime.datetime.now()
        while (datetime.datetime.now() - starttime).seconds < 20:
            if checkprocessexist() ==0:
                print('script is executing')
                break




    # Get result ,and output them ,param means:当当前正在执行的任务结束时，将刚结束的任务结果导出到执行路径下，excel文档
    # taskdbaddr   :     the db file named task.db located in the MobotFiles\tasks folder ,such as 'D:\\Mobot Files\\tasks\\task.db'
    # resultreportname  :   result report name , if resultreportname is ''or you do not input anything,it will be named 'result.xls'
    # srearchtaskname   :    the task name that excepted to get result
    def outputresultexcel(self,newtaskname):
        try:
            while True:
                if checkprocessexist():
                    print('script is finished')
                    nowtime = datetime.datetime.now()
                    resultreportname = newtaskname + str(nowtime.month) + str(nowtime.day) + str(nowtime.hour) + str(nowtime.minute) + str(nowtime.second)
                    content,success,fail,unknow = opentaskdb(self.taskdbaddr)
                    titlelist = ['脚本名称', '起始时间', '结束时间', '脚本执行结果', '结果数值展示']
                    listnum = len(titlelist)
                    excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
                    sheet = excel.add_sheet('result', cell_overwrite_ok=True)
                    for i in range(listnum):
                        sheet.write(0, i, titlelist[i])
                        for j in range(len(content)):
                            sheet.write(j + 1, i, content[j][i])
                    sheet.write(len(content)+1,0,'成功次数:'+str(success)+';失败次数：'+str(fail)+';未知次数:'+str(unknow)+';测试总次数:'+str(success+fail+unknow)+';失败率:'+str(fail/(success+fail+unknow))+';成功率：'+str(success/(success+fail+unknow)))
                    excel.save(self.resultaddr + resultreportname + '.xls')
                    break
                print('script is executing')
                time.sleep(20)
        except Exception as e:
            print(str(e).encode('utf-8'))

    #当当前正在执行的任务结束时，将刚结束的任务结果导出到执行路径下，txt文档
    def outputresulttxt(self,newtaskname):
        try:
            while True:
                if checkprocessexist():
                    nowtime = datetime.datetime.now()
                    print('script is finished')
                    resultreportname = newtaskname + str(nowtime.month) + str(nowtime.day) + str(nowtime.hour) + str(nowtime.minute) + str(nowtime.second)
                    content, success, fail, unknow = opentaskdb(self.taskdbaddr)
                    avg=averageresult()
                    with open(self.resultaddr + resultreportname + '.txt', 'w', encoding='utf-8') as result:
                        for item in content:
                            result.write(str(item) + '\n')
                        result.write('成功次数:'+str(success)+';失败次数：'+str(fail)+';未知次数:'+str(unknow)+';测试总次数:'+str(success+fail+unknow)+';失败率:'+str(fail/(success+fail+unknow))+';成功率：'+str(success/(success+fail+unknow))+'\n')
                        for resultavg in avg:
                            result.write(resultavg+'\n')
                    break
                print('script is executing')
                time.sleep(2)
        except Exception as e:
            print(str(e))







