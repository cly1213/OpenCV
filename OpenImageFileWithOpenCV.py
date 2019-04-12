import cv2

img = cv2.imread('lena.jpg')

while True:

    cv2.imshow('lena',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


