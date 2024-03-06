from langchain.chat_models import ChatOpenAI

from langchain.schema import HumanMessage

llm = ChatOpenAI(
    streaming=True,
    verbose=True,
    # callbacks=[callback],
    openai_api_key="none",
    openai_api_base="http://127.0.0.1:8000/v1",
    model_name="Qwen/Qwen1.5-4B-Chat"
)
instructions = """
你将得到一个带有水果名称的句子,提取这些水果名称并为其分配一个表情符号
在 python 字典中返回水果名称和表情符号
"""

fruit_names = """
苹果,梨,这是奇异果
"""

# 制作结合说明和水果名称的提示
prompt = (instructions + fruit_names)

# Call the LLM
output = llm([HumanMessage(content=prompt)])

print (output.content)
print("========")
print (type(output.content))
# 苹果: 🍎梨: 🥐奇异果: 🍓
# ========
# <class 'str'>
