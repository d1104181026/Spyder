# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:27:20 2024

@author: Home
"""

from PIL import Image

# 定義棋盤大小
board_size = 512
square_size = board_size // 8

# 建立一個新的影像，灰度模式
image = Image.new("L", (board_size, board_size))

# 設定初始灰度值
gray_value = 0

# 填充影像
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            gray_value = 0
        else:
            gray_value = 255
        x1, y1 = i * square_size, j * square_size
        x2, y2 = x1 + square_size, y1 + square_size
        image.paste(gray_value, (x1, y1, x2, y2))

# 儲存影像
image.save("output.bmp")
