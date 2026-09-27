import random
def play_game():
    target =random.randint(1,100)
    count = 0
    max_tries = 7
    print("我想了一个1-100的数字,你有7次机会。")
    while count < max_tries:
        try:
            guess = int(input("请输入你的数字:"))
        except ValueError:
            print("请输入数字！")

        count += 1

        if guess > target:
            print(f"大了，还剩{max_tries - count} 次")
        elif guess < target:
            print(f"小了，还剩{max_tries - count} 次")
        else:
            print(f"恭喜，你用了{count} 次猜对了")
            return
    print(f"机会用完,答案是{target}")

def main():
    while True:
        play_game()
        again = input("再玩一局？(y/n):")
        if again.lower()!="y":
            print("再见")
            break
if __name__ == "__main__":
    main()

            

    