"""第 41 课：案例：证据链。运行：python demo.py"""

def lesson_41():
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    evidence = {
        "配置": project / "outputs/runs/gpt_0p2b_32k_pretrain_2b_v1/config.json",
        "基础评估": project / "evaluations/gpt_0p2b_32k_pretrain_2b_v1_final/ASSESSMENT.md",
        "SFT评估": project / "evaluations/stage6_v1/ASSESSMENT.md",
    }
    print("复盘证据矩阵:", {name: path.exists() for name, path in evidence.items()})
    print("在线 RL 和通用网关实作不列为已完成事实")

if __name__ == '__main__':
    lesson_41()
