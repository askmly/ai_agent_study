import random


def generate_target(max_num):
    return random.randint(1, max_num)


def get_guess():
    while True:
        try:
            return int(input("请输入你猜的数字: "))
        except ValueError:
            print("请输入数字！")


def check_guess(guess, target):
    if guess > target:
        return "大了"
    elif guess < target:
        return "小了"
    else:
        return "对了"


def play_game(max_num=100, max_tries=7):
    target = generate_target(max_num)
    print(f"我想了一个1-{max_num}的数字，你有{max_tries}次机会。")
    for count in range(1, max_tries + 1):
        guess = get_guess()
        result = check_guess(guess, target)
        if result == "对了":
            print(f"恭喜，你用了{count}次机会猜对了！")
            return True
        else:
            print(f"{result}，还剩{max_tries - count}次")

    print(f"很遗憾，正确答案是{target}。")
    return False


def main():
    stats = {"total": 0, "win": 0}
    while True:
        choice = input("选择难度: 1-50(1), 1-100(2), 1-1000(3)，直接回车默认100: ")
        if choice == "":
            choice = "2"
        max_num = {1: 50, 2: 100, 3: 1000}.get(int(choice), 100)
        stats["total"] += 1
        if play_game(max_num):
            stats["win"] += 1
        print(f"统计：玩了{stats['total']}局，赢了{stats['win']}局")
        if input("再玩一局？(y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()