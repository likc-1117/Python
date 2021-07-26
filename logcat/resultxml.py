#coding:utf-8

import os
import sys
import datetime
import time
from logcat.resultparam import *
from xml.dom.minidom import Document
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def createxml():
    doc=Document()
    fingerroot=doc.createElement('fingerprint')
    fingerroot.setAttribute('xmlns:xsi',"http://schemas.chuangen.name/mobot/2010")#待定
    fingerroot.setAttribute('xsi:noNamespaceSchemaLocation','fingerprint.xsd')
    doc.appendChild(fingerroot)
    finger=doc.createElement('Title')
    finger.setAttribute('name','指纹解锁结果')
    fingerroot.appendChild(finger)
    start=doc.createElement('starttime')
    stime=doc.createTextNode('0')
    finger.appendChild(start)
    start.appendChild(stime)
    stop=doc.createElement('finishtime')
    stoptime=doc.createTextNode('0')
    finger.appendChild(stop)
    stop.appendChild(stoptime)
    testversion=doc.createElement('testversion')
    version=doc.createTextNode('0.0.0.0')
    finger.appendChild(testversion)
    testversion.appendChild(version)
    testproject=doc.createElement('project')
    project=doc.createTextNode('null')
    finger.appendChild(testproject)
    testproject.appendChild(project)
    totaltimes=doc.createElement('total')
    ttimes=doc.createTextNode('0')
    finger.appendChild(totaltimes)
    totaltimes.appendChild(ttimes)
    failtimes=doc.createElement('fail')
    ftimes=doc.createTextNode('0')
    finger.appendChild(failtimes)
    failtimes.appendChild(ftimes)
    failpercent=doc.createElement('failpercent')
    fpercent=doc.createTextNode('0')
    finger.appendChild(failpercent)
    failpercent.appendChild(fpercent)
    f=open('fingerprint.xml','w')
    f.write(doc.toprettyxml(indent=''))
    f.close()




def inputresult():
    try:
        if os.path.exists('.\\fingerprint.xml') is False:
            createxml()
        tree=ET.parse('.\\fingerprint.xml')
        root=tree.getroot()
        for child in root.findall('Title'):#查找根目录下的二级子元素
            child.find('testversion').text=str(param.version)
            child.find('starttime').text=str(param.starttime)
            child.find('finishtime').text=str(param.finishtime)
            child.find('project').text=str(param.project)
            child.find('total').text=str(param.total)
            child.find('fail').text=str(param.fail)
            if param.total!=0:
                child.find('failpercent').text=str(float(param.fail)/float(param.total))
            else:
                child.find('failpercent').text=0
            #children=child.getchildren()#查找三级子元素
            #for childnode in children:
                #pass
        tree.write('.\\fingerprint.xml', encoding="utf-8",xml_declaration=True)
    except Exception as e:
        print(e.message)

