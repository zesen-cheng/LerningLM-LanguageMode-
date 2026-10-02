"""检查 48 课、六个主题复习页与离线演示。"""

from __future__ import annotations

import subprocess
import sys
import os
import re
from pathlib import Path

from build_course import SLUGS, read_demos, read_lessons, read_technical_details
from lesson_details import render_technical_details


def main() -> int:
    root = Path(__file__).resolve().parent
    lessons = read_lessons()
    details = read_technical_details()
    demos = read_demos()
    failures = []
    passed = 0
    technical_passed = 0
    review_dir = root / "reviews"
    reviews = sorted(review_dir.glob("*.md"))
    index = (root / "course_plan.md").read_text(encoding="utf-8")
    if len(reviews) != 6 or index.count("### 解答与复习时间") != 6:
        failures.append("review sections: expected 6 files and 6 index headings")
    for review in reviews:
        if "## 自测" not in review.read_text(encoding="utf-8"):
            failures.append(f"missing self-test: {review.name}")
        if f"reviews/{review.name}" not in index:
            failures.append(f"unlinked review: {review.name}")
    for document in [*root.glob("*.md"), *reviews, *root.glob("[0-9][0-9]_*/notes.md")]:
        document_text = document.read_text(encoding="utf-8")
        if "modern-ai-course" in document_text:
            failures.append(f"legacy reference: {document.name}")
        for match in re.finditer(r"\]\(([^)]+)\)", document_text):
            target = match.group(1).split("#", 1)[0]
            if target and not target.startswith(("http://", "https://", "/")) and not (document.parent / target).exists():
                failures.append(f"broken document link: {document.name} -> {target}")
    for number, slug in enumerate(SLUGS):
        directory = root / f"{number:02d}_{slug}"
        notes = directory / "notes.md"
        demo = directory / "demo.py"
        if not notes.is_file() or not demo.is_file():
            failures.append(f"{number:02d}: missing notes/demo")
            continue
        text = notes.read_text(encoding="utf-8")
        if lessons[number][0] not in text or lessons[number][2] not in text or "## 代码演示" not in text:
            failures.append(f"{number:02d}: notes content mismatch")
            continue
        if text.count("## 技术细节与实践流程") != 1 or render_technical_details(number) not in text:
            failures.append(f"{number:02d}: technical details missing or out of date")
            continue
        technical_passed += 1
        broken = []
        for match in re.finditer(r"\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if target and not target.startswith(("http://", "https://", "/")) and not (directory / target).exists():
                broken.append(target)
        if broken:
            failures.append(f"{number:02d}: broken links {broken}")
            continue
        if f"def lesson_{number:02d}" not in demo.read_text(encoding="utf-8"):
            failures.append(f"{number:02d}: demo mismatch")
            continue
        try:
            result = subprocess.run(
                [sys.executable, str(demo)],
                cwd=directory,
                text=True,
                encoding="utf-8",
                errors="replace",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                capture_output=True,
                timeout=15,
                check=False,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{number:02d}: timeout")
            continue
        if result.returncode:
            failures.append(f"{number:02d}: exit={result.returncode} {result.stderr.strip()[-250:]}")
        else:
            passed += 1
    print(f"lessons={len(lessons)} demo_templates={len(demos)} passed={passed} technical_details={technical_passed}/{len(details)} reviews={len(reviews)} failed={len(failures)}")
    for failure in failures:
        print(failure)
    return 0 if len(lessons) == 48 and len(demos) == 48 and passed == 48 and technical_passed == 48 and len(reviews) == 6 and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
