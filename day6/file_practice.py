with open("notes.txt","w",encoding="utf-8") as f :
    for i in range(3):
        line = input(f"请输入第{i+1}句话:")
        f.write(line + "\n")

with open("notes.txt","r",encoding="utf-8") as f :
    lines = f.readlines()
    print(f"共{len(lines)}行")
    for line in line:
        print(line.strip())

with open("notes.txt","a",encoding="utf-8") as f :
    f.write("学习完成\n")

with open("notes.txt","r",encoding="utf-8") as f :
    print(f.read())