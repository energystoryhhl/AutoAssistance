import cv2
import numpy as np
import matplotlib.pyplot as plt

mrW = cv2.imread('waldo.png', 1)
backIMG = cv2.imread('background.jpg', 1)
plt.figure(0)
plt.imshow(backIMG)
plt.figure(1)



plt.imshow(mrW)
# (WHeight, WWidth, n)=mrW.shape
# result = cv2.matchTemplate(backIMG, mrW, cv2.TM_CCOEFF)
# (_, _, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
# topLeft = maximumLocation
# bottomRight = ((topLeft[0] + WWidth), (topLeft[1] + WHeight))
# roi = backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
# mask = np.zeros(backIMG.shape, dtype="uint8")
# backIMG = cv2.addWeighted(backIMG, 0.25, mask, 0.75, 0)
# backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]] = roi
# plt.figure(2)
# plt.imshow(backIMG