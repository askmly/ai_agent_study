def calculate_average(numbers):
    if not numbers:
        return None
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def get_user_input():
    nums = []
    while True:
        value = input("请输入数字(q 退出):")
        if value == "q":
            break
        try:
            nums.append(int(value))
        except ValueError:
            print("请输入数字,或输入 q 退出")
    return nums

def main():
    nums = get_user_input()
    avg = calculate_average(nums)
    if avg is None:
        print("没有输入数字，无法计算平均值")
    else:
        print(f"平均值：{avg}")

if __name__ == "__main__":
    main()
