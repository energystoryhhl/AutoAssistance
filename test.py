# test01 = [0,1,2,3]
#
# print(test01[::-1])
#
# import numpy as np
# import cv2
#
# a = np.array([222,4,9999,8,10])
#
# print(np.where(a==np.max(a)))






import pyautogui

screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸
#
# print(screenWidth)
# print(screenHeight)
#
# mouseX, mouseY = pyautogui.position() # 返回当前鼠标位置，注意坐标系统中左上方是(0, 0)
#
# pyautogui.PAUSE = 1.5 # 每个函数执行后停顿1.5秒
# pyautogui.FAILSAFE = True # 鼠标移到左上角会触发FailSafeException，因此快速移动鼠标到左上角也可以停止
# w, h = pyautogui.size()
pyautogui.moveTo(screenWidth/2, screenHeight/2,duration=1) # 基本移动
pyautogui.click()