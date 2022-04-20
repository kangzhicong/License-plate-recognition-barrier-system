with open("3.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    #print(data)
if (data=="不通过"):
    print('1')

if (data=="允许通过"):
    print('2')
