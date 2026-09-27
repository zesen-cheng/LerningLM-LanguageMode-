"""第 21 课：训练监控与异常。运行：python demo.py"""

def lesson_21():
    import json
    import uuid
    from pathlib import Path
    root = Path(__file__).resolve().parent
    tag = uuid.uuid4().hex
    status_path, metrics_path = root / f"_demo_{tag}_status.json", root / f"_demo_{tag}_metrics.jsonl"
    try:
        status_path.write_text(json.dumps({"state": "running", "step": 2}), encoding="utf-8")
        with metrics_path.open("w", encoding="utf-8") as handle:
            for step, loss in ((1, 2.4), (2, 2.1)):
                handle.write(json.dumps({"step": step, "loss": loss}) + "\n")
        status = json.loads(status_path.read_text(encoding="utf-8"))
        metrics = [json.loads(line) for line in metrics_path.read_text(encoding="utf-8").splitlines()]
        print("状态:", status, "最近指标:", metrics[-1])
        assert status["step"] == metrics[-1]["step"]
    finally:
        status_path.unlink(missing_ok=True)
        metrics_path.unlink(missing_ok=True)

if __name__ == '__main__':
    lesson_21()
