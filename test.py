import cv2

filename = "lena.jpg"
gry = cv2.imread(filename, 0)
cv2.imwrite('gray.jpg', gry)