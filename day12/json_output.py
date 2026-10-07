import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://api.deepseek.com/v1"
)

def extract_info(text):
    system_prompt = """你是一个信息提取助手。
    请从用户输入中提取信息,只输出JSON,不输出任何其他文字。
 jsonn 格式如下:
{
       "name":"姓名",
       "age":年龄数字,
       "city":"城市",
       "hobby":"爱好"
}
如果某个字段没有提到,填null。"""

    messages = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":text}
    ]

    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# 测试
text = "我叫小明,今年25岁,来自天津,喜欢编程和篮球。"
result = extract_info(text)
print("模型原始输出:")
print(result)

# 解析JSON
try:
    data = json.loads(result)
    print("\n解析成功:")
    print(f"姓名:{data['name']}")
    print(f"年龄:{data['age']}")
    print(f"城市:{data['city']}")
    print(f"爱好:{data['hobby']}")
except json.JSONDecodeError as e:
    print(f"\nJSON解析失败:{e}")
