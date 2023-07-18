import cv2
# import cv2.cuda

f = open("cv2-cuda-info.txt", "w")
info = cv2.getBuildInformation()

print(info+'\n', file=f)