"""第 02 课：实验环境与可复现。运行：python demo.py"""

def lesson_02():
    import platform
    import sys
    print("Python:", sys.version.split()[0])
    print("系统:", platform.system())
    print("本课计算:", 1 + 2)
    assert sys.version_info >= (3, 9)

if __name__ == '__main__':
    lesson_02()
