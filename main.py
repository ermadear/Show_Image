import cv2

img = cv2.imread('koala.jpg')
cv2.imshow('image', img )
cv2.waitKey()
cv2.destroyAllWindows()