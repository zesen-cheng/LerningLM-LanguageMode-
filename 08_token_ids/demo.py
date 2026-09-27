"""第 08 课：文本如何变成 token ID。运行：python demo.py"""

def lesson_08():
    text = "我喜欢苹果。"
    vocabulary = {char: i for i, char in enumerate(sorted(set(text)))}
    ids = [vocabulary[char] for char in text]
    inverse = {i: char for char, i in vocabulary.items()}
    recovered = "".join(inverse[i] for i in ids)
    print("字符:", list(text), "ID:", ids, "还原:", recovered)
    assert recovered == text

if __name__ == '__main__':
    lesson_08()
