# 请确保网络畅通，并可以访问Huggingface.co
# 安装vllm
pip install vllm

# 安装好vllm后可以使用以下命令运行LLM
python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen1.5-4B-Chat --max-model-len=1024