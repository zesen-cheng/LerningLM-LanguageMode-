"""第 03 课：训练所需数学直觉。运行：python demo.py"""

def lesson_03():
    import math
    vector = [1.0, 2.0]
    weights = [0.5, -0.25]
    score = sum(a * b for a, b in zip(vector, weights))
    logits = [score, 0.0]
    probabilities = [math.exp(x) / sum(math.exp(y) for y in logits) for x in logits]
    print("标量分数:", score, "概率向量:", probabilities)
    assert abs(sum(probabilities) - 1.0) < 1e-12

if __name__ == '__main__':
    lesson_03()
