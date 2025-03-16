#!/bin/bash

# 参考：https://ollama.com/

# -------- 安装 Ollama ---------

# PS: macOS 和 Windows 从 https://ollama.com/download 下载

# 1. Linux 系统安装 ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. 验证 ollama 是否安装成功
ollama --version

# -------- 下载模型 ---------

# 下载模型
# ollama pull [MODEL_NAME]

# 下载并运行模型(当模型未下载时下载,已下载时仅运行)
# ollama run [MODEL_NAME]

# 3. 下载模型 bge-m3
ollama pull bge-m3

# 4. 下载并运行模型 DeepSeek-R1-Distill-Qwen-1.5B
ollama run deepseek-r1:1.5b

# -------- 其他命令 ---------

# 启动服务
$env:OLLAMA_HOST = "0.0.0.0:11434"  # Windows PowerShell
ollama serve

# PS: Linux 环境使用以下命令配置环境变量
# export OLLAMA_HOST=0.0.0.0:11434

# 列出所有模型
ollama list

# 移除模型
# ollama rm deepseek-r1:1.5b
# ollama rm bge-m3
