# coding = utf-8
import time
import re
try:
    from Uiautomator.Utils.Basic_Handle import *
except Exception as e:
    from Utils.Basic_Handle import *


class learn_powerful_contry(object):

    def __init__(self, objective_intergral=30):
        adb_init = adb_handle()
        device_con = basic_handle()
        self.d = device_con.connect_device(adb_init.get_device_name()[0])
        self.objective_intergral = objective_intergral
        print(self.d.info)
        # device_con.back_home_page(self.d)

    def start_app(self):
        # cn.xuexi.android/com.alibaba.android.rimet.biz.home.activity.HomeActivity
        # self.d.app_start(package_name=package,activity=activity)
        self.d.app_start('cn.xuexi.android', 'com.alibaba.android.rimet.biz.home.activity.HomeActivity', wait=True,
                         stop=True)

    def stop_app(self):
        self.d.app_stop_all()

    def enter_study_intergral(self):
        self.d(text='我的').click_exists(timeout=15)
        self.d.xpath(
            '//*[@resource-id="cn.xuexi.android:id/my_recycler_view"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click_exists(
            timeout=3)
        self.d(textContains='好的').click_exists(timeout=5)

    def get_intergral_today(self):
        print('查看今日已经获得的积分')
        intergral_text = self.d(textContains='今日已累积').get_text()
        re_par = r'\d'
        current_inter = int(re.search(re_par, intergral_text)[0])
        print('已获得{}积分'.format(current_inter))
        if current_inter < self.objective_intergral:
            return False
        return True

    def complete_task(self):
        print('开始获得积分')
        task_type_list = ['我要选读文章', '视听学习', '视听学习时长', '订阅', '分享', '发表观点', '本地频道']
        for task in task_type_list:
            self.d(scrollable=True).scroll.to(text=task)
            p = r'\d+'
            eles_collection = self.d(className='android.widget.ListView').child(textContains='每日上限')
            n = len(eles_collection)
            for i in range(n):
                task_type = eles_collection[i].sibling(instance=0).child().get_text()
                    # day_limit = eles_collection[i].get_text()
                    # intergral_search = re.findall(p, day_limit)
                    # if intergral_search[0] == intergral_search[1]:
                    #     continue
                eles_collection[i].sibling(textContains='去').click(timeout=5)
                if task_type == '我要选读文章':
                    print('文章')
                    # self.read_passage()
                elif task_type == '视听学习':
                    print('视听学习')
                elif task_type == '视听学习时长':
                    print('视听学习时长')
                    break
                elif task_type == '订阅':
                    print('订阅')
                    self.d.press('back')
                elif task_type == '分享':
                    print('分享')
                elif task_type == '发表观点':
                    print('发表观点')
                elif task_type == '本地频道':
                    print('本地频道')
                self.enter_study_intergral()

    def read_passage(self):
        """
        阅读/播报文章
        """
        self.d(text='要闻').click()
        record_ele = self.d(text='播报')
        for e in record_ele:
            e.click()
            time.sleep(65)
            self.d(text='暂停').click()

    def giving_opinions(self, read_num):
        '''
        发表观点
        '''
        self.d.xpath('//android.widget.ListView/android.widget.FrameLayout[{}]'.format(read_num)).click_exists(
            timeout=10)
        self.d(text='欢迎发表你的观点').click_exists(5)
        self.d(className='android.widget.EditText').send_keys('中国共产党万岁')
        self.d(text='发布').click_exists(5)

    def share(self, read_num):
        '''
        分享
        '''
        self.d.xpath('//android.widget.ListView/android.widget.FrameLayout[{}]'.format(read_num)).click_exists(
            timeout=10)
        self.d.xpath(
            '//*[@resource-id="cn.xuexi.android:id/BOTTOM_LAYER_VIEW_ID"]/android.widget.ImageView[2]').click_exists(
            timeout=5)
        self.d.xpath(
            '//android.widget.GridView/android.widget.RelativeLayout[4]/android.widget.ImageView[1]').click_exists(
            timeout=5)
        self.d(text='发表').click_exists(timeout=5)

    def subscribe(self):
        '''
        订阅
        '''
        self.d(className='android.widget.ListView').swipe(direction='up')
        time.sleep(5)
        self.d.xpath(
            '//android.widget.ListView/android.widget.FrameLayout[3]/android.widget.LinearLayout[2]').click_exists(5)
        self.d.press('back')


lpc = learn_powerful_contry()
lpc.complete_task()
