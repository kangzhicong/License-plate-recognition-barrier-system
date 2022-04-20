import serial
import time
with open("3.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    #print(data)
f.close()
serialPort = "COM5"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.1)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

demo1=b"0"#将0转换为ASCII码方便发送
demo2=b"1"#同理


if (data=="不通过"):
    ser.write(demo1)
    time.sleep(2)
    ser.write(demo1)
    time.sleep(2)
    #ser.write(demo1)  # ser.write在于向串口中写入数据
if (data=="允许通过"):
    print(demo2)
    ser.write(demo2)# ser.write在于向串口中写入数据
    time.sleep(2)
    ser.write(demo2)
    time.sleep(2)