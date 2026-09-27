"""第 43 课：结课：tokenizer 基线。运行：python demo.py"""

def lesson_43():
    from collections import Counter
    train = "我喜欢苹果。我喜欢梨。"
    vocabulary = {char: i for i, char in enumerate(sorted(set(train)))}
    ids = [vocabulary[char] for char in train]
    restored = "".join({v: k for k, v in vocabulary.items()}[i] for i in ids)
    bigrams = Counter(zip(ids, ids[1:]))
    print("词表大小:", len(vocabulary), "基线不同 bigram 数:", len(bigrams))
    assert restored == train

if __name__ == '__main__':
    lesson_43()
