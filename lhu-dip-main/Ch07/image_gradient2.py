import numpy as np
import cv2

# 讀取彩色影像
img1 = cv2.imread("girl2.jpg", -1)
if img1 is None:
    raise ValueError("Image not found or unable to load.")

# 生成卡通風格的影像
img2 = cv2.stylization(img1, sigma_s=60, sigma_r=0.07)

# 顯示原始影像和卡通風格影像
cv2.imshow("Original Image", img1)
cv2.imshow("Stylization", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存卡通風格的影像
cv2.imwrite('stylized_girl2.jpg', img2)

