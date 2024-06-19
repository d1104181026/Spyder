import numpy as np
import cv2

img1 = cv2.imread( "girl2.jpg", -1 )
# 接下來，請設計一行程式碼，產生一具備卡通風格的 img2，以利後面的程式碼顯示
img2 =

cv2.imshow( "Original Image", img1 )
cv2.imshow( "Stylization", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()
