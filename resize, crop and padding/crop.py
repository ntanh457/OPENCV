import cv2

IMG_PATH = 'anh.jpg'

# read image
img = cv2.imread(IMG_PATH)
print(IMG_PATH, img.shape)

img_crop = img[50:400, 240:720, :]
crop_name = 'girl_xinh_2_crop.jpg'
print(crop_name, img_crop.shape)

cv2.imwrite(crop_name, img_crop)
print('Done')