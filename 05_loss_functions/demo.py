"""第 05 课：损失函数与任务。运行：python demo.py"""

def lesson_05():
    import math
    true_token = "苹果"
    candidates = {"苹果": 0.8, "梨": 0.15, "香蕉": 0.05}
    loss = -math.log(candidates[true_token])
    worse_loss = -math.log(0.05)
    print("正确 token 概率 0.8 的 loss:", round(loss, 4))
    print("正确 token 概率 0.05 的 loss:", round(worse_loss, 4))
    assert loss < worse_loss

if __name__ == '__main__':
    lesson_05()
