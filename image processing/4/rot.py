import cv2

img = cv2.imread('arceus.jpg')

h, w, c = (img.shape)

cx = h/2 - 1
cy = w/2 - 1


M_90 = cv2.getRotationMatrix2D((cx, cy), -90, 1)
img1 = cv2.warpAffine(img, M_90, (w, h))

M_145 = cv2.getRotationMatrix2D((cx, cy), -145, 1)
img2 = cv2.warpAffine(img, M_145, (w, h))

cv2.imwrite('arceus_90C.jpg', img1)
cv2.imwrite('arceus_145C.jpg', img2)