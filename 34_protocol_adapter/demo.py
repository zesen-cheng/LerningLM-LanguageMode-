"""第 34 课：协议适配。运行：python demo.py"""

def lesson_34():
    openai_style = {"messages": [{"role": "system", "content": "简短回答"}, {"role": "user", "content": "你好"}]}
    system = next(item["content"] for item in openai_style["messages"] if item["role"] == "system")
    messages = [item for item in openai_style["messages"] if item["role"] != "system"]
    anthropic_style = {"system": system, "messages": messages, "max_tokens": 32}
    print("教学用角色字段映射:", anthropic_style)
    print("真实网关仍需处理流式事件、工具、错误等差异")
    assert anthropic_style["system"] == "简短回答"

if __name__ == '__main__':
    lesson_34()
