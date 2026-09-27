"""第 38 课：案例：数据与 tokenizer。运行：python demo.py"""

def lesson_38():
    import re
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    report = project / "data_scaleup/quality_audit/final_2b_clean_acceptance_report.md"
    if not report.exists():
        print("案例验收报告未找到")
        return
    text = report.read_text(encoding="utf-8")
    count = int(re.search(r"全量扫描 tokens：([\d,]+)", text).group(1).replace(",", ""))
    print("全量机械扫描 token:", count)
    print("近重复限制记录:", "不等价于全量 MinHash 证明" in text)
    assert count > 1_900_000_000

if __name__ == '__main__':
    lesson_38()
