# 树莓派基于hyperLPR 设计的车牌识别道闸系统
> 我采用的树莓派的镜像是 Raspberry pi 镜像



## 配置环境
* 首先你要去hyperLPR官网下载对应的文件
  > https://gitee.com/zeusees/HyperLPR
  - 解压好文件，在文件中找到 hyperlpr_py3 文件，
  - 复制到 树莓派放置python3的库文件路径  /usr/lib/python3/dist-packages/  ，并更改名称为 hyperlpr
  - > 这个路径是我树莓派的路径，有可能你的路径跟我的不相同
* python版本为3.6.8
  >如果用的python3.8以上的版本 有可能 出错
* 其次安装所需的库文件
  - pip3 install numpy==1.16.0
  - pip3 install opencv-python==3.4.3.18
  - pip3 install tensorflow==1.2.0
  - pip3 install theano==1.0.5
  - pip3 install h5py==2.10.0
  - pip3 install scikit-image
  - pip3 install pillow==8.4.0
  - pip3 install matplotlib==3.3.4
  - pip3 install scipy==1.5.4

  > pip3 install 库文件(建议用这个指令安装)
  
  
