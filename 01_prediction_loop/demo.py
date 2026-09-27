"""第 01 课：从样本到预测。运行：python demo.py"""

def lesson_01():
    from collections import Counter
    texts = ["我喜欢苹果", "我喜欢梨", "他喜欢苹果"]
    next_words = Counter(text.split("喜欢")[1] for text in texts)
    print("训练样本之后的预测计数:", dict(next_words))
    next_words.update(["梨"])
    print("加入新样本后的计数:", dict(next_words))
    assert next_words["苹果"] == next_words["梨"] == 2

if __name__ == '__main__':
    lesson_01()
