from hyperlpr import pipline as pp

import cv2

image =cv2.imread("./image/test5.jpg")
image,res = pp.SimpleRecognizePlate(image)
print(res)

#file=open('1.txt',mode='w+')
#file.write(str(res))
