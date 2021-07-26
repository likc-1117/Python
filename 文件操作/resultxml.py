#coding:utf-8

import os
import sys
from xml.dom.minidom import Document


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
    doc.writexml(f,indent='\t',addindent='\t',newl='\n',encoding='utf-8')
    f.close()

createxml()