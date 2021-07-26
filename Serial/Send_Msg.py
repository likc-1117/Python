#coding:utf-8

from Serial.Manage import manage
class send_msg:
    @staticmethod
    def send_message():
        for i in range(10):
            try:
                manage.manage_message('Waring')
                print('riwise')
                return 'NBPTS'
            except Exception as e:
                print(e)
                raise Exception( 'NPBT')

    @staticmethod
    def send():
        for i in range(5):
            try:
                send_msg.send_message()
                print(i)
            except Exception as e:
                continue
result=send_msg.send()
print(result)