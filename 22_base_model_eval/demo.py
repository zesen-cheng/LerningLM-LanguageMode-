"""第 22 课：基础模型评估。运行：python demo.py"""

def lesson_22():
    import math
    from collections import Counter, defaultdict
    train = ["我喜欢苹果", "我喜欢梨"]
    validation = "他喜欢苹果"
    counts = defaultdict(Counter)
    for sentence in train:
        for a, b in zip(sentence, sentence[1:]):
            counts[a][b] += 1
    vocabulary = set("".join(train) + validation)
    losses = [-math.log((counts[a][b] + 1) / (sum(counts[a].values()) + len(vocabulary))) for a, b in zip(validation, validation[1:])]
    print("未见句子的平均 NLL:", round(sum(losses) / len(losses), 4))
    assert len(losses) == len(validation) - 1

if __name__ == '__main__':
    lesson_22()
