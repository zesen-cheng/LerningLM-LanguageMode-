"""第 33 课：结构化输出与工具调用。运行：python demo.py"""

def lesson_33():
    import json
    tools = {"add": lambda a, b: a + b}
    model_request = {"name": "add", "arguments": {"a": 2, "b": 3}, "call_id": "call_1"}
    name, args = model_request["name"], model_request["arguments"]
    if name not in tools or not all(isinstance(args.get(k), int) for k in ("a", "b")):
        raise ValueError("工具名或参数不合法")
    tool_result = tools[name](**args)  # 应用执行，不是模型自己执行
    reply = {"call_id": model_request["call_id"], "output": str(tool_result)}
    print("工具执行结果回传:", json.dumps(reply, ensure_ascii=False))
    assert reply["output"] == "5"

if __name__ == '__main__':
    lesson_33()
