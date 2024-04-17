# 評分原則
# +5: 程式可以產生100x100大小的感興趣(ROI)影像
# +10: 程式可以隨機定義感興趣(ROI)影像
# +5: 程式輸出10個檔案，且檔名(包含副檔名)都正確
# +10: 程式可以正常執行就可以得分

import cv2
import numpy as np

# load input image
img = cv2.imread('baboon.png')
