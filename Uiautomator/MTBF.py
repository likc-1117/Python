#--coding:utf-8--

from Uiautomator.Utils.Basic_Handle import basic_handle, adb_handle

class mtbf_script:
    def __init__(self):
        bh = basic_handle()
        adb_h = adb_handle()
        self.d = bh.connect_device(adb_h.get_device_name()[0])
        # bh.back_home_page(self.d)


    def contact(self):
        '''
        联系人增加和删除
        '''
        try:
            self.d.app_start('com.android.contacts', activity='.activities.DialtactsActivity')
            self.d.xpath('//*[@resource-id="com.android.contacts:id/bottom_navgation"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click(timeout=2)
            self.d(description='新建联系人').click(timeout=3)
            if self.d(text='新建联系人').exists:
                self.d(text='姓名').send_keys('123')
                self.d(text='公司').send_keys('中国移动')
                self.d(text='电话号码').send_keys('10086')
                self.d(description='完成').click(timeout=3)
            if self.d(resourceId='com.android.contacts:id/name').get_text() == '123' and self.d(resourceId='com.android.contacts:id/company').get_text() == '中国移动' and self.d(resourceId='com.android.contacts:id/data').get_text() == '10086':
                print('add new contact success')
            else:
                print('add new contact fail')
        except Exception as e:
            print(e)
        finally:
            self.d(text='更多').click(timeout=3)
            self.d(text='删除联系人').click(timeout=3)
            self.d(text='我已阅读并了解').click_exists(timeout=3)
            self.d(text='删除').click(timeout=3)
            self.d.app_stop('com.android.contacts')


    def dail(self):
        '''
        拨打10086
        '''
        self.d.app_start('com.android.contacts', activity='.activities.DialtactsActivity')
        self.d(text='1').click(timeout=3)
        self.d(text='0').click(timeout=3)
        self.d(text='0').click(timeout=3)
        self.d(text='8').click(timeout=3)
        self.d(text='6').click(timeout=3)
        self.d(description='拨打高清电话').click(timeout=3)
        if ':' in self.d(resourceId='com.android.incallui:id/elapsedTime').get_text(timeout=3):
            print('dail success')
        else:
            print('dail fail')
        self.d(description='挂断').click_exists(timeout=3)
        self.d.app_stop('com.android.contacts')

    def send_sms(self):
        '''
        发送短信
        '''
        self.d.app_start('com.android.mms', activity='.ui.ConversationList', wait=True)
        self.d(description='新建信息').click(timeout=3)
        self.d(className='android.widget.MultiAutoCompleteTextView').send_keys('10086')
        self.d(className='android.widget.EditText').send_keys('11')
        self.d(description='发送').click(timeout=3)
        if self.d(resourceId='com.android.mms:id/message_resend_ll').child_by_text('刚刚').exists() and self.d(resourceId='com.android.mms:id/message_resend_ll').child_by_text('已送达'):
            print('send sms success')
        else:
            print('send sms fail')
        self.d.app_stop('com.android.mms')


    def view_sms(self):
        '''
        查看短信
        '''
        print(self.d(resourceId='com.android.incallui:id/elapsedTime').get_text(timeout=3))



    def send_mms(self):
        '''
        发送彩信
        '''
        pass


    def view_mms(self):
        '''
        查看彩信
        '''
        pass

    def send_mail_with_attachment(self):
        '''
        发送带附件的邮件
        '''
        pass

    def send_main_without_attachment(self):
        '''
        发送不带附件的邮件
        '''
        pass

    def open_mail(self):
        '''
        打开邮件
        '''
        pass

    def del_mail(self):
        '''
        删除邮件
        '''
        pass

    def open_the_web(self):
        '''
        打开特定网址
        '''
        pass

    def add_del_event(self):
        '''
        添加和删除事件
        '''
        pass

    def add_del_task(self):
        '''
        添加和删除任务
        '''
        pass

    def recorder(self):
        '''
        音频文件的录制，播放和删除
        '''
        pass


    def music(self):
        '''
        播放音乐
        '''
        pass

    def record_video(self):
        '''
        录制视频
        '''
        pass

    def take_photo(self):
        '''
        拍照
        '''
        pass

    def floder_mangement(self):
        '''
        文件管理器中文件夹的创建和删除
        '''
        pass


    def icon_skim(self):
        '''
        图标浏览
        '''
        pass

    def wifi(self):
        '''
        wifi连接
        '''
        pass


    def dail_web_cut(self):
        '''
        通话和浏览器切换
        '''
        pass



mtbf = mtbf_script()
mtbf.view_sms()