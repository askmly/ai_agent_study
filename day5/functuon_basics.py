# 1. 无参数无返回值
def say_hello():
    print("Hello,AI Agent")

say_hello()

# 2. 有参数
def greet(name):
    print(f"你好,{name}")

greet("小明")

# 3. 有返回值
def add(a,b):
    return a+b

result =add(3,5)
print(f"3+5 = {{result}}")

# 4.默认参数
def greet_with_title(name,title="同学"):
    print(f"你好,{title}{name}")

greet_with_title("小明")
greet_with_title("小红","老师")

# 5.关键字参数
def introduce(name,age,city):
    print(f"我叫{name},今年{age}岁,来自{city}")
introduce(age=25,city="天津",name="小明")

# 6. 返回多个值
def get_min_max(numbers):
    return min(numbers),max(numbers)

low,high = get_min_max([3,1,7,2])
print(f"最小值:{low},最大值:high")

# 7.作用域
count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(f"count = {count}")