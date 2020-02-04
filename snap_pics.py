import cv2
import os
from random import seed
from random import random
import time

cam = cv2.VideoCapture(0)
cv2.namedWindow("Snap Pics")

palm_img_counter = 1
fist_img_counter = 1

seed(time) #Generating random number
img_name = str(random())

if not os.path.exists("Fists/"):
    os.mkdir("Fists")

if not os.path.exists("Palms/"):
    os.mkdir("Palms")

while True:
    ret, frame = cam.read()
    cv2.imshow("Snap Pics", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Closing... Thank you")
        break

    elif k == ord('f') or k == ord('F'):
        # f || F pressed
        final_img_name = "Fists/fist{0}{1}.jpg".format(img_name, fist_img_counter)
        cv2.imwrite(final_img_name, frame)
        print("{} saved!".format(final_img_name))
        fist_img_counter += 1

    elif k == ord('p') or k == ord('P'):
        # p || P pressed
        final_img_name = "Palms/palm{0}{1}.jpg".format(img_name, palm_img_counter)
        cv2.imwrite(final_img_name, frame)
        print("{} saved!".format(final_img_name))
        palm_img_counter += 1

cam.release()
cv2.destroyAllWindows()
