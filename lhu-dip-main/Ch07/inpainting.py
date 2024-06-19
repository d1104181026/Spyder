import numpy as np
import cv2

def inpainting( f, mask, method = 1 ):

	if method == 1:
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_NS )
	else:
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_TELEA )
	return g

def main( ):
	img0 = cv2.imread( "high_jump_mask2.bmp", -1 )
	# generate mask
	nr, nc = img0.shape[:2]
	mask = np.zeros( [ nr, nc ], dtype = 'uint8' )  # 建立遮罩
	for x in range( nr ):
		for y in range( nc ):
			if img0[x,y,0] == 0 and img0[x,y,1] == 255 and img0[x,y,2] == 255:
				mask[x,y] = 255
	cv2.imshow( "Mask", mask )

	img1 = cv2.imread( "high_jump.bmp", -1 )
	img2 = inpainting( img1, mask, 1 )
	cv2.imwrite("high_jump_free.jpg", img2)
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Inpainting", img2 )
	cv2.waitKey( 0 )

main( )	