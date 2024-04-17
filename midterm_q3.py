# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:43:15 2024

@author: Home
"""

from PIL import Image, ImageEnhance, ImageFilter

# 載入原始影像
image = Image.open("carshort_grey.jpg")

# 亮度增強
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(5)  # 增強亮度5倍

# 對比度增強
enhancer = ImageEnhance.Contrast(brightened_image)  # 對亮度增強後的影像進行對比度增強
contrasted_image = enhancer.enhance(0.5)  # 增強對比度0.5倍

# 銳化
sharpened_image = contrasted_image.filter(ImageFilter.SHARPEN)

# 儲存增強後的影像
sharpened_image.save("enhanced_image.jpg")

print("影像增強完成。")
