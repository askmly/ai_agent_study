import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("错误：没有找到 DEEPSEEK_API_KEY")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1",
    timeout=30.0          # ① 新增：请求超时 30 秒
)

# ② 新增：重试次数常量
MAX_RETRIES = 3

def extract_info(text, max_retries=MAX_RETRIES):
    """提取信息，带重试和清理"""
    system_prompt = """你是一个信息提取助手。
请从用户输入中提取信息,只输出JSON,不输出任何其他文字。
json 格式如下:
{
       "name":"姓名",
       "age":年龄数字,
       "city":"城市",
       "hobby":"爱好"
}
如果某个字段没有提到,填null。"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ]

    attempt = 0
    while attempt < max_retries:
        attempt += 1
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0
            )
            raw_output = response.choices[0].message.content

            # ③ 新增：清理模型输出的 JSON
            cleaned = clean_json(raw_output)

            # ④ 新增：校验 JSON
            data = validate_json(cleaned)
            print(f"  [第{attempt}次尝试] 提取成功")
            return data

        except Exception as e:
            print(f"  [第{attempt}次尝试] 调用出错: {e}")
            if attempt < max_retries:
                wait_time = 2 ** (attempt - 1)
                print(f"  等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("  重试次数已用尽，返回空结果。")
                return {}

    return {}


def clean_json(raw_text):
    """清理模型输出的 JSON 文本"""
    text = raw_text.strip()

    # 去掉 markdown 代码块标记（模型经常包在 ```json ... ``` 里）
    if text.startswith("```"):
        text = text.strip("`").strip()
        if text.lower().startswith("json"):
            text = text[4:].strip()

    # 去掉首尾的多余引号（偶尔模型会多输出引号）
    text = text.strip('"').strip()

    return text


def validate_json(json_str):
    """解析并校验 JSON，返回数据字典"""
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  JSON 解析失败: {e}")
        print(f"  原始内容: {json_str[:200]}")
        return {}

    # ⑤ 新增：检查必需字段
    required_fields = ["name", "age", "city", "hobby"]
    for field in required_fields:
        if field not in data:
            print(f"  警告：缺少字段 '{field}'，已补 null")
            data[field] = None

    # ⑥ 新增：类型校验 - age 必须是整数
    if data["age"] is not None:
        if not isinstance(data["age"], int):
            try:
                data["age"] = int(data["age"])
                print(f"  年龄已修正为整数: {data['age']}")
            except (ValueError, TypeError):
                print(f"  警告：年龄 '{data['age']}' 无法转为数字，设为 null")
                data["age"] = None

    return data


# ==================== 测试 ====================

test_cases = [
    ("完整信息", "我叫小明,今年25岁,来自天津,喜欢编程和篮球。"),
    ("缺少年龄", "我叫小红,来自北京,喜欢画画和听音乐。"),
    ("年龄中文数字", "我今年二十五岁,名字是大壮,住在上海,爱好是打游戏。"),
    ("输入为空", ""),
]

for name, text in test_cases:
    print(f"\n{'='*50}")
    print(f"测试: {name}")
    print(f"输入: {text if text else '(空)'}")
    print(f"{'='*50}")
    result = extract_info(text)
    if result:
        print(f"姓名: {result.get('name', 'N/A')}")
        print(f"年龄: {result.get('age', 'N/A')}")
        print(f"城市: {result.get('city', 'N/A')}")
        print(f"爱好: {result.get('hobby', 'N/A')}")
    else:
        print("未能提取到有效信息。")