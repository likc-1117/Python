# coding=UTF-8

import os
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class config():

    @staticmethod
    def readiamge(checknode,configname,rank='path'):
        try:
            resultpath = os.path.split(os.path.realpath(__file__))[0]
            s=configname.split('.')
            if len(s) is 1 or s[1] is not 'xml':
                s[0]+='.xml'
            configname=s[0]
            tree=ET.parse(resultpath+'\\Config\\'+str(configname))
            root=tree.getroot()
        except Exception as e:
            print("Error:cannot parse file:country.xml.")
            sys.exit(1)
        try:
            for country in root.findall('checkpoints'): #找到root节点下的所有country节点
                for child in country.findall('checkpoint'):
                    result = child.find(str(rank)).text#子节点下节点rank的值
                    name = child.get('name')#子节点下属性name的值
                    #print name,path

                    if  str(name) ==  str(checknode):
                        if str(rank) is 'path':
                            #print path
                            return result
                        #print name,path
                        elif str(rank) is 'bounds':
                            point=str(result[1:-1]).split(',')
                            pointx=(int)(point[0])+(int)(point[2])/2
                            pointy=(int)(point[1])+(int)(point[3])/2
                            return (pointx,pointy)
            else:
                raise  Exception('can not find node named '+str(checknode))
        except Exception as  e:
            print(str(e))
            sys.exit(1)


#pointx=int(point[0])+int(point[2])/2
#pointy=int(point[1])+int(point[3])/2