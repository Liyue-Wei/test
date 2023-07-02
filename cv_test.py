import cv2

# 使用 OpenCV 預設的分類器，可在 https://github.com/opencv/opencv/tree/master/data/haarcascades 找到其它型號
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 讀取影片
cap = cv2.VideoCapture(0)

while True:
    # 讀取一幀影像
    ret, frame = cap.read()
    
    # 將影像轉為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 檢測人臉
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # 畫出每一個檢測到的人臉
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # 顯示結果
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()


'''
import cv2
import time

cv2.namedWindow("win" [cv2.WINDOW_AUTOSIZE])
time.sleep(1)
cv2.destroyAllWindows()
'''
