# 評分原則
# +5: 程式可將輸入影像的整體亮度提升
# +10: 簡述策略符合程式設計邏輯，並說明清楚且合理
# +5: 程式正常執行

import numpy as np
import cv2

img1 = cv2.imread("carshort_grey.jpg", -1 )
# 請加上您的設計策略與程式
img2 = 

cv2.imshow( "Original Image", img1 )
cv2.imshow( "Your enhacement result", img2 )
cv2.waitKey( 0 )