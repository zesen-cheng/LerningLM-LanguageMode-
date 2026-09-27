"""第 11 课：因果 Attention。运行：python demo.py"""

def lesson_11():
    import math
    values = [1.0, 2.0, 4.0]
    for position in range(len(values)):
        visible = values[:position + 1]  # 因果遮罩：只看当前位置及之前
        scores = [values[position] * key for key in visible]
        scale = max(scores)
        weights = [math.exp(s - scale) for s in scores]
        weights = [w / sum(weights) for w in weights]
        context = sum(w * v for w, v in zip(weights, visible))
        print(f"位置 {position}: 可见={visible}, 汇总={context:.3f}")
    assert len(values[:1]) == 1

if __name__ == '__main__':
    lesson_11()
