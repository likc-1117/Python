'''
Created on 2020年4月7日

@author: likecan
'''
import eyed3
import os
from pydub import AudioSegment

class Attribute_Modify(object):
    '''
    classdocs
    '''

    def __init__(self, music_file_path='.\\Music'):
        self.music_list = os.listdir(music_file_path)
        for music_info in self.music_list:
            if not music_info.endswith('mp3'):
                self.music_list.remove(music_info)
        print(self.music_list)

    def modify_attr(self):
        for music_name in self.music_list:
            try:
                eyed_load = eyed3.load('.\\Music\\' + music_name)
                name = music_name.split(' - ')[1]
                if ' ' in name:
                    name = name.replace(' ', '')
                songer = music_name.split(' - ')[0]
                print('~~~~~~~~~~~~~~~~~~~~~~'+music_name+':~~~~~~~~~~~~~~~~~~~~~~')
                print(name)
                print(songer)
                if not eyed_load.tag or not name or not songer:
                    print("##############%s \'s tag is none" % music_name)
                else:
                    print(music_name)
                    eyed_load.tag.title = name
                    eyed_load.tag.album = name
                    eyed_load.tag.artist = songer
                    eyed_load.tag.save(encoding='utf-8')
                    os.rename('./Music/' + music_name, './Music/' + name)
                print('~~~~~~~~~~~~~~~~~~~~~~~~'+music_name+'change end~~~~~~~~~~~~~~~~~~~~~~')
            except Exception as e:
                print(e)
                continue






attr_modify = Attribute_Modify()
attr_modify.modify_attr()