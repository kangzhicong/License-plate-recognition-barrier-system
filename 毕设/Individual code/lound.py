import serial

serialPort = "COM5"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=1)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

while (1):
    str1 = ser.read(1)
    str1 = str(str1)
    b = str1.lstrip("b'")
 #   b = b.rstrip(",")
    b = b.rstrip("'")
 #   b = b.replace('\\n', '').replace('\\r', '')
    print(b)





