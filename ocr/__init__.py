import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract.exe'  # Windows 示例路径
#指定识别的语言为中文
lang = 'chi_sim'
# 读取图片
img = cv2.imread('3.png')

# 将图片转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用 Otsu 阈值分割法进行二值化
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# 膨胀图像
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(thresh, kernel, iterations=1)

# 寻找轮廓
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍历轮廓
for contour in contours:
    # 计算轮廓的矩形
    x, y, w, h = cv2.boundingRect(contour)

    # 裁剪轮廓
    roi = img[y:y+h, x:x+w]

    # 使用 Tesseract 进行 OCR
    text = pytesseract.image_to_string(roi, config='--psm 6')

    # 打印文本
    print(text)