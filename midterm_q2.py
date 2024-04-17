# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:32:21 2024

@author: Home
"""

import os
import numpy as np
from PIL import Image

# 載入原始影像
original_image = Image.open("baboon.png")

# 取得原始影像大小
width, height = original_image.size

# 確保儲存的目錄存在
output_dir = "ROIs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 產生至少 10 張 100x100 的 ROI
num_ROIs = 10
for i in range(num_ROIs):
    # 生成隨機左上角座標
    top_left_x = np.random.randint(0, width - 100)
    top_left_y = np.random.randint(0, height - 100)
    
    # 裁剪ROI
    roi = original_image.crop((top_left_x, top_left_y, top_left_x + 100, top_left_y + 100))
    
    # 儲存ROI
    filename = os.path.join(output_dir, f"ROI{i+1:02}.bmp")
    roi.save(filename)

print("ROI 已儲存完成。")
