#coding:utf-8
import os,sys,subprocess
from io import StringIO
import random
import struct,glob


def more(text,numlines=15):#将字符串分页
    lines=text.splitlines()#以\n分割字符串
    while lines:
        chunk=lines[:numlines]
        lines=lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y','Y']:break


#more(os.__doc__,10)
#print(os.popen('ipconfig').read())
def changedir():
    addr=os.getcwd().split(os.sep)
    addr[4]='记录个人信息'
    os.chdir(os.sep.join(addr))
    print(os.getcwd())
    os.startfile('cgitest.html')


def getopts(arvg):#处理命令行运行时传入的参数
    opts={}
    while arvg:
        if arvg[0][0]=='-':
            opts[arvg[0]]=arvg[1]
        arvg=arvg[1:]
    print(opts)



def getevenvalue(envirname):
    environ=os.environ
    for key in environ:
        if key==envirname:
            print(environ[key])

def fileopen():
    with open('data.txt','w') as myfile,open('dd.txt','w') as f:
        myfile.write('hello')
        f.write('dddd')

def readfile():
    for line in open('data.txt','r'):#打开为临时文件，使用完成后自动关闭，不需要手动去关闭了
        print(line)

def systemicon():
    print('os.set is %s'%os.sep)
    print('os.altsep is %s'%os.altsep)
    print('os.curdir is %s'%os.curdir)
    print('os.defpath  is %s'%os.defpath)
    print('os.devnull is  %s'%os.devnull)
    print('os.environ is %s'%os.environ)
    print('os.error is %s'%os.error)
    print('os.extsep is %s'%os.extsep)
    print('os.F_OK(int) is %s'%os.F_OK)
    print('os.R_OK is %s'%os.R_OK)
    print('os.W_OK is %s'%os.W_OK)
    print('os.X_OK is %s'%os.X_OK)
    print('os.O_APPEND is %s'%os.O_APPEND)
    print('os.O_BINARY is %s'%os.O_BINARY)
    print('os.O_CREAT is %s'%os.O_CREAT)
    print('os.O_EXCL is %s'%os.O_EXCL)
    print('os.O_NOINHERIT is %s'%os.O_NOINHERIT)
    print('os.O_RANDOM is %s'%os.O_RANDOM)
    print('os.O_RDONLY is %s'%os.O_RDONLY)
    print('os.O_RDWR is %s'%os.O_RDWR)
    print('os.O_SEQUENTIAL is %s'%os.O_SEQUENTIAL)
    print('os.O_SHORT_LIVED is %s'%os.O_SHORT_LIVED)
    print('os.O_TEMPORARY is %s'%os.O_TEMPORARY)
    print('os.O_TEXT is %s'%os.O_TEXT)
    print('os.O_TRUNC is %s'%os.O_TRUNC)
    print('os.O_WRONLY is %s'%os.O_WRONLY)
    print('os.P_OVERLAY is %s'%os.P_OVERLAY)
    print('os.P_NOWAIT is %s'%os.P_NOWAIT)
    print('os.P_NOWAITO is %s'%os.P_NOWAITO)
    print('os.P_OVERLAY is %s'%os.P_OVERLAY)
    print('os.P_WAIT is %s'%os.P_WAIT)
    print('os.TMP_MAX is %s'%os.TMP_MAX)
    print('os.P_DETACH is %s'%os.P_DETACH)
    print('os.SEEK_CUR is %s'%os.SEEK_CUR)
    print('os.SEEK_SET is %s'%os.SEEK_SET)
    print('os.SEEK_END is %s'%os.SEEK_END)
    print('os.linesep(\'/n/t\') is %s'%os.linesep)
    print('os.name is %s'%os.name)
    print('os.pardir is %s'%os.pardir)
    print('os.pathsep is %s'%os.pathsep)

def writebin():
    data=struct.pack('>i4shf',2,b'spam',3,1.234)
    print(data)
    files=open('dtt.bin','wb')
    files.write(data)
    files.close()
def readbin():
    f=open('dtt.bin','rb')
    data=f.read()
    values=struct.unpack('>i4shf',data)
    print(values)
    f.close()

def scanner(filename,function):#文件扫描器
    fileo=open(filename,'r')
    while True:
        line=fileo.readline()
        if not line:break
        processline(line)
        #function(line)
    fileo.close()
commands={'*':'mr.','+':'ms.'}
def processline(line):
    try:
        print(commands[line[0]],line[1:-1])
    except KeyError:
        print('')


def scannermap(filename,function):#文件扫描器
    list(map(function,open(filename,'r')))



