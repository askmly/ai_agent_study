import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE,"r",encoding="utf-8") as f :
            return json.load(f)
    except (json.JSONDecodeError,FileExistsError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE ,"w",encoding="utf-8") as f :
        json.dump(contacts,f,ensure_ascii=False,indent=2)

def show_contatcts(contacts):
    if not contacts:
        print("暂无联系人")
        return
    for i ,c in enumerate(contacts,start=1):
        print(f"{i}.{c['name']}|{c['phone']}|{c['email']}")

def add_contact(contacts):
    name = input("姓名:").strip()
    phone = input("电话:").strip()
    email = input("邮箱:").strip()
    if not name:
        print("姓名不能为空")
        return
    contacts.append({"name":name,"phone":phone,"email":email})
    print("添加成功")

def find_contact(contacts):
    keyword = input("输入姓名关键词:".strip())
    results = [c for c in contacts if keyword in c["name"]]
    if not results:
        print("未找到")
    else:
        for c in results:
            print(f"{c['name']}|{c['phone']}|{c['email']}")

def delete_contact(contacts):
    show_contatcts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("输入要删除的编号:")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"已删除:{removed['name']}")
        else:
            print("编号不存在")
    except ValueError:
        print("请输入数字")

def main():
    contacts = load_contacts()
    while True:
        print("\n====通讯录====")
        print("1.查看")
        print("2.添加")
        print("3.查找")
        print("4.删除")
        print("5.保存")
        print("6.退出")
        choice= input("请选择:")
        if choice == "1":
            show_contatcts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("已保存")
        elif choice == "6":
            save_contacts(contacts)
            print("退出,已自动保存")
            break
        else:
            print("无效选择")

if  __name__ == "__main__":
    main()