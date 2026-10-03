import json

profile = {
    "name":"小明",
    "age":25,
    "hobbies":["AI","编程"]
}

# 写入JSON文件
with open("profile.json","w",encoding="utf-8") as f :
    json.dump(profile,f,ensure_ascii=False,indent=2)

print("写入完成")

# 读取JSON文件
with open("profile.json","r",encoding="utf-8") as f :
    data = json.load(f)

print(data)
print(type(data))
print(data["name"])