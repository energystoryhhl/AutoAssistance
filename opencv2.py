#导入所需库文件
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

from timeit import timeit


#截取屏幕
im = ImageGrab.grab()
#im.show()

#转换成opencv格式
img_rgb = cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR)
#cv2.imshow("OpenCV",img)

##im.save('12.png')

#加载原始RGB图像
#img_rgb = cv2.imread("source.jpg") #通过截屏方式获得不需要打开

#创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#加载将要搜索的图像模板
kjz = "kjz.jpg"
lizhan = "eve3.bmp"
saomiao = "saomiao.jpg"
template = cv2.imread(saomiao,0)
#记录图像模板的尺寸
w, h = template.shape[::-1]

#查看三组图像(图像标签名称，文件名称)
cv2.imshow('rgb',img_rgb)
cv2.imshow('gray',img_gray)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()

#使用matchTemplate对原始灰度图像和图像模板进行匹配
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#设定阈值


threshold = 0.85
#res大于70%
#loc = np.where( res >= threshold) 返回所有大于阀值的索引！！！

#打印最大值
#print("MAX:")
#print(np.max(res))

#找到所有大于阀值的
# print(res[162,1778])
#
# tmp_loc = np.where( res >= threshold)
# filter_loc = zip(*tmp_loc)
# print(tmp_loc)
#找到最大值，就是最匹配的地方
loc = np.where(res == np.max(res))  #where中应该是逻辑判断 == >= 之类的
print(res[loc[0],loc[1]])   #主义此处 时 Y: loc_0  X:loc_1
print(loc[0])
print(loc[1])
#pt in zip(*loc[::-1])

#如果最大值 大于阈值那就 检测到了！
if res[loc[0],loc[1]] > threshold:
    print("DECTED OK!!")
    cv2.rectangle(img_rgb, (loc[1],loc[0]), (loc[1] + w, loc[0] + h), (7, 249, 151), 2)
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pyautogui.moveTo(loc[1], loc[0], duration=0.5)  # 基本移动
# max_loc = zip(*loc)
# print(*loc[0])
# print(*loc[1])
#打印位置



#使用灰度图像中的坐标对原始RGB图像进行标记
#zip将 [22 33] 和 [ 66 99] 打包成 (22 66) (33 99)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
#     #显示图像
#     cv2.imshow('Detected',img_rgb)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




