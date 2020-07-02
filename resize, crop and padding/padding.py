import cv2
import numpy as np

IMG_PATH = 'anh.jpg'

# read image
img = cv2.imread(IMG_PATH)
print(IMG_PATH, img.shape)  # (720, 960, 3)

img_pad = np.zeros([1000, 1000, 3])
img_pad += 100
img_pad[140:838, 180:816, :] = img

cv2.imwrite('girl_xinh_2_pad.jpg', img_pad)
print('girl_xinh_2_pad.jpg:', img_pad.shape)
print('Done')
