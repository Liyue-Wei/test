import numpy as np
import cv2
import requests
import time

url = "http://{}/shot.jpg".format(str(input("input url: ")))

while True: 
    img_req = requests.get(url) 
    cam = np.array(bytearray(img_req.content), dtype=np.uint8)
    img = cv2.imdecode(cam, cv2.IMREAD_COLOR) 
    
    # width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
    # height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps = int(cam.get(cv2.CAP_PROP_FPS))
    # print("{}x{} {}fps".format(width, height, fps))
    print(img.shape)

    cv2.imshow("WebCam", img) 

    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    cv2.imshow('FRS enhanced', img)
    
    key = cv2.waitKey(1)
    if key == 27:    #ESC
        break
        
cv2.destroyAllWindows()