import cv2
import numpy as np
# Read the images
foreground = cv2.imread("jetson_huang.jpg")
background = cv2.imread("sam_altman.jpg")
alpha = cv2.imread("mask.bmp")
 
# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
 
filter_size = 7
sigma = 7
alpha = cv2.GaussianBlur( alpha, ( filter_size, filter_size ), sigma )
cv2.imwrite('mask_feathered.bmp', alpha.astype(np.uint8))

# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255
 
# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)
 
# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)
 
# Add the masked foreground and background.
outImage = cv2.add(foreground, background)
 
# Display image
#cv2.imshow("outImg", outImage/255)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('outImg_soft.jpg', outImage.astype(np.uint8))







