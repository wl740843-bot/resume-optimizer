# Resume Optimizer - AI 简历优化工具

基于阿里云百炼大模型 API 的自动化简历优化工具。输入原始项目经历，AI 自动按 STAR 法则润色并生成专业排版的 Word 简历。

## 功能

- AI 智能润色项目经历（STAR 法则 + 量化数据补充）
- 自动生成格式化的 Word 简历文档
- 支持自定义 Prompt 和模型配置

## 技术栈

- Python 3
- 阿里云百炼大模型 API (Qwen)
- python-docx (Word 文档生成)
- requests (HTTP 请求)

## 快速开始

### 1. 安装依赖

```bash
pip install requests python-docx
## 🔒 安全说明
API密钥使用环境变量`.env`读取，**不硬编码写在代码内**，避免密钥泄露。
`.env`文件已配置在.gitignore，不会提交到代码仓库。
