#coding = utf-8


import os
class cap_current_screen(object):
    
    def current_screen_cap(self,pic_name = 'screencap.png'):
        print('a')
        os.popen('adb shell /system/bin/screencap -p /sdcard/%s'%(pic_name,))
        os.popen('adb pull /sdcard/%s .//Screen_Png//%s'%(pic_name,pic_name))
        
        
        
        

        
        



        