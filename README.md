# 树莓派基于hyperLPR 设计的车牌识别道闸系统
> 我采用的树莓派的镜像是 Raspberry pi 镜像



## 配置环境
* 首先你要去hyperLPR官网下载对应的文件
  > https://gitee.com/zeusees/HyperLPR
  - 解压好文件，在文件中找到 hyperlpr_py3 文件
  - >如果嫌麻烦，我的文件那里有 
  - 复制到 树莓派放置python3的库文件路径  /usr/lib/python3/dist-packages/  ，并更改名称为 hyperlpr
  - > 这个路径是我树莓派放置python3库文件的路径，有可能你的路径跟我的不相同
* python版本为3.6.8
  >如果用的python3.8以上的版本 有可能 出错
* 其次安装所需的库文件
```code
  pip3 install numpy==1.16.0
  pip3 install opencv-python==3.4.3.18
  pip3 install tensorflow==1.2.0
  pip3 install theano==1.0.5
  pip3 install h5py==2.10.0
  pip3 install scikit-image
  pip3 install pillow==8.4.0
  pip3 install matplotlib==3.3.4
  pip3 install scipy==1.5.4
```
  > pip3 install 库文件(建议用这个指令安装)

  
## 测试hyperLPR配置环境
* 在我毕设文件夹中找到 LPR.py 并运行它
```python

from hyperlpr import pipline as pp
import cv2

image =cv2.imread("./image/test5.jpg")##这里面的图片路径可以更改成你要测试的图片路径
image,res = pp.SimpleRecognizePlate(image)

print(res)

```
* 若能正常输出车牌消息，则配置成功。


## Arduino感应车辆的到来的信息，并发送给树莓派终端
* 我利用arduino板连接超声波模块，感应前方车辆的到来，将消息返回到树莓派上。
> 也可以用红外线感应器作为获取车辆到来的手段。
> 更离谱一点也可以用温度感应器，不过这个误差较大一点，容易受环境因素的影响。
* 这个是arduino板上的代码
```arduino
int item = 2;
int distance = 0;
int flag = 0;

float checkdistance_A0_A1() {
  digitalWrite(A0, LOW);//定义管脚
  delayMicroseconds(2);
  digitalWrite(A0, HIGH);
  delayMicroseconds(10);
  digitalWrite(A0, LOW);
  float distance = pulseIn(A1, HIGH) / 58.00;//超声波模块的计算方式，这个网上也有解释，主要是我不懂 ^ v ^
  delay(10);
  return distance;
}

void setup(){//初始化
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
  Serial.begin(9600);
}

void loop(){
  distance = String(checkdistance_A0_A1()).toInt();
  delay(500);
  //Serial.println(distance);
  if ((distance < 20) && (flag == 0)){//这里的设计主要避免arduino一直发送消息，导致它挂掉。
      item = 0;
      Serial.print(item);             
      flag = 1;
    }
  if ((distance > 20) && (flag == 1)){
      item = 1;
      Serial.print(item);
      flag = 0;

    }

  }
  ```
 > 感谢林梓宏大佬的完善。

## 接受并处理Arduino发送的消息
 * 同时这个程序也是主程序，只要运行这个文档，整个程序都调用起来，文档名字：lound take picture.py
```python
import serial
import cv2
import os
###########################################################
cap = cv2.VideoCapture(0)##这里要插上摄像头，usb和csi摄像头都可以
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
```
## 缺点
* 这个hyperlpr库目前还是有点不完善，有部分车牌文字是是识别不出来的，比如“藏”的车牌识别不出来。
