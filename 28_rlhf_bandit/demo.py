"""第 28 课：RLHF 与在线强化学习。运行：python demo.py"""

def lesson_28():
    import math
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    logit = 0.0
    rewards = {"答对": 1.0, "答错": 0.0}
    before = sigmoid(logit)
    for _ in range(10):
        probability = sigmoid(logit)
        expected_policy_gradient = probability * (1 - probability) * (rewards["答对"] - rewards["答错"])
        logit += 0.3 * expected_policy_gradient
    print("两动作策略中答对概率:", round(before, 3), "->", round(sigmoid(logit), 3))
    print("这是期望奖励玩具更新，不是完整 PPO/GRPO 训练")
    assert sigmoid(logit) > before

if __name__ == '__main__':
    lesson_28()
