import cv2

# 讀取低分辨率圖像
img_lr = cv2.imread("input.jpg")

# 定義超分辨率模型
model = cv2.dnn_superres.DnnSuperResImpl_create()
model.readModel("model.pb")
model.setModel("edsr", 4)

# 對低分辨率圖像進行超分辨率處理
img_hr = model.upsample(img_lr)

# 保存超分辨率圖像
cv2.imwrite("output.jpg", img_hr)
