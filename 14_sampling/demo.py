"""第 14 课：采样与回复。运行：python demo.py"""

def lesson_14():
    import math
    logits = {"苹果": 2.0, "梨": 1.0, "香蕉": 0.0}
    for temperature in (0.5, 1.0, 2.0):
        weights = {k: math.exp(v / temperature) for k, v in logits.items()}
        total = sum(weights.values())
        print(f"温度 {temperature}: 苹果概率={weights['苹果'] / total:.3f}")
    top2 = sorted(logits, key=logits.get, reverse=True)[:2]
    print("top-k=2 的候选:", top2)
    assert "香蕉" not in top2

if __name__ == '__main__':
    lesson_14()
