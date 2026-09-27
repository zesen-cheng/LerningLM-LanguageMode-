"""第 25 课：小规模 SFT。运行：python demo.py"""

def lesson_25():
    import math
    score = 0.0  # 选择“简短回答”的 logit
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    before = sigmoid(score)
    for _ in range(12):
        score -= 0.3 * (sigmoid(score) - 1.0)  # SFT: 目标是简短回答
    after = sigmoid(score)
    print("SFT 玩具模型中目标回答概率:", round(before, 3), "->", round(after, 3))
    assert after > before

if __name__ == '__main__':
    lesson_25()
