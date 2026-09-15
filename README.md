# Resume-Optimizer

基于阿里云百炼大模型 API 的自动化简历优化工具。输入原始项目经历，AI 自动按 STAR 法则润色并生成专业排版的 Word 简历。

## ✨ 功能

- AI 智能润色项目经历（STAR 法则 + 量化数据补充）
- 自动生成格式化的 Word 简历文档
- 支持自定义 Prompt 和模型配置

## 🛠️ 技术栈

- Python 3
- 阿里云百炼大模型 API (Qwen)
- python-docx (Word 文档生成)
- requests (HTTP 请求)

## 🚀 快速开始

### 1. 安装依赖

```
pip install requests python-docx
```

### 2. 配置环境变量

在项目根目录新建 `.env` 文件，填入你的百炼 API 密钥

```
DASHSCOPE_API_KEY=你的API_KEY
```

> 
> ⚠️ `.env` 文件已加入 `.gitignore`，不会上传到 Github，保护密钥安全。

### 3. 运行程序

```
python main.py
```

程序读取 `resume.txt` 的原始简历，AI 优化后生成 `optimized_resume.txt` 和 `resume_final.docx`。

## 📁 项目结构

```
├── ai_engine.py         # 调用阿里云百炼大模型API，简历文本润色逻辑
├── config.py            # 读取环境变量，模型配置
├── main.py              # 程序入口，串联整个流程
├── make_word.py         # python-docx模块，生成格式化Word简历
├── resume.txt           # 输入：原始简历文本
├── optimized_resume.txt # 输出：AI优化后的简历文本
├── resume_final.docx    # 输出：最终Word简历
├── .gitignore           # Git忽略配置文件
└── README.md            # 项目说明文档
```

## 🔒 安全说明

API 密钥使用环境变量`.env`读取，**不硬编码写在代码内**，避免密钥泄露。
`.env`文件已配置在`.gitignore`，不会提交到代码仓库。

## 📌 后续迭代计划

- 增加命令行参数，支持自定义输入输出文件路径
- 增加简历模板切换功能
- 增加简单 Web 界面，可视化操作
