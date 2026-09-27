"""第 44 课：结课：训练与恢复。运行：python demo.py"""

def lesson_44():
    import json
    import uuid
    from pathlib import Path
    checkpoint = Path(__file__).resolve().parent / f"_demo_checkpoint_{uuid.uuid4().hex}.json"
    try:
        state = {"step": 0, "weight": 0.0, "optimizer_momentum": 0.0}
        for _ in range(3):
            gradient = 2 * (state["weight"] - 1.0)
            state["optimizer_momentum"] = 0.5 * state["optimizer_momentum"] + gradient
            state["weight"] -= 0.1 * state["optimizer_momentum"]
            state["step"] += 1
        checkpoint.write_text(json.dumps(state), encoding="utf-8")
        resumed = json.loads(checkpoint.read_text(encoding="utf-8"))
        resumed["step"] += 1
        print("暂停检查点 step:", state["step"], "恢复后 step:", resumed["step"])
        assert resumed["step"] == 4
    finally:
        checkpoint.unlink(missing_ok=True)

if __name__ == '__main__':
    lesson_44()
