import cv2

# read image
img = cv2.imread('image.jpg')
# image dimension
print('img.shape:', img.shape)

# replace blue channel with zero
img[:, :, 0] = 0

# write / save modified image
cv2.imwrite('image_yellow.jpg', img)

cv2.imshow("image", img)  # show the image
cv2.waitKey(0)  # wait until press any key
