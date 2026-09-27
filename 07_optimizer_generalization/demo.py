"""第 07 课：优化器与泛化。运行：python demo.py"""

def lesson_07():
    target = 3.0
    for rate in (0.1, 1.2):
        weight = 0.0
        history = []
        for _ in range(5):
            history.append(round((weight - target) ** 2, 3))
            weight -= rate * 2 * (weight - target)
        print(f"学习率 {rate}: loss={history}")
    assert (0.0 - target) ** 2 > (0.0 + 0.1 * 2 * target - target) ** 2

if __name__ == '__main__':
    lesson_07()
