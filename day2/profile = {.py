profile = {
    "name": "小明",
    "age": 25,
    "city": "天津"
}

print("原始字典：", profile)
print("姓名：", profile["name"])
print("年龄：", profile.get("age"))
print("职业：", profile.get("job", "暂无"))

profile["job"] = "AI 学习者"
print("增加 job 后：", profile)

profile["age"] = 26
print("修改 age 后：", profile)

del profile["city"]
print("删除 city 后：", profile)

print("所有键：", profile.keys())
print("所有值：", profile.values())
print("所有键值对：", profile.items())

for key, value in profile.items():
    print(f"{key} = {value}")