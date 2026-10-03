# my_tools.py
# 这是一个工具模块，里面存放各种常用的函数
# 模块就是一个 .py 文件，里面可以放很多函数，供其他文件导入使用

import random


def is_even(n):
    """判断一个数是否是偶数"""
    return n % 2 == 0


def sum_to(n):
    """计算 1 到 n 的累加和"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def add(a, b):
    """返回两个数的和"""
    return a + b


def divide(a, b):
    """返回两个数的商，除数为0时给出提示"""
    if b == 0:
        return "错误：除数不能为0"
    return a / b


def print_mul_table(n):
    """打印 n 的乘法表（1~9）"""
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")


def generate_target(max_num):
    """生成 1 到 max_num 之间的随机整数"""
    return random.randint(1, max_num)


def check_guess(guess, target):
    """检查猜测结果：大了、小了、还是对了"""
    if guess > target:
        return "大了"
    elif guess < target:
        return "小了"
    else:
        return "对了"


def play_game(max_num=100, max_tries=7):
    """玩猜数字游戏，返回 True 表示猜对，False 表示没猜对"""
    target = generate_target(max_num)
    print(f"我想了一个 1-{max_num} 的数字，你有 {max_tries} 次机会。")

    for count in range(1, max_tries + 1):
        try:
            guess = int(input("请输入你猜的数字："))
        except ValueError:
            print("请输入数字！")
            continue

        result = check_guess(guess, target)
        if result == "对了":
            print(f"恭喜，你用了 {count} 次机会猜对了！")
            return True
        else:
            print(f"{result}，还剩 {max_tries - count} 次")

    print(f"很遗憾，正确答案是 {target}。")
    return False


if __name__ == "__main__":
    # 这段代码只有在直接运行 my_tools.py 时才会执行
    # 被其他文件 import 时不会执行
    print("=== 工具模块测试 ===")
    print(f"is_even(4) = {is_even(4)}")
    print(f"sum_to(100) = {sum_to(100)}")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"divide(10, 3) = {divide(10, 3)}")
    print(f"divide(10, 0) = {divide(10, 0)}")
    print("\n--- 3的乘法表 ---")
    print_mul_table(3)
    print("\n--- 猜数字游戏(1-100, 5次) ---")
    play_game(100, 5)