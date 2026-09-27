"""第 24 课：对话样本与损失掩码。运行：python demo.py"""

def lesson_24():
    import math
    tokens = ["<user>", "你好", "<assistant>", "你好！", "<eos>"]
    assistant_mask = [0, 0, 0, 1, 1]
    probabilities_of_actual_tokens = [0.9, 0.4, 0.8, 0.6, 0.7]
    supervised_loss = sum(-math.log(p) * m for p, m in zip(probabilities_of_actual_tokens, assistant_mask)) / sum(assistant_mask)
    print("token/监督位置:", list(zip(tokens, assistant_mask)))
    print("仅助手位置的平均损失:", round(supervised_loss, 4))
    assert sum(assistant_mask) == 2

if __name__ == '__main__':
    lesson_24()
