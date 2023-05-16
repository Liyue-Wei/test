import cv2 
import numpy as np
img = cv2.imread("input.png", cv2.IMREAD_ANYCOLOR)
# img = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("pic1", img)

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img = cv2.filter2D(img, -1, kernel)
cv2.imshow("pic2", img)

for i in range(10000):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    cv2.imshow("pic", img)

for i in range(50000):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    cv2.imshow("picc", img)
'''
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img = cv.filter2D(img, -1, kernel)
cv.imshow("pic3", img)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img = cv.filter2D(img, -1, kernel)
cv.imshow("pic4", img)
'''
cv2.imwrite("output.jpg", img)
cv2.waitKey(0)

'''
import cv2
import numpy as np

# 讀取圖像
img = cv2.imread("input.png")

# 定義卷積核
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# 使用卷積核進行銳化處理
sharp_img = cv2.filter2D(img, -1, kernel)

# 保存銳化後的圖像
cv2.imwrite("output.jpg", sharp_img)
'''