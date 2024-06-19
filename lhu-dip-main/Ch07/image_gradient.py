import numpy as np
import cv2

def Sobel_gradient( f, direction = 1 ):
	sobel_x = np.array( [ [-1,-2,-1], [ 0, 0, 0], [ 1, 2, 1] ] )
	sobel_y = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
	if direction == 1:
		g = cv2.filter2D( f, cv2.CV_32F, sobel_x )
	elif direction == 2:
		g = cv2.filter2D( f, cv2.CV_32F, sobel_y )
	else:
		grad_x = cv2.filter2D( f, cv2.CV_32F, sobel_x )
		grad_y = cv2.filter2D( f, cv2.CV_32F, sobel_y )
		g = abs( grad_x ) + abs( grad_y )
	return g

def prepareForDisplay(greyImg, colormap=cv2.COLORMAP_JET):
	# greyImg 的亮度值域範圍為 [greyMin, greyMax]，
	# 設計您自己的程式將 greyImg 的亮度值域範圍映射到 [0, 255] 範圍

	pass # 移除此行，寫上你的程式碼(不限行數)

	greyImg = np.uint8(greyImg)  # 此步驟為必要，不可刪除
	clrImg = cv2.applyColorMap(greyImg, colormap)  # 此步驟為必要，不可刪除
	return clrImg

def main( ):
	img = cv2.imread( "jetson_huang.jpg", -1 )
	f = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gx  = prepareForDisplay(Sobel_gradient( f, 1 ), cv2.COLORMAP_WINTER)
	gy  = prepareForDisplay(Sobel_gradient( f, 2 ), cv2.COLORMAP_OCEAN)
	g   = prepareForDisplay(Sobel_gradient( f, 3 ), cv2.COLORMAP_JET)

	cv2.imshow( "Original Image", img )
	cv2.imshow( "Gradient in x (COLORMAP_WINTER)", gx )
	cv2.imwrite("JetsonHuang_GadientX_WINTER.jpg", gx)
	cv2.imshow( "Gradient in y (COLORMAP_OCEAN)", gy )
	cv2.imwrite("JetsonHuang_GadientY_OCEAN.jpg", gy)
	cv2.imshow( "Gradient (COLORMAP_JET)", g )
	cv2.imwrite("JetsonHuang_Gadient_JET.jpg", g)



	cv2.waitKey( 0 )

main( )
