import json
import os
import re

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """加载联系人列表。文件不存在或格式错误时，返回空列表。"""
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, ValueError):
        return []
    except Exception:
        return []


def save_contacts(contacts):
    """把联系人列表保存到 JSON 文件。"""
    try:
        with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("保存失败：", e)


def show_contacts(contacts):
    """显示所有联系人。"""
    if not contacts:
        print("暂无联系人")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def add_contact(contacts):
    """添加联系人，并校验邮箱格式。"""
    try:
        name = input("姓名: ").strip()
        phone = input("电话: ").strip()
        email = input("邮箱: ").strip()
    except Exception as e:
        print("输入出错：", e)
        return

    if not name:
        print("姓名不能为空")
        return

    if not is_valid_email(email):
        print("邮箱格式不正确，未添加")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("添加成功")


def find_contact(contacts):
    """按姓名关键词查找联系人。"""
    try:
        keyword = input("输入姓名关键词: ").strip()
    except Exception as e:
        print("输入出错：", e)
        return

    if not keyword:
        print("关键词不能为空")
        return

    results = [c for c in contacts if keyword in c["name"]]
    if not results:
        print("未找到")
    else:
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']}")


def find_contact_by_phone(contacts):
    """按电话关键词查找联系人。"""
    try:
        keyword = input("输入电话关键词: ").strip()
    except Exception as e:
        print("输入出错：", e)
        return

    if not keyword:
        print("关键词不能为空")
        return

    results = [c for c in contacts if keyword in c["phone"]]
    if not results:
        print("未找到")
    else:
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']}")


def modify_contact(contacts):
    """修改联系人。"""
    show_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("输入要修改的编号: ").strip()) - 1
    except ValueError:
        print("请输入数字")
        return

    if 0 <= idx < len(contacts):
        old = contacts[idx]
        print(f"当前联系人: {old['name']} | {old['phone']} | {old['email']}")

        try:
            new_name = input(f"新姓名(直接回车不改): ").strip()
            new_phone = input(f"新电话(直接回车不改): ").strip()
            new_email = input(f"新邮箱(直接回车不改): ").strip()
        except Exception as e:
            print("输入出错：", e)
            return

        if new_name:
            old["name"] = new_name
        if new_phone:
            old["phone"] = new_phone
        if new_email:
            if not is_valid_email(new_email):
                print("邮箱格式不正确，未修改邮箱")
            else:
                old["email"] = new_email

        print("修改成功")
    else:
        print("编号不存在")


def delete_contact(contacts):
    """删除联系人。"""
    show_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("输入要删除的编号: ").strip()) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"已删除: {removed['name']}")
        else:
            print("编号不存在")
    except ValueError:
        print("请输入数字")


def is_valid_email(email):
    """简单校验邮箱格式。"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def main():
    contacts = load_contacts()
    while True:
        print("\n====通讯录====")
        print("1. 查看")
        print("2. 添加")
        print("3. 查找姓名")
        print("4. 查找电话")
        print("5. 修改")
        print("6. 删除")
        print("7. 保存")
        print("8. 退出")
        choice = input("请选择: ").strip()
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            find_contact_by_phone(contacts)
        elif choice == "5":
            modify_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("已保存")
        elif choice == "8":
            save_contacts(contacts)
            print("退出，已自动保存")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    main()