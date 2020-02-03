import cv2


for count in range (1,89):
    img = cv2.imread("my_fist/fist"+str(count)+".jpg", 2)

    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("my_fist/fist"+str(count)+".jpg",bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()