"""第 39 课：案例：预训练与基础评估。运行：python demo.py"""

def lesson_39():
    import re
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    report = project / "evaluations/gpt_0p2b_32k_pretrain_2b_v1_final/ASSESSMENT.md"
    if not report.exists():
        print("基础评估报告未找到")
        return
    text = report.read_text(encoding="utf-8")
    losses = [float(x) for x in re.findall(r"step \d+：loss ([\d.]+)", text)]
    print("固定验证 loss 序列:", losses)
    print("可直接聊天成品:", "不是可直接对话的成品" not in text)
    assert losses and losses[-1] < losses[0]

if __name__ == '__main__':
    lesson_39()
