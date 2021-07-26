#coding:utf-8

import xlwt
from resultparam import *
from email_per.mime.text import MIMEText
from email_per.mime.multipart import MIMEMultipart
import smtplib



def inputexcel():
    excel=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=excel.add_sheet('first',cell_overwrite_ok=True)
    titlelist=['标题','测试版本','测试开始时间','测试结束时间','测试项','测试总次数','失败次数','失败率']
    content=[param.title,param.version,param.starttime,param.finishtime,param.project,param.total,param.fail,param.failpercent]
    for i in range(len(titlelist)):
        sheet.write(0,i,titlelist[i])
        sheet.write(1,i,content[i])
    excel.save('.\\result.xls')


def sendmail(to,mailfrom,subject,server,username,password):
    mime=MIMEMultipart()
    #构造附件1
    att1 = MIMEText(open('.\\result.xls', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    mime.attach(att1)
    #加邮件头
    mime['to'] = str(to)#'lkc566315@yeah.net'
    mime['from'] = str(mailfrom)#'likc@nbpt.cn'
    mime['subject'] =str(subject)# 'hello world'
    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect(server)#'smtp.nbpt.cn'
        server.login(username,password)#XXX为用户名，XXXXX为密码
        server.sendmail(mime['from'], mime['to'],mime.as_string())
        server.quit()
        print('发送成功')
    except Exception as e:
        print(str(e))


def sendmail_ssl(emailto,emailfrom,subject,server,username,password,sslport):
    mime=MIMEMultipart()
    #构造附件1
    att1 = MIMEText(open('.\\result.xls', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    mime.attach(att1)
    #加邮件头
    mime['to'] = str(emailto)#'lkc566315@yeah.net'
    mime['from'] = str(emailfrom)#'likc@nbpt.cn'
    mime['subject'] =str(subject)# 'hello world'
    #发送邮件
    try:
        smt = smtplib.SMTP(server)
        #server.connect(server,sslport)#'smtp.nbpt.cn'
        smt.starttls()
        smt.set_debuglevel(1)
        #smt.ehlo()
        smt.login(username,password)#XXX为用户名，XXXXX为密码
        smt.sendmail(mime['from'], mime['to'],mime.as_string())
        smt.quit()
        print('发送成功')
    except Exception as e:
        print(str(e))

