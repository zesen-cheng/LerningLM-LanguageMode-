"""第 06 课：神经网络与反向传播。运行：python demo.py"""

def lesson_06():
    x, target = 2.0, 3.0
    w1 = w2 = 1.0
    hidden = max(0.0, w1 * x)
    prediction = w2 * hidden
    before = (prediction - target) ** 2 / 2
    d_w2 = (prediction - target) * hidden
    d_w1 = (prediction - target) * w2 * x
    w1 -= 0.1 * d_w1
    w2 -= 0.1 * d_w2
    after = (w2 * max(0.0, w1 * x) - target) ** 2 / 2
    print("一次反向传播前后 loss:", round(before, 4), round(after, 4))
    assert after < before

if __name__ == '__main__':
    lesson_06()
