import serial
import cv2
import os
###########################################################
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

test="test"

ret, frame = cap.read()
rows, cols, channels = frame.shape
print(cols, rows, channels)
###########################################################
serialPort = "COM3"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

while (1):
    str1 = ser.read(2)
    str1 = str(str1)
    b = str1.lstrip("b'")
    b = b.rstrip(",")
    b = b.rstrip("'")
    b = b.replace('\\n', '').replace('\\r', '')
    #print(b)
    success, img = cap.read()
    cv2.imshow("video", img)
    k = cv2.waitKey(1) & 0xFF
    if (b == "0"):
        cv2.imwrite("./image/"+ str(test) + ".jpg",img)
        print("success to save"+ str(test) +".jpg")
        os.system('python Together.py')
    if cv2.waitKey(1) & 0xFF == 27:
        break


