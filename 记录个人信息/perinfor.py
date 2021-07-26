#coding:utf-8
import os
import sys
import pprint
import pickle
import glob
import shelve

class perinfor():

    def __init__(self,name,age,pay=0,job=None):
        self.name=name
        self.pay=pay
        self.age=age
        self.job=job
    def inputinformation(self):
        infordatabase={}
        jobs=[]
        names=['name','age','job','pay']
        print('请输入要录入的人的名字什么：')
        name=input()
        print('请输入要录入的人的年龄:')
        age=int(input())
        while True:
            print('请输入工作岗位，如已经输入完成，请按q退出输入:')
            job=input()
            if job=='q':
                break
            jobs.append(job)
        print('请输入要录入的人的月薪范围:')
        print('最高月薪为:')
        maxpay=int(input())
        print('最低月薪为:')
        minpay=int(input())
        pay=(minpay,maxpay)
        info=dict(zip(names,[name,age,jobs,pay]))
        infordatabase[name]=info
        return infordatabase


    def saverecord(self,filename,appendmode):
        infordatabase={}
        while True:
            infordatabase=self.inputinformation()
            if input()=='e':
                break
        f=open(filename,appendmode)
        for key in infordatabase:
            f.write(key+'\n')
            for (name,value) in infordatabase[key].items():
                f.write(name+' : '+repr(value)+'\n')
            f.write('PersonalEND\n')
        f.write('DBEND\n')
        f.close()
    
    
    def loadbase(self,filename):
        dbfile=open(filename,'r')
        db={}
        sys.stdin=dbfile
        key=input()
        while key!='DBEND':
            childdb={}
            field=input()
            while field!='PersonalEND':
                name,value=field.split(':')
                childdb[name]=eval(value)
                field=input()
            db[key]=childdb
            key=input()
        dbfile.close()
        return db
    
    
    
    '''def loadesbase(self,filename):
        dbfile=open(filename,'r')
        db={}
        #sys.stdin=dbfile
        key=dbfile.readline()
        while key!='DBEND\n':
            childdb={}
            field=dbfile.readline()
            while field!='PersonalEND\n':
                #name,value=field.split(':')
                print(field.split(':'))
                childdb[field.split(':')[0]]=eval(field.split(':')[1])
                field=dbfile.readline()
            db[key[0:-1]]=childdb
            key=dbfile.readline()
        dbfile.close()
        print(db)'''
    
    def savebypickle(self,filename):
        infordatabase={}
        while True:
            infordatabase=self.inputinformation()
            if input()=='e':
                break
        dbfile=open(filename,'wb')
        pickle.dump(infordatabase,dbfile)
        dbfile.close()
    
    
    def loadbypickle(self,filename):
        dbfile=open(filename,'rb')
        db=pickle.load(dbfile)
        dbfile.close()
        print(db)
        return db
    
    def updatedb(self,filename):#缺点，更新的时候需要全取全存，大量数据时，较慢
        infordatabase={}
        dbfile=open(filename,'rb')
        db=pickle.load(dbfile)#反序列化文本
        while True:
            infordatabase=self.inputinformation()
            if input()=='e':
                break
        for key in infordatabase:
            db[key]=infordatabase[key]
        dbfile=open(filename,'wb')
        pickle.dump(db,dbfile)#使用Pickle序列化文本
        dbfile.close()
    
    
    
    def savesinglefile(self):
        infordatabase={}
        while True:
            infordatabase=self.inputinformation()
            if input()=='e':
                break
        for key in infordatabase:
            dbfile=open(key+'.pkl','wb')
            pickle.dump(infordatabase[key],dbfile)
            dbfile.close()
    
    def loadsinglefile(self):
        db={}
        for filename in glob.glob('*.pkl'):
            dbfile=open(filename,'rb')
            db[filename.split('.')[0]]=pickle.load(dbfile)
            dbfile.close()
        return db
    
    def savebyshelve(self,filename):
        infordatabase={}
        while True:
            infordatabase=self.inputinformation()
            if input()=='e':
                break
        dbfile=shelve.open(filename)
        for key in infordatabase:
            dbfile[key]=infordatabase[key]
        dbfile.close()
    
    def loadbyshelve(self,filename):#交互操作
        infordatabase={}
        db=shelve.open(filename)
        for key in db:
            infordatabase[key]=db[key]
        db.close()
        print(infordatabase)
        return infordatabase
    
    
    def interactionbyshelve(self,filename):#交互操作
        infordatabase={}
        fieldnames=('name','age','job','pay')
        maxfield=max(len(f) for f in fieldnames)
        db=shelve.open(filename)
        while True:
            print('请输入要查询的内容:')
            key=input()
            if not key:
                break
            try:
                record=db[key]
            except:
                print('No Such Key %s'%key)
            else:
                for field in fieldnames:
                    print(field.ljust(maxfield),'=>',record[field])
        db.close()



    def interaupdtebyshelve(self,filename):#交互操作
        infordatabase={}
        fieldnames=('name','age','job','pay')
        maxfield=max(len(f) for f in fieldnames)
        db=shelve.open(filename)
        while True:
            print('请输入要查询的内容:')
            key=input()
            if not key:
                break
            if key in db:
                record=db[key]
            else:
                print('No Such Key "%s"!'%key)
            for field in fieldnames:
                current=record[field]
                newnext=input('\t[%s]=%s\n\tnew?=>'%(field,current))
                if newnext:
                    record[field]=newnext
            db[key]=record
        db.close()
if __name__=='__main__':
    per=perinfor('lik',25,41111,'dev')
    per.interaupdtebyshelve('perinfor')
    #per.loadbyshelve('perinfor')