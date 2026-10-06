import json
import os
from datetime import datetime

TODOS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos(filename):
    """从文件加载待办列表。
    如果文件不存在或内容不是列表，就返回空列表。
    """
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_todos(todos, filename):
    """把待办列表保存到 JSON 文件。
    ensure_ascii=False 让中文正常显示，indent=2 让文件更整齐。
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def show_todos(todos, filter_type="all"):
    """查看待办。
    filter_type 可选：all=全部，todo=未完成，done=已完成。
    """
    if filter_type == "todo":
        filtered = [t for t in todos if not t["done"]]
        title = "未完成待办"
    elif filter_type == "done":
        filtered = [t for t in todos if t["done"]]
        title = "已完成待办"
    else:
        filtered = todos
        title = "当前待办"

    print(f"\n--- {title} ---")
    if not filtered:
        print("(暂无待办)")
        return

    for i, todo in enumerate(filtered, start=1):
        status = "√" if todo["done"] else "☐"
        created = todo.get("created_at", "")
        print(f"{i}. [{status}] {todo['title']}  (创建时间: {created})")


def add_todo(todos, title):
    """添加待办，直接接收标题字符串。
    每条待办会带上 created_at 时间戳。
    内容为空时不添加。
    """
    title = title.strip()
    if not title:
        print("内容为空，未添加")
        return

    todos.append({
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat()
    })
    print(f"已添加：{title}")


def remove_todo(todos, keyword):
    """按关键词删除待办。
    找到第一条标题包含关键词的待办并删除。
    """
    keyword = keyword.strip()
    if not keyword:
        print("请提供要删除的内容关键词")
        return

    for i, todo in enumerate(todos):
        if keyword in todo["title"]:
            removed = todos.pop(i)
            print(f"已删除：{removed['title']}")
            return

    print(f"未找到包含「{keyword}」的待办")


def mark_done(todos, keyword):
    """按关键词标记待办为完成。
    找到第一条标题包含关键词的待办并标记。
    """
    keyword = keyword.strip()
    if not keyword:
        print("请提供要标记的内容关键词")
        return

    for i, todo in enumerate(todos):
        if keyword in todo["title"]:
            todos[i]["done"] = True
            print(f"已标记完成：{todo['title']}")
            return

    print(f"未找到包含「{keyword}」的待办")


def clear_todos(todos):
    """清空所有待办。
    需要用户输入 y 确认，防止误删。
    """
    if not todos:
        print("暂无待办，无需清空")
        return

    confirm = input("确认清空所有待办？(y/n): ").strip().lower()
    if confirm == "y":
        todos.clear()
        print("已清空所有待办")
    else:
        print("已取消清空")


def parse_command(todos, cmd):
    """解析自然语言命令。
    用 if/elif 匹配开头关键词，把剩下的部分当作参数。
    """
    cmd = cmd.strip()
    if not cmd:
        return

    if cmd.startswith("添加"):
        content = cmd[2:].strip()
        add_todo(todos, content)

    elif cmd.startswith("删除"):
        content = cmd[2:].strip()
        remove_todo(todos, content)

    elif cmd.startswith("完成"):
        content = cmd[2:].strip()
        mark_done(todos, content)

    elif cmd in ("查看", "查看待办", "列表"):
        show_todos(todos, "all")

    elif cmd in ("查看未完成", "未完成"):
        show_todos(todos, "todo")

    elif cmd in ("查看已完成", "已完成"):
        show_todos(todos, "done")

    elif cmd in ("清空", "清空待办"):
        clear_todos(todos)

    elif cmd in ("退出", "exit", "quit"):
        save_todos(todos, TODOS_FILE)
        print("已保存，退出")
        return "exit"

    else:
        print("未识别的命令，试试这些：")
        print("  添加 买牛奶")
        print("  删除 买牛奶")
        print("  完成 买牛奶")
        print("  查看 / 查看未完成 / 查看已完成")
        print("  清空")
        print("  退出")


def main():
    """程序主循环：加载数据 → 等待自然语言命令 → 解析执行 → 退出时保存。"""
    todos = load_todos(TODOS_FILE)

    print("\n===== 待办清单（自然语言版）=====")
    print("输入「帮助」查看可用命令，输入「退出」保存并退出\n")

    while True:
        cmd = input("请输入命令：").strip()
        if not cmd:
            continue

        if cmd in ("帮助", "help", "h"):
            print("\n可用命令:")
            print("  添加 xxx       - 添加待办")
            print("  删除 xxx       - 删除待办")
            print("  完成 xxx       - 标记完成")
            print("  查看           - 查看全部")
            print("  查看未完成     - 只看未完成")
            print("  查看已完成     - 只看已完成")
            print("  清空           - 清空所有")
            print("  退出           - 保存并退出\n")
            continue

        result = parse_command(todos, cmd)
        if result == "exit":
            break


if __name__ == "__main__":
    main()