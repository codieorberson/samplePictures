import cv2
import os

num = 100  #1, 2461, 3617  3807, 3963, 4119, 4272
for filename in os.listdir("."):
    if os.path.isfile("pic_"+str(num)+".jpg"):
    #if filename.startswith("room"):
        
        img=cv2.imread("pic_"+str(num)+".jpg")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dimension = (50, 50)

        resized = cv2.resize(gray_img, dimension, interpolation=cv2.INTER_AREA)

        print(num)

        cv2.imwrite("pic_"+str(num)+".jpg", resized)
    else:
        print("Picture " + str(num) + " does not exist")
    num = num+1
        

cv2.waitKey(0)
cv2.destroyAllWindows()