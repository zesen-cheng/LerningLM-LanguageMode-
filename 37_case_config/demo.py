"""第 37 课：案例：设备、配置与目标。运行：python demo.py"""

def lesson_37():
    import json
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    path = project / "outputs/runs/gpt_0p2b_32k_pretrain_2b_v1/config.json"
    if not path.exists():
        print("案例配置未找到；复制课程时请同步案例资料")
        return
    config = json.loads(path.read_text(encoding="utf-8"))
    processed_positions = config["max_steps"] * config["batch_size"] * config["gradient_accumulation_steps"] * config["block_size"]
    print("词表/上下文/层数:", config["model"]["vocab_size"], config["block_size"], config["model"]["n_layer"])
    print("按配置估算训练位置数:", processed_positions)
    assert config["model"]["vocab_size"] == 32768

if __name__ == '__main__':
    lesson_37()
