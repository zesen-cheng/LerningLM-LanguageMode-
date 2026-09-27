"""第 16 课：清洗、去重与审计。运行：python demo.py"""

def lesson_16():
    raw = ["我喜欢苹果。", "  我喜欢苹果。  ", "", "乱码�文本", "他喜欢梨。"]
    seen, clean, rejected = set(), [], []
    for item in raw:
        item = item.strip()
        reason = "empty" if not item else "decode_noise" if "�" in item else "duplicate" if item in seen else None
        if reason:
            rejected.append(reason)
        else:
            seen.add(item)
            clean.append(item)
    print("保留:", clean, "拒绝原因:", rejected)
    assert len(clean) == 2

if __name__ == '__main__':
    lesson_16()
