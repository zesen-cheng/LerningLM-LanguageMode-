"""第 27 课：偏好数据与 DPO。运行：python demo.py"""

def lesson_27():
    import math
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    preference_logit = 0.0
    reference_gap = 0.0
    beta = 1.0
    before = sigmoid(preference_logit)
    for _ in range(10):
        margin = beta * (preference_logit - reference_gap)
        gradient = -beta * (1 - sigmoid(margin))  # -log sigmoid(margin)
        preference_logit -= 0.2 * gradient
    print("DPO 玩具偏好边际概率:", round(before, 3), "->", round(sigmoid(preference_logit), 3))
    assert sigmoid(preference_logit) > before

if __name__ == '__main__':
    lesson_27()
