"""第 45 课：结课：SFT 与评估。运行：python demo.py"""

def lesson_45():
    examples = [("你好", "你好！"), ("我叫什么？", "我不知道你的名字。")]
    baseline = lambda prompt: prompt + "……"
    sft_toy = dict(examples)
    for prompt, expected in examples:
        before = baseline(prompt)
        after = sft_toy[prompt]
        print("提示:", prompt, "基础:", before, "玩具 SFT 目标:", after)
        assert after == expected
    print("这里是样本查找示意，不是神经网络泛化能力")

if __name__ == '__main__':
    lesson_45()
