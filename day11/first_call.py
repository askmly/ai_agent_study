import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取 API 文件
load_dotenv()

# 读取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("错误:没有找到DEEPSEEK_API_KEY,请检查.env文件")
    exit()

# 创建客户端
client = OpenAI(
    api_key = api_key,
    base_url = "https://api.deepseek.com"
)

# 构造消息
messages = [
    {"role":"system","content":"你是一个友好的AI助手,回答简洁明了。"},
    {"role":"user","content":"请用一句话介绍你自己。"}
]
# 调用API
response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = messages ,
    temperature = 0.7
)

# 打印结果
print("模型回复：")
print(response.choices[0].message.content)