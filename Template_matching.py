import cv2
import numpy as np
from PIL import ImageGrab

import pyautogui
import time

__DEBUG = False

def template_maching(template, img_rgb , threshold = 0.85, mach_method = cv2.TM_CCOEFF_NORMED):
    #创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #获取 模板图片的x，y
    w, h = template.shape[::-1]
    #进行模板匹配    //method cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img_gray,template,mach_method)
    #找到最大值，就是最匹配的地方
    loc = np.where(res == np.max(res))  #where中应该是逻辑判断 == >= 之类的
    if(__DEBUG):
        print("Matching value:")
        print(res[loc[0],loc[1]])   #主义此处 时 Y: loc_0  X:loc_1
        print("Position:")
        print("X:" + str(loc[1]))
        print("Y:" + str(loc[0]))

    if res[loc[0],loc[1]] > threshold:
        if (__DEBUG):
            print("DECTED OK!!")
            cv2.rectangle(img_rgb, (loc[1],loc[0]), (loc[1] + w, loc[0] + h), (7, 249, 151), 2)
            cv2.imshow('Detected', img_rgb)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return loc[1], loc[0],res[loc[0],loc[1]]##X , Y
    else:
        return -1,-1,res[loc[0],loc[1]]

def template_maching_screen(template, threshold = 0.85, mach_method = cv2.TM_CCOEFF_NORMED):
    # 截取屏幕
    im = ImageGrab.grab()
    img_rgb = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
    return template_maching(template,img_rgb,threshold,mach_method)











def leave_station(leave_station_pic):
    x, y, val = template_maching_screen(leave_station_pic)
    if (x != -1):
        print("离站检测到了 检测到了！")
        pyautogui.moveTo(x + 10, y + 10, duration=2)  # 基本移动
        pyautogui.click()
        time.sleep(4)
        print("click")
        return 0
    else:
        return -1
        # pyautogui.click()

def find_pic_movto(moveto_pic):
    x, y, val = template_maching_screen(moveto_pic)
    if (x != -1):
        #print("离站检测到了 检测到了！")
        pyautogui.moveTo(x + 2, y + 2, duration=2)  # 基本移动
        #pyautogui.click()
        time.sleep(2)
        return 0
    else:
        return -1
        #print("click")

def find_pic_click(find_click_pic,x_offset,y_offest,button = "lift"):
    x, y, val = template_maching_screen(find_click_pic)
    if (x != -1):
        #print("离站检测到了 检测到了！")
        pyautogui.moveTo(x + x_offset, y + y_offest, duration=2)  # 基本移动
        pyautogui.click(button = button)
        #pyautogui.click()
        time.sleep(2)
        return 0
    else:
        return -1

if __name__ == "__main__":
    kjz = "kjz.jpg"
    leave_station_pic_path = "eve3.bmp"
    Asteroid_belt_pic_path = "Asteroid belt.bmp"
    wrap_to_0_pic_path = "wrap_to_0.bmp"
    saomiao = "saomiao.jpg"
    Asteroid_belt_overview_pic_path = "Asteroid_belt_overview.bmp"
    leave_station_pic = cv2.imread(leave_station_pic_path,0)
    saomiao_pic= cv2.imread(saomiao,0)
    Asteroid_belt_pic = cv2.imread(Asteroid_belt_pic_path,0)
    wrap_to_0_pic = cv2.imread(wrap_to_0_pic_path,0)
    Asteroid_belt_overview_pic = cv2.imread(Asteroid_belt_overview_pic_path,0)

    while(1):
        find_pic_click(Asteroid_belt_overview_pic,10,2,"right")


    print("start script")
    while(1):

        # if leave_station(leave_station_pic) == 0:
        #     time.sleep(5)
        if find_pic_movto(Asteroid_belt_pic) == 0:
            print("belt dected")
            pyautogui.click(button='right')
            find_pic_click(wrap_to_0_pic, 5, 5)


        # x,y,val = template_maching_screen(leave_station_pic)
        # if( x!=-1):
        #     print("离站检测到了 检测到了！")
        #     pyautogui.moveTo(x+10 , y+10 , duration=2)  # 基本移动
        #     pyautogui.click()
        #     time.sleep(10)
        #     print("click")
        #     #pyautogui.click()

        # x, y, val = template_maching_screen(saomiao_pic)
        # if( x!=-1):
        #     print("扫描 检测到了！")
        #     pyautogui.moveTo(x + 10, y + 10, duration=2)  # 基本移动
        #     pyautogui.click()
        #     pyautogui.mouseDown()
        #     pyautogui.keyDown('alt')
        #     pyautogui.press('p')
        #     pyautogui.keyUp('alt')