import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"
)

def extract_info(text):
    system_prompt = """你是一个专业的信息提取助手。
【角色】你是一位高精度的信息提取专家，擅长从自然语言文本中准确提取结构化数据。
【任务】从用户输入的文本中提取以下四个字段的信息：name（姓名）、age（年龄）、city（城市）、hobby（爱好）。
【约束】
- 只输出JSON，不要输出任何其他文字、解释或Markdown代码块
- 不要使用 ```json 或 ``` 包裹
- age 必须是整数类型（不要加引号），如果无法确定则填 null
- 如果某个字段在文本中没有提到，该字段填 null
- 不要自行推断或编造信息，没有提到的字段一律填 null
【输出格式】严格按照以下JSON结构输出，不要多也不要少：
{"name": "提取到的姓名或null", "age": 年龄数字或null, "city": "提取到的城市或null", "hobby": "提取到的爱好或null"}

以下是两个示例：

示例1（完整信息）：
用户输入：我叫小明，今年25岁，来自天津，喜欢编程和篮球。
你的输出：{"name": "小明", "age": 25, "city": "天津", "hobby": "编程和篮球"}

示例2（缺失字段填null）：
用户输入：我叫小红，喜欢读书和旅行。
你的输出：{"name": "小红", "age": null, "city": null, "hobby": "读书和旅行"}

现在请从以下文本中提取信息："""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
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