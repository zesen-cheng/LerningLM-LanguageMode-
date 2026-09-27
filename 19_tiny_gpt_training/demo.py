"""第 19 课：从随机权重训练 Tiny GPT。运行：python demo.py"""

def lesson_19():
    import math
    sequence = [0, 1, 2, 3, 0, 1, 2, 3]
    vocab = 4
    weights = [[0.0] * vocab for _ in range(vocab)]
    pairs = list(zip(sequence, sequence[1:]))
    def nll():
        return sum(-math.log(math.exp(weights[a][b]) / sum(math.exp(v) for v in weights[a])) for a, b in pairs) / len(pairs)
    before = nll()
    for _ in range(60):
        for a, b in pairs:
            probs = [math.exp(x) / sum(math.exp(z) for z in weights[a]) for x in weights[a]]
            for j in range(vocab):
                weights[a][j] -= 0.2 * (probs[j] - (j == b))
    after = nll()
    print("真实参数更新前后 NLL:", round(before, 4), round(after, 4))
    assert after < before

if __name__ == '__main__':
    lesson_19()
