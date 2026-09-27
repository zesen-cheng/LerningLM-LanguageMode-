"""第 30 课：推理模型文件。运行：python demo.py"""

def lesson_30():
    import json
    import uuid
    from pathlib import Path
    root = Path(__file__).resolve().parent
    tag = uuid.uuid4().hex
    payloads = {"config": {"vocab_size": 4, "context": 8}, "tokenizer": {"我": 0, "喜": 1}, "weights": {"transition": [1, 0]}}
    paths = {name: root / f"_demo_{tag}_{name}.json" for name in payloads}
    try:
        for name, path in paths.items():
            path.write_text(json.dumps(payloads[name], ensure_ascii=False), encoding="utf-8")
        print("推理加载前工件检查:", {name: path.exists() for name, path in paths.items()})
        assert all(path.exists() for path in paths.values())
    finally:
        for path in paths.values():
            path.unlink(missing_ok=True)

if __name__ == '__main__':
    lesson_30()
