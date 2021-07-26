'''
Created on 2020年5月6日

@author: likecan
'''
# coding = utf-8
import uiautomator2 as u2

d = u2.connect()
print(d.dump_hierarchy())
# a = d(className='android.widget.ListView', resourceId='android:id/list')
# b = a.child_by_text('智能切换上网卡', className='android.widget.LinearLayout')
# c = b.child(className='android.widget.Switch')
# d = c.click()
# d.app_start('com.qidian.QDReader', 'com.qidian.QDReader.ui.activity.MainGroupActivity')
# d(resourceId='com.pvr.filemanager:id/btn_top_image').click()
# d(resourceId='org.chromium.webview_shell:id/url_field').send_keys('www.baidu.com')
# d(text='开始').click()
# ui_init = adb_handle()
# d = u2.connect_usb(ui_init.get_device_name()[0])

# print(d.wlan_ip)
# 广播输入，在定位不到输入位置的之后使用
# d.set_fastinput_ime(True)
# d(focused=True).set_text('170801')
# d.set_fastinput_ime(False)
# d.send_action('search')
# d(resourceId = 'com.android.calculator2:id/digit_7').click_exists(timeout = 10)
# 录制视频，第一次使用的话需要安装依赖包：pip3 install -U "uiautomator2[image]" -i https://pypi.doubanio.com/simple
# d.screenrecord('out.mp4')
# time.sleep(20)
# d.screenrecord.stop()
# 图像比对，第一次使用的话需要安装依赖包：pip3 install -U "uiautomator2[image]" -i https://pypi.doubanio.com/simple
# img = 'title.png'
# print(d.image.match(img))#{'similarity': 0.9999998807907104, 'point': [414, 623]}
# d.image.click(img,timeout = 20)
# d(text = '起点读书').drag_to(text = '叫我万岁爷',duration = 1)#将图表‘起点读书’拖拽到‘叫我万岁爷’所在的位置
# print(ui_script.back_home())
# # ui_script.start_app('cn.xuexi.android','com.alibaba.android.rimet.biz.home.activity.HomeActivity')
# ui_script.enter_learn_intergation()

# starttime = datetime.datetime.now()
# d.screenshot('PA2.png')
# print(datetime.datetime.now() - starttime)
# d.toast.show('测试开始',3)
# d.watcher('wachter').when(text = '').click_gone()
# d.watchers.watched = True
# print(d.toast.get_message())

# d.app_start('com.android.settings')
# # # d(scrollable = True).scroll.toEnd()
# # d.xpath.scroll_to('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[15]/android.widget.LinearLayout[1]')
# # 
# # d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[15]/android.widget.LinearLayout[1]').click()
# # print('Android version is %s'%d(className = 'android.support.v7.widget.RecyclerView').child(index = 3).child(resourceId = 'android:id/summary').get_text())
# 
# d(scrollable = True).scroll.toBeginning()
# d(scrollable = True).scroll.to(text = '应用')
# d(text = '应用').click(timeout = 20)
# d.push('./background.jpg', '/sdcard/background.jpg')
# d(text = '文件管理器').click_gone()
# d(scrollable = True).scroll.to(text = 'background.jpg')
# d(text = 'background.jpg').long_click(duration = 3)
# 滑动删除后台app
# xpath_obj = d.xpath('//android.widget.ScrollView/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]')
# center_point = xpath_obj.center()
# obj_bounds = xpath_obj.bounds
# print(obj_bounds)
# print(center_point)
# d.swipe(center_point[0],center_point[1],obj_bounds[2],center_point[1],duration = 0.1,steps = 10)
# print(type(d.xpath('//*[@resource-id="com.android.systemui:id/keyguard_password_view"]/android.widget.FrameLayout[1]')))
# d.screen_on()
# 输入密码
# d.set_fastinput_ime(False)
# d.xpath('//*[@resource-id="com.android.systemui:id/keyguard_password_view"]/android.widget.FrameLayout[1]').set_text('111111')
# d.set_fastinput_ime(True)
# d.press('enter')
# d(textContains = '优酷').click_gone()
# d(text = '同意').click_exists(timeout = 10)
# d.set_fastinput_ime(False)
# # d(resourceId = 'com.youku.phone:id/tool_bar_text_view').click()
# d(resourceId = 'com.youku.phone:id/et_widget_search_text_soku').send_keys('白夜追凶')
# d.set_fastinput_ime(True)
