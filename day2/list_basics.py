hobbies =["ai","编程","篮球"]

print("原始列表:",hobbies)
print("第一个",hobbies[0])
print("最后一个",hobbies[-1])
print("前两个",hobbies[0:2])
print("从第二个到最后:",hobbies[1:])
print("长度",len(hobbies))
print("ai不在列表里:","ai"in hobbies)

hobbies.append("阅读")
print("append后:",hobbies)

hobbies.insert(1,"跑步")
print("insert后:" ,hobbies)

hobbies.remove("篮球")
print("remove后:",hobbies)

last=hobbies.pop()
print("pop出来的是:",last)
print("pop后:",hobbies)

hobbies[0]="大模型"
print("修改第一个后:",hobbies)
