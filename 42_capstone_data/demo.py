"""第 42 课：结课：选择可完成的任务。运行：python demo.py"""

def lesson_42():
    import hashlib
    documents = ["我喜欢苹果。", "我喜欢梨。", "他喜欢香蕉。", "她喜欢葡萄。"]
    train, validation, sealed = documents[:2], documents[2:3], documents[3:]
    fingerprints = [set(hashlib.sha256(item.encode()).hexdigest() for item in part) for part in (train, validation, sealed)]
    print("自写数据 train/val/sealed 数量:", [len(part) for part in (train, validation, sealed)])
    assert not (fingerprints[0] & fingerprints[1] or fingerprints[0] & fingerprints[2])

if __name__ == '__main__':
    lesson_42()
