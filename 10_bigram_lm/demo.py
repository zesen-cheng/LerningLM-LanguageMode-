"""第 10 课：Bigram 语言模型。运行：python demo.py"""

def lesson_10():
    from collections import Counter, defaultdict
    corpus = ["我喜欢苹果", "我喜欢梨", "他喜欢苹果"]
    counts = defaultdict(Counter)
    for sentence in corpus:
        for a, b in zip(sentence, sentence[1:]):
            counts[a][b] += 1
    print("'欢' 后接 token 分布:", dict(counts["欢"]))
    print("'苹' 后接 token 分布:", dict(counts["苹"]))
    assert counts["苹"]["果"] == 2

if __name__ == '__main__':
    lesson_10()
