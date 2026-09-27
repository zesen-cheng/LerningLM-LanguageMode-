"""第 26 课：封存评估与回归。运行：python demo.py"""

def lesson_26():
    sealed = [
        ("三项建议", lambda text: text.count("；") == 2),
        ("不要编造姓名", lambda text: "不知道" in text),
    ]
    baseline = ["先规划；再执行；最后复盘", "不知道你的姓名"]
    candidate = ["先规划；再执行；最后复盘", "你叫小白"]
    score = lambda outputs: [check(text) for (_, check), text in zip(sealed, outputs)]
    print("固定测试 基线:", score(baseline), "候选:", score(candidate))
    assert sum(score(candidate)) < sum(score(baseline))

if __name__ == '__main__':
    lesson_26()
