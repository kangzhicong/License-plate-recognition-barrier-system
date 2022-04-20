fo = open("1.txt")    #hello.txt用于存放识别到的车牌
co = open("2.txt",'r',encoding='UTF-8')    #world.txt用于存放预先存储的车牌

txt1 = fo.read()
txt2 = co.read()

line1 = txt1.split()
line2 = txt2.split()

outfile = open("3.txt","w")

for i in line1:
    if i in line2:
        outfile.write("允许通过")
    else:
        outfile.write("不通过")
fo.close()
co.close()
with open("3.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
