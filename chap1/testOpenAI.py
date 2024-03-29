import openai
from openai import OpenAI

client = OpenAI(api_key="none")
# TODO: The 'openai.api_base' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url="http://localhost:8000/v1")'
# openai.api_base = "http://localhost:8000/v1"

# 使用流式回复的请求
for chunk in client.chat.completions.create(model="Qwen/Qwen1.5-4B-Chat",
messages=[
    {"role": "user", "content": "You know who the Pat Gelsinger is?"}
],
stream=True
# 流式输出的自定义stopwords功能尚未支持，正在开发中):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n")
# 不使用流式回复的请求
# response = openai.ChatCompletion.create(
#     model="Qwen/Qwen1.5-4B-Chat",
#     messages=[
#         {"role": "user", "content": "你知道黄仁勋吗？"}
#     ],
#     stream=False,
#     stop=[] # 在此处添加自定义的stop words 例如ReAct prompting时需要增加： stop=["Observation:"]。
# )
# print(response.choices[0].message.content)
