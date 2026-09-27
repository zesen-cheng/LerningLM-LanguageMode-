"""第 15 课：语料来源与许可。运行：python demo.py"""

def lesson_15():
    import hashlib
    import json
    text = "我喜欢苹果。\n"
    manifest = {"source": "课程自写示例", "license": "课程内部示例", "bytes": len(text.encode("utf-8")), "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    assert len(manifest["sha256"]) == 64

if __name__ == '__main__':
    lesson_15()
