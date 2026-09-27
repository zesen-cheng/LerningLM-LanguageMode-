"""第 20 课：检查点与恢复。运行：python demo.py"""

def lesson_20():
    import json
    import uuid
    from pathlib import Path
    state = {"step": 3, "weight": 0.6, "optimizer_momentum": 0.2, "seed": 7}
    checkpoint = Path(__file__).resolve().parent / f"_demo_checkpoint_{uuid.uuid4().hex}.json"
    try:
        checkpoint.write_text(json.dumps(state), encoding="utf-8")
        restored = json.loads(checkpoint.read_text(encoding="utf-8"))
        restored["step"] += 1
        print("恢复到 step", state["step"], "并更新到", restored["step"])
        assert restored["optimizer_momentum"] == state["optimizer_momentum"]
    finally:
        checkpoint.unlink(missing_ok=True)

if __name__ == '__main__':
    lesson_20()
