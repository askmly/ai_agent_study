import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("错误：没有找到 DEEPSEEK_API_KEY")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
    timeout=30.0
)

# ① 新增：预设几套 System Prompt，用数字切换
SYSTEM_PROMPTS = {
    "1": "你是一个友好的 AI 助手，回答简洁明了。",
    "2": "你是一个专业的 Python 编程导师，擅长用通俗的语言解释代码，适合零基础学习者。",
    "3": "你是一个严谨的翻译助手，只输出翻译结果，不添加额外说明。",
}

# ② 新增：默认使用第 1 套
current_prompt_key = "1"

# ③ 新增：JSON 文件路径，对话历史保存在这里
HISTORY_FILE = "chat_history.json"

# ④ 新增：从 JSON 文件加载历史
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # ⑤ 保存的是完整 messages（含 system），加载时直接用
                return data
        except Exception:
            print("历史文件读取失败，将使用空历史。")
    return []

# ⑥ 新增：把当前 messages 保存到 JSON
def save_history(messages):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存历史失败：{e}")

# ⑦ 新增：根据当前选择的 prompt 重建 messages
def build_messages():
    system_content = SYSTEM_PROMPTS.get(current_prompt_key, SYSTEM_PROMPTS["1"])
    # 如果有历史且第一条是 system，就替换它；否则重新构建
    messages = load_history()
    if messages and messages[0].get("role") == "system":
        messages[0]["content"] = system_content
    else:
        messages = [{"role": "system", "content": system_content}]
    return messages

# ⑧ 初始加载历史
messages = build_messages()

print("多轮对话开始，输入 q 退出。")
print("输入 /role 切换 AI 人设，输入 /clear 清空历史。")

MAX_RETRIES = 3

while True:
    user_input = input("\n你: ")

    # ⑨ 新增：切换 System Prompt
    if user_input.strip() == "/role":
        print("\n请选择 AI 人设：")
        for key, desc in SYSTEM_PROMPTS.items():
            print(f"  {key}. {desc}")
        choice = input("请输入编号: ").strip()
        if choice in SYSTEM_PROMPTS:
            current_prompt_key = choice
            messages = build_messages()  # 重建 messages，保留历史但换 system
            save_history(messages)
            print(f"已切换到人设 {choice}。")
        else:
            print("无效编号，未切换。")
        continue

    # ⑩ 新增：清空历史
    if user_input.strip() == "/clear":
        messages = [{"role": "system", "content": SYSTEM_PROMPTS[current_prompt_key]}]
        save_history(messages)
        print("历史已清空。")
        continue

    if user_input.lower() == "q":
        print("再见！")
        break

    messages.append({"role": "user", "content": user_input})

    attempt = 0
    success = False
    while attempt < MAX_RETRIES and not success:
        attempt += 1
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            print(f"AI: {reply}")
            messages.append({"role": "assistant", "content": reply})
            save_history(messages)  # ⑪ 每次收到回复后保存
            success = True
        except Exception as e:
            print(f"调用出错（第 {attempt} 次尝试）：{e}")
            if attempt < MAX_RETRIES:
                wait_time = 2 ** (attempt - 1)
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("重试次数已用尽，跳过本次对话。")
                messages.pop()