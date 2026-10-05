import json
import os

CONTACTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        print("通讯录文件格式不正确，已重新开始")
        return []
    except (json.JSONDecodeError, OSError):
        print("通讯录文件读取失败，已重新开始")
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print("已保存")


def show_contacts(contacts):
    if not contacts:
        print("暂无联系人")
        return
    print("编号 | 姓名 | 电话 | 邮箱")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def add_contact(contacts):
    name = input("姓名: ").strip()
    if not name:
        print("姓名不能为空")
        return
    phone = input("电话: ").strip()
    email = input("邮箱: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print("添加成功")


def find_contact(contacts):
    keyword = input("输入姓名关键词: ").strip()
    if not keyword:
        print("关键词不能为空")
        return
    results = [c for c in contacts if keyword in c["name"]]
    if not results:
        print("未找到")
        return
    for c in results:
        print(f"{c['name']} | {c['phone']} | {c['email']}")


def ask_index(contacts, prompt):
    """请用户输入编号，非法输入返回 None。"""
    raw = input(prompt).strip()
    try:
        idx = int(raw) - 1
    except ValueError:
        print("请输入数字")
        return None
    if not (0 <= idx < len(contacts)):
        print("编号不存在")
        return None
    return idx


def delete_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    idx = ask_index(contacts, "输入要删除的编号: ")
    if idx is None:
        return
    removed = contacts.pop(idx)
    print(f"已删除: {removed['name']}")


def edit_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    idx = ask_index(contacts, "输入要修改的编号: ")
    if idx is None:
        return
    contact = contacts[idx]
    print("直接回车表示不修改该项")
    name = input(f"姓名 [{contact['name']}]: ").strip()
    phone = input(f"电话 [{contact['phone']}]: ").strip()
    email = input(f"邮箱 [{contact['email']}]: ").strip()
    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    print("修改成功")


def show_menu():
    print("\n==== 通讯录 ====")
    print("1. 添加")
    print("2. 查看")
    print("3. 查找")
    print("4. 删除")
    print("5. 修改")
    print("6. 保存")
    print("7. 退出")


def main():
    contacts = load_contacts()
    while True:
        show_menu()
        choice = input("请选择: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("已退出")
            break
        else:
            print("无效选择，请输入 1-7 的数字")


if __name__ == "__main__":
    main()
