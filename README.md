# Langflow 实现本地知识库

> 本项目将用 <a href="https://github.com/langflow-ai/langflow" target="_blank">langflow</a> 实现一个本地知识库。

Langflow 是大模型可视化组件编排工具。它可以为大模型赋能，比如可以为大模型应用增加对话记忆、文档检索等等的功能。它基本上站到了 LangChain 类似的生态位。开发大模型应用的需求通常比较 flexible，在功能和性能都满足的条件下，Langflow 可以快速实现原型开发和模块复用，是目前的效率之选。

本项目的内容包括：

- 介绍 RAG 的相关概念
- 使用 Langflow 实现简单的知识库
- 使用 Langflow 实现带对话记忆功能的知识库
- 使用 Langflow 实现代码检查 (code review) 功能

✨环境部署相关的脚本，我放在这里了 [deploy](/deploy).


## 一、RAG 的概念介绍

这一节，我们先介绍 RAG 的相关概念，

**知识库** 就像大语言模型的“小抄”。在回答你之前，大模型先瞅一眼小抄，看有没有和你的问题相关的内容。如果有，就会从知识库中取回相应的文本片段，再结合大模型自身的能力生成最终回答。

知识库使用了一种叫 **RAG（检索增强生成）** 的技术。通过 RAG，大模型可以检索我们给它的文档。比如我们给它数学、法律、金融相关的文档，它可以事先进行“消化”、“吸收”。当我们对它提问时，它就能够像真正的专家一样，结合这些领域知识回答问题。

目录：

1. 提示词模板
2. RAG 技术
    - 文本向量化
    - 向量数据库


## 二、简单的 RAG 应用

本节我们完成一个简单的 RAG 应用。我们将一个文档向量化后，存入向量数据库中，然后用 deepseek-r1:1.5b 模型，整合 RAG 取回的内容后输出回答。

最终的 langflow 工作流如下：

![](/img/simple_rag_app.jpg)

目录：

1. 环境准备
    - 安装 Ollama
    - 安装 langflow
    - 安装 chroma
2. langflow 搭建工作流
    - 创建一个新的 Flow
    - 初始界面
    - 本地改造计划
    - 启动 Ollama 服务
    - 添加 Ollama Embeddings 组件
    - 添加 Chroma DB 组件
    - 添加 Ollama 组件
    - 传入文档


## 三、带对话记忆功能的 RAG

通过添加 Messsage History 组件，就可以为 RAG 添加对历史对话的记忆。

![](/img/rag_flow_with_memory.jpg)

目录：

1. Messsage History 组件
2. Directory 组件


## 四、Langflow 实现代码检查

> 最后，来开发一个没用到 RAG，但是很有用的大模型应用。

工作中，我们在提交代码之前，需要找同事 code review。但是现在我们有大模型，在找同事前不先用大模型 review 一番，总感觉不尊重同事。即使有保密需求，本地部署大模型也可以满足。8G 显存就可以轻松运行 `deepseek-r1:14b`，在 code review 方面完全够用了。

实现一个这样的工作流特别简单，最终完成的工作流如下：

![](/img/code_review.jpg)

目录：

1. 提示词模板
2. 模型部分
3. 本地提交代码
