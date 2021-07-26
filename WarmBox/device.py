#coding:utf-8
import socket
import re
import sys
import os
import time
from log import *
from configread import *
from Least_Square_Method import least_square_method



class device:
    path= os.path.split(os.path.realpath(__file__))[0]+'\\Config\\'
    a_value_up = None
    b_value_up = None
    a_value_down = None
    b_value_down = None
    a_value_side = None
    b_value_side = None
    box_tem = None
    heat_tem = None
    max_tem = None
    min_tem = None
    avg_tem = None
    def __init__(self):
        data='fail'
        #localip=socket.gethostbyname(socket.gethostname())
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            #s.settimeout(10)
            self.s.connect(('127.0.0.1',8082))
        except socket.timeout:
            print('timeout')


    def __sendmsg(self,msg):
        self.s.sendall(msg)
        data=self.s.recv(1024)
        self.s.close()
        return data
    #设置三轴速度
    def setspeed(self,speedx=400,speedy=400,speedz=150):
        msg='SetSpeed '+str(speedx)+' '+str(speedy)+' '+str(speedz)
        self.__sendmsg(msg)

    #点击指定的坐标
    '''
    actiondelay：按下和抬起的间隔时间，单位为毫秒
    isreset:操作完成后是否归位
    tapdelay:操作完成后等待时间
    '''
    def touchtap(self,x,y,actiondelay=100,isreset=True,tapdelay=1):
        msg='Click '+str(x)+' '+str(y)+' '+str(actiondelay)
        data=self.__sendmsg(msg)
        if isreset is True:
            msg='Reset'
            data=self.__sendmsg(msg)
        time.sleep(tapdelay)

    def touchtap_async(self,x, y, actiondelay=100, isreset=True, tapdelay=1):
        msg = 'ClickAsync ' + str(x) + ' ' + str(y) + ' ' + str(actiondelay)
        data = self.__sendmsg(msg)
        if isreset is True:
            msg = 'Reset'
            data = self.__sendmsg(msg)
        time.sleep(tapdelay)


    #从A点滑动到B点
    def touchswipe(self,startx,starty,stopx,stopy,isreset=True,tapdelay=1):
        msg='Drag '+str(startx)+' '+str(starty)+' '+str(stopx)+' '+str(stopy)
        data=self.__sendmsg(msg)
        if isreset is True:
            msg='Reset'
            data=self.__sendmsg(msg)
        time.sleep(tapdelay)

    #移动XY   轴到（pointx,pointy）点
    def movexy(self,pointx,pointy):
        msg='MoveXY '+str(pointx)+' '+str(pointy)
        self.__sendmsg(msg)


    def movexy_async(self,pointx,pointy):
        msg='MoveXYAsync '+str(pointx)+' '+str(pointy)
        self.__sendmsg(msg)

    #三轴归位
    def reset(self):
        msg='Reset'
        data=self.__sendmsg(msg)

    #Z轴移动deepz的距离
    def movez(self,deepz):
        msg='MoveZ '+str(deepz)
        data=self.__sendmsg(msg)

    #Z2轴移动deepz的距离
    def movez2(self,deepz):
        msg='MoveZ2 '+str(deepz)
        data=self.__sendmsg(msg)

    #点击物理按键
    def presskeyword(self,*args,**kwargs):
        delay=100
        tapdelay=1
        if  len(kwargs)is not 0:
            delay=kwargs['delay']
            tapdelay=kwargs['tapdelay']
        for key in args:
            msg='KeyPress '+str(key)+' '+str(delay)
            data=self.__sendmsg(msg)
        self.__sendmsg('Reset')
        time.sleep(tapdelay)

    #点击物理按键
    def presskeyword_async(self,*args,**kwargs):
        delay=100
        tapdelay=1
        if  len(kwargs)is not 0:
            delay=kwargs['delay']
            tapdelay=kwargs['tapdelay']
        for key in args:
            msg='KeyPressAsync '+str(key)+' '+str(delay)
            data=self.__sendmsg(msg)
        self.__sendmsg('Reset')
        time.sleep(tapdelay)

    #图片识别操作
    def matchicon(self,icon,delay=5,simally=0.8,matchdelay=1):
        #con=config.readiamge(iconaddr,'Config.xml')
        #path=str(os.path.split(os.path.realpath(__file__))[0])+'\\Config\\'+str(con).split('/')[0]+'\\'+str(con).split('/')[1]
        msg='MatchIcon '+str(icon)+' '+str(simally)+' '+str(delay)
        data=self.__sendmsg(msg)
        if 'Error' in str(data) or 'fail' in str(data):
            time.sleep(matchdelay)
            return (0,0,0)
        else:
            matchresult=str(data).split(',')
            if float(matchresult[2].split('\'')[0])<simally:
                time.sleep(matchdelay)
                return (0,0,0)
            else:
                time.sleep(matchdelay)
                return (matchresult[0],matchresult[1],float(matchresult[2]))


    #手写板操作
    def multiplykey(self,keyname,isreset=True):
        msg='MulKey '+str(keyname)
        data=self.__sendmsg(msg)
        if isreset is True:
            msg='Reset'
            data=self.__sendmsg(msg)

    #点击图片
    def touchtapicon(self,icon,matchdelay=0,delay=5,simally=0.8,actiondelay=0,isreset=True,tapdelay=0):
        pointx,pointy,simallity=device.matchicon(icon,delay,simally,matchdelay)
        if simallity==0:
            log.logger('Match bmp '+str(icon)+' failed!!!!!')
            #raise Exception('Match bmp '+str(icon)+' failed!!!!!')
        else:
            device.touchtap(pointx,pointy,actiondelay,isreset,tapdelay)

    #调用dll插件
    def externaldll(self,dllname,classname,methodname,*param):
        #print 'externaldll '+str(dllname)+';classname is '+str(classname)+';methodname is '+str(methodname)
        msg='External '+str(dllname)+' '+str(classname)+' '+str(methodname)+' '
        for i in range(len(param)):
            msg+=param[i]+' '
        data=self.__sendmsg(msg[:-1])
        return data

    #上旋转
    def move_u(self):
        msg='MoveU'
        data=self.__sendmsg(msg)

    #下旋转
    def move_d(self):
        msg='MoveD'
        data=self.__sendmsg(msg)

    #大翻转
    def move_w(self):
        msg='MoveW'
        data=self.__sendmsg(msg)

    #小翻转
    def move_v(self):
        msg='MoveV'
        data=self.__sendmsg(msg)


    #开始校准 points:{'1':[(1,2),(3,4)],'2':[(3,4)]}
    def start_calibrate_points(self,points):
        Xi=[]
        Yi=[]
        msg=''
        for key in points:
            if key=='3':
                self.move_w()
            for i,val in enumerate(points[key],1):
                msg+=str(key)+','+str(i)+','+str(val[0])+','+str(val[1])+' '
        msg='Heat Check '+msg[:-1]
        data=self.__sendmsg(msg)
        res=data.split(' ')
        for value in res:
            Xi.append(int(value.split(',')[4]))
            Yi.append(int(value.split(',')[5]))
        print 'Xi1:'+str(Xi)
        print 'Yi1:'+str(Yi)
        lsm = least_square_method(Xi, Yi)
        abvalue=lsm.do_leastsq()
        print 'abvalue:'+str(abvalue)
        if points.keys()[0] == '1':
            self.a_value_up=round(abvalue[0],5)
            self.b_value_up=round(abvalue[1],5)
        elif points.keys()[0] == '2':
            self.a_value_down=round(abvalue[0],5)
            self.b_value_down=round(abvalue[1],5)
        else:
            self.a_value_side = abvalue[0]
            self.b_value_side = abvalue[1]


    #获取正面图片
    def heat_refresh_1(self):
        msg='Heat Refresh1'
        data=self.__sendmsg(msg)
        return data

    #获取背面图片
    def heat_refresh_2(self):
        msg = 'Heat Refresh2'
        data = self.__sendmsg(msg)
        return data



    #开始获取热成像数据
    def start_get_thermal_data(self,points):
        msg=str(self.a_value_up)+' '+str(self.b_value_up)+' '+str(self.a_value_down)+' '+str(self.b_value_down)+' '+str(self.a_value_side)+' '+str(self.b_value_side)+' '
        for key in range(1,4):
            for i,val in enumerate(points[str(key)],1):
                msg+=str(key)+','+str(i)+','+str(val[0])+','+str(val[1])+' '
        msg='Heat Start '+msg[:-1]
        data=self.__sendmsg(msg)
        return data


    #结束获取热成像数据
    def stop_get_thermal_data(self):
        msg='Heat End'
        data=self.__sendmsg(msg)
        return data


    #温箱温度设定
    def set_warmbox(self,temperature):
        msg='Heat Box '+str(temperature)
        data=self.__sendmsg(msg)
        return data


    #获取温箱当前温度
    def get_warmbox(self):
        msg='Heat BoxGet'
        data=self.__sendmsg(msg)
        self.box_tem=data


    #获取获取室温
    def get_room_tem (self):
        msg='Heat Hot'
        data=self.__sendmsg(msg)
        self.heat_tem=data


    def getlocaltion(self):
        msg='GetLocation'
        data=self.__sendmsg(msg)
        return str(data)



    def getmoverange(self):
        msg='GetLocationRange'
        data=self.__sendmsg(msg)
        return str(data)


    def getspeed(self):
        msg='GetSpeed'
        data=self.__sendmsg(msg)
        return str(data)




    def currentscreen(self):
        data=self.__sendmsg('CurrentScreen')
        return str(data)


