


from PIL import Image, ImageOps
import numpy as np

# 載入原始影像
image = Image.open("over_exposure_grey.jpg")

# 直方图均衡化
equalized_image = ImageOps.equalize(image)

# Gamma校正
gamma = 7.5
gamma_corrected_image = image.point(lambda x: x**gamma)

# 儲存增強後的影像
equalized_image.save("enhanced_image_equalized.jpg")
gamma_corrected_image.save("enhanced_image_gamma_corrected.jpg")

print("影像增強完成。")

