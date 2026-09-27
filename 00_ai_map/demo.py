"""第 00 课：AI 的任务地图。运行：python demo.py"""

def lesson_00():
    systems = {"手写关键词规则": "AI/规则", "从邮件样本学习": "机器学习", "多层网络续写": "深度学习/生成式AI"}
    for name, group in systems.items():
        print(f"{name} -> {group}")
    assert systems["手写关键词规则"] != systems["从邮件样本学习"]

if __name__ == '__main__':
    lesson_00()
