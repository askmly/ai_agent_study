import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

SYSTEM_PROMPT = """你是一个意图分类助手。
请判断用户输入的意图，只输出 JSON，不要任何解释。
意图类别：weather_query、add_todo、delete_todo、view_todo、unknown。
JSON 格式：
{
    "intent": "意图类别",
    "confidence": 0.0-1.0,
    "entities": {"key": "value"}
}
示例1：
用户：帮我查一下明天天津的天气
输出：{"intent": "weather_query", "confidence": 0.95, "entities": {"city": "天津", "date": "明天"}}
示例2：
用户：添加买牛奶
输出：{"intent": "add_todo", "confidence": 0.98, "entities": {"title": "买牛奶"}}
"""

def classify(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def clean_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]
    return text.strip()

def main():
    while True:
        user_input = input("\n请输入一句话（q 退出）：")
        if user_input.lower() == "q":
            break
        try:
            raw = classify(user_input)
            cleaned = clean_json(raw)
            data = json.loads(cleaned)
            print(f"意图：{data['intent']}")
            print(f"置信度：{data['confidence']}")
            print(f"实体：{data['entities']}")
        except Exception as e:
            print(f"处理失败：{e}")

if __name__ == "__main__":
    main()