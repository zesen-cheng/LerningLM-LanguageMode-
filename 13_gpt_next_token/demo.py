"""第 13 课：GPT 的下一个 token 目标。运行：python demo.py"""

def lesson_13():
    transition = {"我": "喜", "喜": "欢", "欢": "苹", "苹": "果", "果": "。"}
    output = "我"
    for _ in range(5):
        output += transition[output[-1]]
    print("逐 token 自回归生成:", output)
    assert output == "我喜欢苹果。"

if __name__ == '__main__':
    lesson_13()
