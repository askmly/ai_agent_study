def show_todos(todos):
    """查看：只打印，不改变数据。"""
    print("\n--- 当前待办 ---")
    if not todos:
        print("(暂无待办)")
        return

    for i, todo in enumerate(todos, start=1):
        status = "√" if todo["done"] else "☐"
        print(f"{i}. [{status}] {todo['title']}")


def read_positive_int(prompt):
    """安全读取一个非负整数；失败返回 None，不抛异常。"""
    raw = input(prompt).strip()
    if not raw.isdigit():
        print("请输入数字")
        return None
    return int(raw)


def choose_index(todos, action):
    """让用户选择 1 开始的编号，返回 0 开始下标；无效返回 None。"""
    if not todos:
        print("暂无待办")
        return None

    show_todos(todos)
    n = read_positive_int(f"请输入要{action}的编号：")
    if n is None:
        return None

    idx = n - 1  # 用户看 1 开始，程序内部用 0 开始
    if not (0 <= idx < len(todos)):
        print("编号不存在")
        return None
    return idx


def add_todo(todos):
    """添加：空内容不添加。"""
    title = input("请输入待办内容：").strip()
    if not title:
        print("内容为空，未添加")
        return

    todos.append({"title": title, "done": False})
    print("添加成功")


def remove_todo(todos):
    """删除：按编号删。"""
    idx = choose_index(todos, "删除")
    if idx is None:
        return

    removed = todos.pop(idx)
    print(f"已删除：{removed['title']}")


def mark_done(todos):
    """标记完成：按编号改 done。"""
    idx = choose_index(todos, "标记完成")
    if idx is None:
        return

    todos[idx]["done"] = True
    print("已标记完成")


def main():
    todos = []  # 数据只由 main 拥有，函数通过参数借用它

    while True:
        print("\n===== 待办清单 =====")
        print("1. 查看待办")
        print("2. 添加待办")
        print("3. 删除待办")
        print("4. 标记完成")
        print("5. 退出")

        choice = input("请选择操作(1-5):").strip()

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            remove_todo(todos)
        elif choice == "4":
            mark_done(todos)
        elif choice == "5":
            print("退出，再见")
            break
        else:
            print("无效选择，请输入 1-5")


if __name__ == "__main__":
    main()