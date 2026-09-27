"""第 40 课：案例：SFT 收益与回退。运行：python demo.py"""

def lesson_40():
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    reports = [project / f"evaluations/stage{i}_v1/ASSESSMENT.md" for i in (4, 5, 6)]
    available = {path.parent.name: path.exists() for path in reports}
    print("SFT 阶段报告:", available)
    if all(available.values()):
        stage4 = reports[0].read_text(encoding="utf-8")
        stage6 = reports[2].read_text(encoding="utf-8")
        print("Stage4 自动规则 42/80:", "42/80" in stage4)
        print("Stage6 未升级:", "均不升级" in stage6)
        assert "42/80" in stage4 and "均不升级" in stage6

if __name__ == '__main__':
    lesson_40()
