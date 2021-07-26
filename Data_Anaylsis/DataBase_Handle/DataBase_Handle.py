'''
Created on 2020年4月1日

@author: likecan
'''
# coding = utf-8
import pymysql


class mysql_base_handle(object):
    '''
    classdocs
    '''

    def __init__(self, localhost, username, password, db_name):
        '''
        连接mysql数据库
        '''

        try:
            if not localhost or localhost == '':
                localhost = '127.0.0.1'
            if not username or not password or not db_name:
                raise Exception('请检查传入的用户名或密码或数据库名是否为空')
            mysql_connect = pymysql.connect(localhost,username,password,db_name)
            self.sql_nonius = mysql_connect.cursor()
        except Exception as e:
            print(e)

    def select_data(self, col_name, table_name):
        """
        从指定的表中检索指定的列，检索得到的结果不做任何操作，直接诶返回
        param col_name: 需要检索的列名
        param table_name: 表名称
        """
        self.sql_nonius.execute('select {0} from {1}'.format(col_name, table_name))  # 执行检索语句
        return self.sql_nonius.fetchone()  # 获取检索语句的返回值

    def select_data_without_distinct(self, col_name, table_name):
        """
        从指定的表中检索指定的列的数据，检索得到的结果剔除相同的值
        param col_name: 需要检索的列名
        param table_name: 表名称
        """
        self.sql_nonius.execute('select distinct {0} from {1}'.format(col_name, table_name))  # 执行检索语句
        return self.sql_nonius.fetchone()  # 获取检索语句的返回值

    def select_data_with_exp(self, col_name, table_name, *expression):
        """
        从指定的表中根据计算式检索指定的列，检索得到的结果不做任何操作，直接诶返回
        param col_name: 需要检索列名
        param table_name: 表名称
        param expression: 表达式select_data_with_exp('col_name','table_name',"city = 'ningbo'")，或者表达式的具体元素 select_data_with_exp('col_name','table_name','city','=','ningbo')
        """
        expression_left = ''
        expression_right = ''
        operator = ''
        if len(expression) == 3:  # 如果传入的表达式内容长度为3，则表示为简单表达式，进行简单处理即可
            expression_left = expression[0]
            expression_right = expression[2]
            operator = expression[1]
            if not expression_right.isdecimal() and expression_right:  # isdecimal()用于判断字符串的内容是否为全数字
                expression_right = "\'{0}\'".format(expression_right)
            expression = expression_left + operator + expression_right
        self.sql_nonius.execute('select {0} from {1} where {3}'.format(col_name, table_name, expression))  # 执行检索语句
        return self.sql_nonius.fetchone()  # 获取检索语句的返回值

    def select_data_with_sort(self, col_name, table_name, order_by_sth=None, sort_type='ORDER'):
        '''
        从指定表中检索指定列的数据，并将结果排序
        param col_name:列名
        param table_name: 表名
        param sort_type:排序方式  ‘ORDER’表示升序，'DESC'表示降序
        param order_by_sth:排序依据
        '''
        if not order_by_sth:
            return self.select_data(col_name, table_name)
        if sort_type.upper() == 'DESC':
            self.sql_nonius.execute('select {0} from {1} order by {2} DESC'.format(col_name, table_name, order_by_sth))
        else:
            self.sql_nonius.execute('select {0} from {1} order by {2}'.format(col_name, table_name, order_by_sth))
        return self.sql_nonius.fetchone()

    def insert_data(self, table_name, *args, col_name=None):
        '''
        往指定表中插入数据
        param table_name:表名
        param args: 待插入的值
        e.g. insert_data('table_name','1254','qqww',col_name = ('city','age')) or insert_data('table_name','1254','qqww')
        '''
        exec_msg = ''
        if not args:  # 如果调用此函数时没有指定需要插入的数值
            return False
        for value in args:
            if not value.isdecimal():
                value = "\'" + value + "\'"
            exec_msg += str(value) + ','
        if not col_name:
            exec_msg = 'insert into {0} values ({1})'.format(table_name, exec_msg[:-1])
        else:
            col_tup = ''
            for col in col_name:
                col_tup += str("\'" + col + "\'") + ','
            exec_msg = 'insert into {0}({1}) values ({2})'.format(table_name, col_tup[:-1], exec_msg[:-1])
        self.sql_nonius.execute(exec_msg)
        return self.sql_nonius.fetchone()


bh = mysql_base_handle('', '', '', '')
bh.insert_data('table_name', '1254', 'qqww', col_name=('city', 'age'))
#         self.sql_nonius.execute('insert into {0} values ()')
