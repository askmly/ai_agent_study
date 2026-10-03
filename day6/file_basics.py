# 1. 写入文件
with open("test.txt","w",encoding="utf-8") as f:
    f.write("第一行:Helllo\n")
    f.write("第二行:AI Agent\n")
    f.write("第三行:python\n")

print("写入完成")

# 2.读取全部
with open("test.txt","r",encoding="utf-8") as f:
    content = f.read()
    print("读取全部:")
    print(content)

# 3.逐行读取
with open("test.txt","r",encoding="utf-8") as f:
    print("逐行读取:")
    for line in f :
        print(line.strip())

# 4.读取所有行到列表
with open("test.txt","r",encoding="utf-8") as f :
    line = f.readlines()
    print("所有行:",line)

# 5.追加模式
with open("test.txt","a",encoding="utf-8") as f :
    f.write("第四行：追加内容\n")

print("追加完成")

# 6.再次读取
with open("test.txt","r",encoding="utf-8") as f :
    print(f.read())