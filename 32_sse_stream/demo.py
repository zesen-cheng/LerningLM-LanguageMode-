"""第 32 课：流式输出与 SSE。运行：python demo.py"""

def lesson_32():
    import json
    events = [
        {"type": "response.output_text.delta", "delta": "你"},
        {"type": "response.output_text.delta", "delta": "好"},
        {"type": "response.completed"},
    ]
    wire = "".join("data: " + json.dumps(event, ensure_ascii=False) + "\n\n" for event in events)
    decoded = [json.loads(chunk[6:]) for chunk in wire.strip().split("\n\n")]
    text = "".join(item.get("delta", "") for item in decoded)
    print("SSE 事件数:", len(decoded), "拼接文本:", text, "结束:", decoded[-1]["type"])
    assert text == "你好" and decoded[-1]["type"] == "response.completed"

if __name__ == '__main__':
    lesson_32()
