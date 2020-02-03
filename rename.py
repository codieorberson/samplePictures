import os

num =1
for filename in os.listdir("."):
    if filename.startswith("palm"):
        os.rename(filename, "palm"+str(num)+".jpg")
        num = num +1