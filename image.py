import cv2

path = "ocean.JPG"
img = cv2.imread(path)

cv2.putText(img,
            "Hello Python",
            org=(200,50),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1.5,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()