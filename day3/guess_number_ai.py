import random

DIFFICULTIES = {
    "1": {"name": "简单", "low": 1, "high": 50, "max_tries": 10},
    "2": {"name": "普通", "low": 1, "high": 100, "max_tries": 7},
    "3": {"name": "困难", "low": 1, "high": 200, "max_tries": 5},
}


def choose_difficulty():
    while True:
        print("\n请选择难度：")
        print("1. 简单：1-50，10 次机会")
        print("2. 普通：1-100，7 次机会")
        print("3. 困难：1-200，5 次机会")

        choice = input("输入 1/2/3：").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("无效选择，请输入 1、2 或 3。")


def new_stats():
    stats = {
        "games": 0,
        "wins": 0,
        "total_guesses": 0,
        "best": None,
        "by_difficulty": {},
    }

    for cfg in DIFFICULTIES.values():
        stats["by_difficulty"][cfg["name"]] = {
            "games": 0,
            "wins": 0,
            "total_guesses": 0,
        }

    return stats


def update_stats(stats, cfg, won, used_guesses):
    stats["games"] += 1
    stats["total_guesses"] += used_guesses

    if won:
        stats["wins"] += 1
        if stats["best"] is None or used_guesses < stats["best"]:
            stats["best"] = used_guesses

    d = stats["by_difficulty"][cfg["name"]]
    d["games"] += 1
    d["total_guesses"] += used_guesses
    if won:
        d["wins"] += 1


def play_game(stats):
    cfg = choose_difficulty()
    target = random.randint(cfg["low"], cfg["high"])
    guesses = []  # 本局历史猜测；每局重新建一个空 list

    print(f"\n我想了一个 {cfg['low']}-{cfg['high']} 的数字，你有 {cfg['max_tries']} 次机会。")

    while len(guesses) < cfg["max_tries"]:
        try:
            guess = int(input("请输入你的数字："))
        except ValueError:
            print("请输入数字！")
            continue  # 关键：输入失败不算次数，也不进历史

        guesses.append(guess)  # 历史 list 记录这一次
        left = cfg["max_tries"] - len(guesses)

        if guess > target:
            print(f"大了，还剩 {left} 次；历史：{guesses}")
        elif guess < target:
            print(f"小了，还剩 {left} 次；历史：{guesses}")
        else:
            print(f"恭喜，你用了 {len(guesses)} 次猜对了！历史：{guesses}")
            update_stats(stats, cfg, won=True, used_guesses=len(guesses))
            return

    print(f"机会用完，答案是 {target}；历史：{guesses}")
    update_stats(stats, cfg, won=False, used_guesses=len(guesses))


def show_stats(stats):
    print("\n===== 游戏统计 =====")
    print(f"总局数：{stats['games']}")
    print(f"胜利局数：{stats['wins']}")

    if stats["games"] == 0:
        print("胜率：0%")
        print("平均每次用：0 次")
    else:
        win_rate = stats["wins"] / stats["games"] * 100
        avg_guesses = stats["total_guesses"] / stats["games"]
        print(f"胜率：{win_rate:.1f}%")
        print(f"平均每次用：{avg_guesses:.1f} 次")

    if stats["best"] is not None:
        print(f"最快猜中：{stats['best']} 次")

    for name, data in stats["by_difficulty"].items():
        print(f"{name}：玩 {data['games']} 局，胜 {data['wins']} 局，总猜测 {data['total_guesses']} 次")


def main():
    stats = new_stats()  # 跨局统计只在 main 创建一次

    while True:
        play_game(stats)   # 函数借用 stats，并把本局结果写进去
        show_stats(stats)

        again = input("再玩一局？(y/n)：").strip().lower()
        if again != "y":
            print("再见")
            break


if __name__ == "__main__":
    main()