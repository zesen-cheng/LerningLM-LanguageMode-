"""第 12 课：Transformer Block。运行：python demo.py"""

def lesson_12():
    import math
    x = [1.0, 2.0]
    head_a = [0.75 * x[0] + 0.25 * x[1]] * 2
    head_b = [0.25 * x[0] + 0.75 * x[1]] * 2
    residual = [x[i] + head_a[i] + head_b[i] for i in range(2)]
    mean = sum(residual) / len(residual)
    variance = sum((v - mean) ** 2 for v in residual) / len(residual)
    normalized = [(v - mean) / math.sqrt(variance + 1e-5) for v in residual]
    print("双头汇总 + 残差 + 归一化:", [round(v, 3) for v in normalized])
    assert len(normalized) == len(x)

if __name__ == '__main__':
    lesson_12()
