import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"   # ① 注意是 api，不是 qpi
)

def ask(system_prompt, user_prompt):         # ② systen → system
    messages = [
        {"role": "system", "content": system_prompt},   # ③ systen → system
        {"role": "user", "content": user_prompt}
    ]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content

# 场景1：翻译助手
print("=" * 40)
print("场景1: 翻译助手")
print("=" * 40)
system1 = "你是一个专业的中英文翻译助手。只输入翻译结果，不要解释。"
user1 = "请把下面这句话翻译成英:今天天气很好，我想去公园散步。"
print(ask(system1, user1))

# 场景2: 代码审查
print("\n" + "=" * 40)
print("场景2: 代码审查")
print("=" * 40)
system2 = """你是一个严格的python代码审查员。
只指出问题，不夸奖。每个问题给出：问题描述、原因、修改意见。
如果代码没问题,回复"无问题"。"""
user2 = """请审查下面代码:
def add(a,b):
    return a+b
    
result = add(3,5)
print(result)"""
print(ask(system2, user2))

# 场景3：面试官模拟
print("\n" + "=" * 40)
print("场景三: 面试官模拟")
print("=" * 40)
system3 = """你是一个AI公司面试官,正在面试零基础转行AI编程的候选人。
每次只问一个问题,等候选人回答后再问下一个。
问题要循序渐进,从python基础到Agent概念。"""
user3 = "请开始面试,问第一个问题。"
print(ask(system3, user3))