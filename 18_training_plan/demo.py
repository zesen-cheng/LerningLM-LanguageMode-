"""第 18 课：预训练实验设计。运行：python demo.py"""

def lesson_18():
    micro_batch, accumulation, devices, context, steps = 2, 8, 1, 1024, 100
    effective_sequences = micro_batch * accumulation * devices
    positions = effective_sequences * context * steps
    print("有效 batch 序列数:", effective_sequences, "处理位置数:", positions)
    assert positions == 1_638_400

if __name__ == '__main__':
    lesson_18()
