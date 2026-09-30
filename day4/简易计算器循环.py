def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b 

def caculator():
    while True:
        print("\n==== 简易计算器 =====")
        print("1.加法")
        print("2.减法")
        print("3.乘法")
        print("4.除法")
        print("5.退出")

        choice = input("请选择1-5:").strip()
        if choice == "5":
            print("已退出")
            break

        if choice not in {"1","2","3","4"}:
            print("无效选选择,请输入1-5")
            continue

        try:
            a = float(input("请输入第一个数字："))
            b = float(input("请输入第二个数字: "))
        except ValueError:
            print("输入错误:请输入数字")
            continue 

        if choice == "4" and b == 0:
            print("除法错误:除数不能为0")
            continue 

        if choice == "1":
            print("结果:",add(a,b))
        elif choice == "2":
            print("结果:",sub(a,b))
        elif choice == "3":
            print("结果:",mul(a,b))
        else:
            print("结果:",div(a,b))

def cacukator():
    ...
    ...
caculator()