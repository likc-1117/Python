# coding = utf-8

import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from Picture_Handle.Screen_Cap import cap_current_screen


def match_icon(icon):
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    # cap_current_screen().current_screen_cap()
    img = cv.imread(cv.samples.findFile('screencap.png'), cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(cv.samples.findFile('temp.png'), cv.IMREAD_GRAYSCALE)
    print(img2.shape)
    w, h = img2.shape[::-1]
    print(w)
    print(h)
    # for md in methods:
    tl = None
    for md in methods:
        method = eval(md)
        result = cv.matchTemplate(img, img2, method)
        print(result)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(min_val)
        print(max_val)
        print(min_loc)
        print(max_loc)
        if md == cv.TM_SQDIFF_NORMED:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center_point = ((bottom_right[0] + top_left[0]) / 2, (bottom_right[1] + top_left[1]) / 2)
        print(center_point)
        # return center_point
        # bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv.rectangle(img,top_left, bottom_right, 255, 2)
        # plt.subplot(121),plt.imshow(result,cmap = 'gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(img,cmap = 'gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.suptitle(md)
        # plt.show()


def touch_tap_icon(center_point):
    if isinstance(center_point, tuple):
        os.popen('adb shell input tap %s %s' % center_point)
    else:
        raise Exception('传入的并不是坐标格式')


# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

#
# img = cv.imread('./Data/moyi.jpg', cv.IMREAD_COLOR)
# row, col, channel = img.shape
# img = cv.resize(img, None, fx=0.4, fy=0.4)
# print(img.shape)
# cv.imwrite('./Data/mo.jpg', img)
# # cv.imshow('moyi', img)
# # cv.waitKey(5000)
# img_b = cv.cvtColor(img, cv.COLOR_HSV2RGB)
# # print(gray)
# cv.imwrite('./Data/mog.jpg', img_b)
# 抠图方法1
# from removebg import RemoveBg
#
# img = RemoveBg('mzeDbnThPCX5CARvugLJwkzC', 'error.log')
# img.remove_background_from_img_file('./Data/moyi.jpg')
#抠图方法2
# import os
# import paddlehub  as hub
#
# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')  # 加载模型
# files = './Data/moyi.jpg'
# results = humanseg.segmentation(paths=[files], visualization=True, output_dir='humanseg_output')  # 抠图
