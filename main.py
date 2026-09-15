from ai_engine import ask_ai

# 1.读取简历文件 resume.txt
with open("resume.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

# 2.构造提示词，传给AI
prompt = f"""
请帮我优化下面这份简历，语言专业精炼，适合求职，不要改变原有信息：
{original_text}
"""

# 3.调用AI函数
result = ask_ai(prompt)

# 4.打印输出优化结果
print("=====优化后的简历=====")
print(result)

# 可选：把结果保存到新文件
with open("optimized_resume.txt","w",encoding="utf-8") as f:
    f.write(result)
