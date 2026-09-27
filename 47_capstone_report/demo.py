"""第 47 课：结课：展示与边界。运行：python demo.py"""

def lesson_47():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    lessons = sorted(path for path in root.iterdir() if path.is_dir() and path.name[:2].isdigit())
    ready = [path for path in lessons if (path / "notes.md").is_file() and (path / "demo.py").is_file()]
    print("课程目录/含讲义与代码的目录:", len(lessons), len(ready))
    assert len(ready) == 48

if __name__ == '__main__':
    lesson_47()
