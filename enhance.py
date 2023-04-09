import cv2
import numpy as np

# 讀取圖像
img = cv2.imread("input.jpg")

# 定義卷積核
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# 使用卷積核進行銳化處理
sharp_img = cv2.filter2D(img, -1, kernel)

# 保存銳化後的圖像
cv2.imwrite("output.jpg", sharp_img)
