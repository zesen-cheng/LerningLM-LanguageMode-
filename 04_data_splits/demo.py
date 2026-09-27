"""第 04 课：训练、验证与测试。运行：python demo.py"""

def lesson_04():
    import hashlib
    documents = ["我喜欢苹果。", "他喜欢梨。", "今天下雨。", "明天晴天。"]
    train, validation, test = documents[:2], documents[2:3], documents[3:]
    digest = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    groups = [set(map(digest, part)) for part in (train, validation, test)]
    print("train/validation/test 文档数:", list(map(len, groups)))
    assert not (groups[0] & groups[1] or groups[0] & groups[2] or groups[1] & groups[2])

if __name__ == '__main__':
    lesson_04()
