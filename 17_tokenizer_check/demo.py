"""第 17 课：训练与检验 tokenizer。运行：python demo.py"""

def lesson_17():
    text = "我喜欢苹果。"
    vocabulary = ["我", "喜欢", "苹果", "。"]
    ids = []
    remaining = text
    while remaining:
        match = next(token for token in sorted(vocabulary, key=len, reverse=True) if remaining.startswith(token))
        ids.append(vocabulary.index(match))
        remaining = remaining[len(match):]
    recovered = "".join(vocabulary[i] for i in ids)
    print("玩具子词 ID:", ids, "还原:", recovered)
    assert recovered == text

if __name__ == '__main__':
    lesson_17()
