"""根据本目录独立撰写的课文生成逐课笔记与索引。"""

from __future__ import annotations

import ast
import re
from pathlib import Path

from lesson_content import LESSONS
from lesson_details import TECHNICAL_DETAILS, render_technical_details


ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "demo_templates.py"
SLUGS = [
    "ai_map", "prediction_loop", "environment", "math_intuition",
    "data_splits", "loss_functions", "backpropagation", "optimizer_generalization",
    "token_ids", "embedding_position", "bigram_lm", "causal_attention",
    "transformer_block", "gpt_next_token", "sampling",
    "corpus_provenance", "cleaning_audit", "tokenizer_check", "training_plan",
    "tiny_gpt_training", "checkpoint_resume", "progress_monitoring", "base_model_eval",
    "base_vs_chat", "sft_masking", "sft_update", "sealed_eval",
    "preference_dpo", "rlhf_bandit", "posttrain_acceptance",
    "inference_artifacts", "http_json", "sse_stream", "tool_calling",
    "protocol_adapter", "gateway_controls", "end_to_end",
    "case_config", "case_data_tokenizer", "case_pretrain_eval", "case_sft_results",
    "case_evidence", "capstone_data", "capstone_tokenizer", "capstone_train_resume",
    "capstone_sft_eval", "capstone_gateway", "capstone_report",
]


def read_lessons() -> dict[int, tuple[str, str, str, str, str]]:
    if len(LESSONS) != 48:
        raise ValueError(f"expected 48 lessons, found {len(LESSONS)}")
    return dict(enumerate(LESSONS))


def read_technical_details() -> dict[int, tuple[str, str, str]]:
    if set(TECHNICAL_DETAILS) != set(range(48)):
        raise ValueError("technical detail IDs must cover lessons 00–47 exactly")
    for number, parts in TECHNICAL_DETAILS.items():
        if not isinstance(parts, tuple) or len(parts) != 3 or not all(
            isinstance(part, str) and part.strip() for part in parts
        ):
            raise ValueError(f"invalid technical details for lesson {number:02d}")
    return TECHNICAL_DETAILS


def read_demos() -> dict[int, str]:
    source = TEMPLATES.read_text(encoding="utf-8")
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    demos = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and re.fullmatch(r"lesson_\d{2}", node.name):
            number = int(node.name[-2:])
            demos[number] = "".join(lines[node.lineno - 1:node.end_lineno])
    if set(demos) != set(range(48)):
        raise ValueError(f"demo IDs differ: {set(range(48)) - set(demos)}")
    return demos


def write_new_or_identical(path: Path, content: str, force: bool = False) -> None:
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            if not force:
                raise FileExistsError(f"existing edited file: {path}; use --force after review")
            path.write_text(content, encoding="utf-8", newline="\n")
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def build(force: bool = False) -> None:
    lessons = read_lessons()
    details = read_technical_details()
    demos = read_demos()
    index = ["# 从零训练语言模型：逐课索引", "", "每课都有独立撰写的 `notes.md` 与可运行的 `demo.py`，并补充技术机制、实践步骤、检查与常见错误；每个主题末尾都设有解答与复习时间。", "", "先读[项目复盘与学习价值](TRAINING_STORY.md)，了解为什么训练这个模型、实际技术流程以及能迁移的方法。"]
    ranges = [
        (0, 14, "基础知识与 GPT", "01_foundations.md", "token 是切分后的单位；tokenizer 是编码规则。32K 词表不等于 32K 上下文。"),
        (15, 22, "预训练", "02_pretraining.md", "step 是一次参数更新；checkpoint 保存可恢复状态；KV cache 用于推理复用。"),
        (23, 29, "后训练", "03_posttraining.md", "SFT 学示范回答；DPO 学离线偏好；在线 RL 根据奖励更新策略。"),
        (30, 36, "推理与网关", "04_serving.md", "模型提出工具调用，宿主程序验证并执行；推理服务与网关各有职责。"),
        (37, 41, "真实案例", "05_case.md", "将配置、日志、评估与失败样本合在一起，才能解释 0.2B 实验。"),
        (42, 47, "学员结课", "06_capstone.md", "先封存评估，再训练、恢复、对比和报告。"),
    ]
    review_by_end = {end: (review, recap) for _, end, _, review, recap in ranges}
    for number in range(48):
        title, concept, example, question, answer = lessons[number]
        directory = ROOT / f"{number:02d}_{SLUGS[number]}"
        directory.mkdir(exist_ok=True)
        for start, _, heading, _, _ in ranges:
            if number == start:
                index.extend(["", f"## {heading}", ""])
        index.append(f"- [{number:02d}｜{title}]({directory.name}/notes.md) · [运行代码]({directory.name}/demo.py)")
        if number in review_by_end:
            review, recap = review_by_end[number]
            index.extend(["", "### 解答与复习时间", "", f"先回答本主题关键问题：{recap}", "", f"[进入完整问答、自测与答案](reviews/{review})", ""])
        notes = (
            f"# {number:02d}｜{title}\n\n"
            f"## 核心概念\n\n{concept}\n\n"
            f"## 观察一个例子\n\n{example}\n\n"
            f"{render_technical_details(number)}"
            f"## 自问自答\n\n**问：{question}**\n\n答：{answer}\n\n"
            f"## 代码演示\n\n在本目录运行 `python demo.py`。演示只用 Python 标准库；"
            f"玩具实验用于解释机制，不代表真实 0.2B 模型成绩。\n\n"
            f"学完本主题的全部课程，请回到[课程索引](../course_plan.md)进入主题末尾的“解答与复习时间”。\n"
        )
        demo = (
            f'"""第 {number:02d} 课：{title}。运行：python demo.py"""\n\n'
            + demos[number].rstrip()
            + f"\n\nif __name__ == '__main__':\n    lesson_{number:02d}()\n"
        )
        write_new_or_identical(directory / "notes.md", notes, force=force)
        write_new_or_identical(directory / "demo.py", demo, force=force)
    write_new_or_identical(ROOT / "course_plan.md", "\n".join(index).rstrip() + "\n", force=force)
    print(f"generated=48 notes=48 demos=48 technical_details={len(details)} reviews=6")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="replace generated lesson notes/demo files and index")
    build(force=parser.parse_args().force)
