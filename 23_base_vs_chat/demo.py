"""第 23 课：基础模型与聊天模型。运行：python demo.py"""

def lesson_23():
    prompt = "用户：你好\n助手："
    base_continuation = "你好\n小白：我也来了"
    sft_continuation = "你好！有什么我可以帮你的？"
    print("相同提示:", prompt)
    print("基础续写示意:", base_continuation)
    print("SFT 目标示意:", sft_continuation)
    assert "小白" not in sft_continuation

if __name__ == '__main__':
    lesson_23()
