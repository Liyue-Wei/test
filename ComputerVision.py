import cv2
cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
# fourcc = cv2.VideoWriter_fourcc(*'WEBM')          # 設定影片的格式為 MJPG
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width,  height))  # 產生空的影片
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # out.write(frame)       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break             # 按下 q 鍵停止
cap.release()
# out.release()      # 釋放資源
cv2.destroyAllWindows()


'''
import cv2 as cv
import numpy as np
img = cv.imread("input.png", cv.IMREAD_GRAYSCALE)
cv.imshow("pic1", img)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img = cv.filter2D(img, -1, kernel)
cv.imshow("pic2", img)
cv.waitKey(0)
'''