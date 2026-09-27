"""每个 lesson_NN 都会被拆成对应课程目录内的独立 demo.py。"""


def lesson_00():
    systems = {"手写关键词规则": "AI/规则", "从邮件样本学习": "机器学习", "多层网络续写": "深度学习/生成式AI"}
    for name, group in systems.items():
        print(f"{name} -> {group}")
    assert systems["手写关键词规则"] != systems["从邮件样本学习"]


def lesson_01():
    from collections import Counter
    texts = ["我喜欢苹果", "我喜欢梨", "他喜欢苹果"]
    next_words = Counter(text.split("喜欢")[1] for text in texts)
    print("训练样本之后的预测计数:", dict(next_words))
    next_words.update(["梨"])
    print("加入新样本后的计数:", dict(next_words))
    assert next_words["苹果"] == next_words["梨"] == 2


def lesson_02():
    import platform
    import sys
    print("Python:", sys.version.split()[0])
    print("系统:", platform.system())
    print("本课计算:", 1 + 2)
    assert sys.version_info >= (3, 9)


def lesson_03():
    import math
    vector = [1.0, 2.0]
    weights = [0.5, -0.25]
    score = sum(a * b for a, b in zip(vector, weights))
    logits = [score, 0.0]
    probabilities = [math.exp(x) / sum(math.exp(y) for y in logits) for x in logits]
    print("标量分数:", score, "概率向量:", probabilities)
    assert abs(sum(probabilities) - 1.0) < 1e-12


def lesson_04():
    import hashlib
    documents = ["我喜欢苹果。", "他喜欢梨。", "今天下雨。", "明天晴天。"]
    train, validation, test = documents[:2], documents[2:3], documents[3:]
    digest = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    groups = [set(map(digest, part)) for part in (train, validation, test)]
    print("train/validation/test 文档数:", list(map(len, groups)))
    assert not (groups[0] & groups[1] or groups[0] & groups[2] or groups[1] & groups[2])


def lesson_05():
    import math
    true_token = "苹果"
    candidates = {"苹果": 0.8, "梨": 0.15, "香蕉": 0.05}
    loss = -math.log(candidates[true_token])
    worse_loss = -math.log(0.05)
    print("正确 token 概率 0.8 的 loss:", round(loss, 4))
    print("正确 token 概率 0.05 的 loss:", round(worse_loss, 4))
    assert loss < worse_loss


def lesson_06():
    x, target = 2.0, 3.0
    w1 = w2 = 1.0
    hidden = max(0.0, w1 * x)
    prediction = w2 * hidden
    before = (prediction - target) ** 2 / 2
    d_w2 = (prediction - target) * hidden
    d_w1 = (prediction - target) * w2 * x
    w1 -= 0.1 * d_w1
    w2 -= 0.1 * d_w2
    after = (w2 * max(0.0, w1 * x) - target) ** 2 / 2
    print("一次反向传播前后 loss:", round(before, 4), round(after, 4))
    assert after < before


def lesson_07():
    target = 3.0
    for rate in (0.1, 1.2):
        weight = 0.0
        history = []
        for _ in range(5):
            history.append(round((weight - target) ** 2, 3))
            weight -= rate * 2 * (weight - target)
        print(f"学习率 {rate}: loss={history}")
    assert (0.0 - target) ** 2 > (0.0 + 0.1 * 2 * target - target) ** 2


def lesson_08():
    text = "我喜欢苹果。"
    vocabulary = {char: i for i, char in enumerate(sorted(set(text)))}
    ids = [vocabulary[char] for char in text]
    inverse = {i: char for char, i in vocabulary.items()}
    recovered = "".join(inverse[i] for i in ids)
    print("字符:", list(text), "ID:", ids, "还原:", recovered)
    assert recovered == text


def lesson_09():
    embeddings = {"猫": [1.0, 0.0], "追": [0.0, 1.0], "狗": [0.5, 0.5]}
    positions = [[0.0, 0.1], [0.1, 0.0], [0.2, 0.0]]
    encode = lambda words: [[a + b for a, b in zip(embeddings[word], positions[i])] for i, word in enumerate(words)]
    cat_chases_dog = encode(["猫", "追", "狗"])
    dog_chases_cat = encode(["狗", "追", "猫"])
    print("猫追狗首位置:", cat_chases_dog[0], "狗追猫首位置:", dog_chases_cat[0])
    assert cat_chases_dog != dog_chases_cat


def lesson_10():
    from collections import Counter, defaultdict
    corpus = ["我喜欢苹果", "我喜欢梨", "他喜欢苹果"]
    counts = defaultdict(Counter)
    for sentence in corpus:
        for a, b in zip(sentence, sentence[1:]):
            counts[a][b] += 1
    print("'欢' 后接 token 分布:", dict(counts["欢"]))
    print("'苹' 后接 token 分布:", dict(counts["苹"]))
    assert counts["苹"]["果"] == 2


def lesson_11():
    import math
    values = [1.0, 2.0, 4.0]
    for position in range(len(values)):
        visible = values[:position + 1]  # 因果遮罩：只看当前位置及之前
        scores = [values[position] * key for key in visible]
        scale = max(scores)
        weights = [math.exp(s - scale) for s in scores]
        weights = [w / sum(weights) for w in weights]
        context = sum(w * v for w, v in zip(weights, visible))
        print(f"位置 {position}: 可见={visible}, 汇总={context:.3f}")
    assert len(values[:1]) == 1


def lesson_12():
    import math
    x = [1.0, 2.0]
    head_a = [0.75 * x[0] + 0.25 * x[1]] * 2
    head_b = [0.25 * x[0] + 0.75 * x[1]] * 2
    residual = [x[i] + head_a[i] + head_b[i] for i in range(2)]
    mean = sum(residual) / len(residual)
    variance = sum((v - mean) ** 2 for v in residual) / len(residual)
    normalized = [(v - mean) / math.sqrt(variance + 1e-5) for v in residual]
    print("双头汇总 + 残差 + 归一化:", [round(v, 3) for v in normalized])
    assert len(normalized) == len(x)


def lesson_13():
    transition = {"我": "喜", "喜": "欢", "欢": "苹", "苹": "果", "果": "。"}
    output = "我"
    for _ in range(5):
        output += transition[output[-1]]
    print("逐 token 自回归生成:", output)
    assert output == "我喜欢苹果。"


def lesson_14():
    import math
    logits = {"苹果": 2.0, "梨": 1.0, "香蕉": 0.0}
    for temperature in (0.5, 1.0, 2.0):
        weights = {k: math.exp(v / temperature) for k, v in logits.items()}
        total = sum(weights.values())
        print(f"温度 {temperature}: 苹果概率={weights['苹果'] / total:.3f}")
    top2 = sorted(logits, key=logits.get, reverse=True)[:2]
    print("top-k=2 的候选:", top2)
    assert "香蕉" not in top2


def lesson_15():
    import hashlib
    import json
    text = "我喜欢苹果。\n"
    manifest = {"source": "课程自写示例", "license": "课程内部示例", "bytes": len(text.encode("utf-8")), "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    assert len(manifest["sha256"]) == 64


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


def lesson_17():
    text = "我喜欢苹果。"
    vocabulary = ["我", "喜欢", "苹果", "。"]
    ids = []
    remaining = text
    while remaining:
        match = next(token for token in sorted(vocabulary, key=len, reverse=True) if remaining.startswith(token))
        ids.append(vocabulary.index(match))
        remaining = remaining[len(match):]
    recovered = "".join(vocabulary[i] for i in ids)
    print("玩具子词 ID:", ids, "还原:", recovered)
    assert recovered == text


def lesson_18():
    micro_batch, accumulation, devices, context, steps = 2, 8, 1, 1024, 100
    effective_sequences = micro_batch * accumulation * devices
    positions = effective_sequences * context * steps
    print("有效 batch 序列数:", effective_sequences, "处理位置数:", positions)
    assert positions == 1_638_400


def lesson_19():
    import math
    sequence = [0, 1, 2, 3, 0, 1, 2, 3]
    vocab = 4
    weights = [[0.0] * vocab for _ in range(vocab)]
    pairs = list(zip(sequence, sequence[1:]))
    def nll():
        return sum(-math.log(math.exp(weights[a][b]) / sum(math.exp(v) for v in weights[a])) for a, b in pairs) / len(pairs)
    before = nll()
    for _ in range(60):
        for a, b in pairs:
            probs = [math.exp(x) / sum(math.exp(z) for z in weights[a]) for x in weights[a]]
            for j in range(vocab):
                weights[a][j] -= 0.2 * (probs[j] - (j == b))
    after = nll()
    print("真实参数更新前后 NLL:", round(before, 4), round(after, 4))
    assert after < before


def lesson_20():
    import json
    import uuid
    from pathlib import Path
    state = {"step": 3, "weight": 0.6, "optimizer_momentum": 0.2, "seed": 7}
    checkpoint = Path(__file__).resolve().parent / f"_demo_checkpoint_{uuid.uuid4().hex}.json"
    try:
        checkpoint.write_text(json.dumps(state), encoding="utf-8")
        restored = json.loads(checkpoint.read_text(encoding="utf-8"))
        restored["step"] += 1
        print("恢复到 step", state["step"], "并更新到", restored["step"])
        assert restored["optimizer_momentum"] == state["optimizer_momentum"]
    finally:
        checkpoint.unlink(missing_ok=True)


def lesson_21():
    import json
    import uuid
    from pathlib import Path
    root = Path(__file__).resolve().parent
    tag = uuid.uuid4().hex
    status_path, metrics_path = root / f"_demo_{tag}_status.json", root / f"_demo_{tag}_metrics.jsonl"
    try:
        status_path.write_text(json.dumps({"state": "running", "step": 2}), encoding="utf-8")
        with metrics_path.open("w", encoding="utf-8") as handle:
            for step, loss in ((1, 2.4), (2, 2.1)):
                handle.write(json.dumps({"step": step, "loss": loss}) + "\n")
        status = json.loads(status_path.read_text(encoding="utf-8"))
        metrics = [json.loads(line) for line in metrics_path.read_text(encoding="utf-8").splitlines()]
        print("状态:", status, "最近指标:", metrics[-1])
        assert status["step"] == metrics[-1]["step"]
    finally:
        status_path.unlink(missing_ok=True)
        metrics_path.unlink(missing_ok=True)


def lesson_22():
    import math
    from collections import Counter, defaultdict
    train = ["我喜欢苹果", "我喜欢梨"]
    validation = "他喜欢苹果"
    counts = defaultdict(Counter)
    for sentence in train:
        for a, b in zip(sentence, sentence[1:]):
            counts[a][b] += 1
    vocabulary = set("".join(train) + validation)
    losses = [-math.log((counts[a][b] + 1) / (sum(counts[a].values()) + len(vocabulary))) for a, b in zip(validation, validation[1:])]
    print("未见句子的平均 NLL:", round(sum(losses) / len(losses), 4))
    assert len(losses) == len(validation) - 1


def lesson_23():
    prompt = "用户：你好\n助手："
    base_continuation = "你好\n小白：我也来了"
    sft_continuation = "你好！有什么我可以帮你的？"
    print("相同提示:", prompt)
    print("基础续写示意:", base_continuation)
    print("SFT 目标示意:", sft_continuation)
    assert "小白" not in sft_continuation


def lesson_24():
    import math
    tokens = ["<user>", "你好", "<assistant>", "你好！", "<eos>"]
    assistant_mask = [0, 0, 0, 1, 1]
    probabilities_of_actual_tokens = [0.9, 0.4, 0.8, 0.6, 0.7]
    supervised_loss = sum(-math.log(p) * m for p, m in zip(probabilities_of_actual_tokens, assistant_mask)) / sum(assistant_mask)
    print("token/监督位置:", list(zip(tokens, assistant_mask)))
    print("仅助手位置的平均损失:", round(supervised_loss, 4))
    assert sum(assistant_mask) == 2


def lesson_25():
    import math
    score = 0.0  # 选择“简短回答”的 logit
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    before = sigmoid(score)
    for _ in range(12):
        score -= 0.3 * (sigmoid(score) - 1.0)  # SFT: 目标是简短回答
    after = sigmoid(score)
    print("SFT 玩具模型中目标回答概率:", round(before, 3), "->", round(after, 3))
    assert after > before


def lesson_26():
    sealed = [
        ("三项建议", lambda text: text.count("；") == 2),
        ("不要编造姓名", lambda text: "不知道" in text),
    ]
    baseline = ["先规划；再执行；最后复盘", "不知道你的姓名"]
    candidate = ["先规划；再执行；最后复盘", "你叫小白"]
    score = lambda outputs: [check(text) for (_, check), text in zip(sealed, outputs)]
    print("固定测试 基线:", score(baseline), "候选:", score(candidate))
    assert sum(score(candidate)) < sum(score(baseline))


def lesson_27():
    import math
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    preference_logit = 0.0
    reference_gap = 0.0
    beta = 1.0
    before = sigmoid(preference_logit)
    for _ in range(10):
        margin = beta * (preference_logit - reference_gap)
        gradient = -beta * (1 - sigmoid(margin))  # -log sigmoid(margin)
        preference_logit -= 0.2 * gradient
    print("DPO 玩具偏好边际概率:", round(before, 3), "->", round(sigmoid(preference_logit), 3))
    assert sigmoid(preference_logit) > before


def lesson_28():
    import math
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    logit = 0.0
    rewards = {"答对": 1.0, "答错": 0.0}
    before = sigmoid(logit)
    for _ in range(10):
        probability = sigmoid(logit)
        expected_policy_gradient = probability * (1 - probability) * (rewards["答对"] - rewards["答错"])
        logit += 0.3 * expected_policy_gradient
    print("两动作策略中答对概率:", round(before, 3), "->", round(sigmoid(logit), 3))
    print("这是期望奖励玩具更新，不是完整 PPO/GRPO 训练")
    assert sigmoid(logit) > before


def lesson_29():
    tests = {"正常学习请求": True, "隐私请求处理": True, "多轮人物归属": False}
    accepted = all(tests.values())
    print("各项验收:", tests)
    print("是否升级默认模型:", accepted)
    assert not accepted


def lesson_30():
    import json
    import uuid
    from pathlib import Path
    root = Path(__file__).resolve().parent
    tag = uuid.uuid4().hex
    payloads = {"config": {"vocab_size": 4, "context": 8}, "tokenizer": {"我": 0, "喜": 1}, "weights": {"transition": [1, 0]}}
    paths = {name: root / f"_demo_{tag}_{name}.json" for name in payloads}
    try:
        for name, path in paths.items():
            path.write_text(json.dumps(payloads[name], ensure_ascii=False), encoding="utf-8")
        print("推理加载前工件检查:", {name: path.exists() for name, path in paths.items()})
        assert all(path.exists() for path in paths.values())
    finally:
        for path in paths.values():
            path.unlink(missing_ok=True)


def lesson_31():
    import json
    request = {"method": "POST", "path": "/generate", "body": {"prompt": "我喜欢", "max_new_tokens": 2}}
    def handle(req):
        if req["method"] != "POST" or req["path"] != "/generate":
            return 404, {"error": "not_found"}
        if not isinstance(req["body"].get("prompt"), str):
            return 400, {"error": "invalid_prompt"}
        return 200, {"text": req["body"]["prompt"] + "苹果"}
    status, body = handle(request)
    print("本机无端口 HTTP/JSON 处理逻辑:", status, json.dumps(body, ensure_ascii=False))
    assert (status, body["text"]) == (200, "我喜欢苹果")


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


def lesson_34():
    openai_style = {"messages": [{"role": "system", "content": "简短回答"}, {"role": "user", "content": "你好"}]}
    system = next(item["content"] for item in openai_style["messages"] if item["role"] == "system")
    messages = [item for item in openai_style["messages"] if item["role"] != "system"]
    anthropic_style = {"system": system, "messages": messages, "max_tokens": 32}
    print("教学用角色字段映射:", anthropic_style)
    print("真实网关仍需处理流式事件、工具、错误等差异")
    assert anthropic_style["system"] == "简短回答"


def lesson_35():
    keys = {"course-key": "student"}
    quota = {"student": 2}
    def authorize(key):
        identity = keys.get(key)
        if identity is None:
            return 401
        if quota[identity] <= 0:
            return 429
        quota[identity] -= 1
        return 200
    statuses = [authorize("wrong"), authorize("course-key"), authorize("course-key"), authorize("course-key")]
    print("鉴权/限流状态码:", statuses)
    assert statuses == [401, 200, 200, 429]


def lesson_36():
    request = {"model": "toy-model", "messages": [{"role": "user", "content": "你好"}], "request_id": "demo-1"}
    routes = {"toy-model": "deterministic-mock"}
    backend = routes[request["model"]]
    generated = "你好" if backend == "deterministic-mock" else "未实现"
    response = {"request_id": request["request_id"], "backend": backend, "text": generated}
    print("客户端→网关→模拟后端→客户端:", response)
    assert response["backend"] == "deterministic-mock"


def lesson_37():
    import json
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    path = project / "outputs/runs/gpt_0p2b_32k_pretrain_2b_v1/config.json"
    if not path.exists():
        print("案例配置未找到；复制课程时请同步案例资料")
        return
    config = json.loads(path.read_text(encoding="utf-8"))
    processed_positions = config["max_steps"] * config["batch_size"] * config["gradient_accumulation_steps"] * config["block_size"]
    print("词表/上下文/层数:", config["model"]["vocab_size"], config["block_size"], config["model"]["n_layer"])
    print("按配置估算训练位置数:", processed_positions)
    assert config["model"]["vocab_size"] == 32768


def lesson_38():
    import re
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    report = project / "data_scaleup/quality_audit/final_2b_clean_acceptance_report.md"
    if not report.exists():
        print("案例验收报告未找到")
        return
    text = report.read_text(encoding="utf-8")
    count = int(re.search(r"全量扫描 tokens：([\d,]+)", text).group(1).replace(",", ""))
    print("全量机械扫描 token:", count)
    print("近重复限制记录:", "不等价于全量 MinHash 证明" in text)
    assert count > 1_900_000_000


def lesson_39():
    import re
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    report = project / "evaluations/gpt_0p2b_32k_pretrain_2b_v1_final/ASSESSMENT.md"
    if not report.exists():
        print("基础评估报告未找到")
        return
    text = report.read_text(encoding="utf-8")
    losses = [float(x) for x in re.findall(r"step \d+：loss ([\d.]+)", text)]
    print("固定验证 loss 序列:", losses)
    print("可直接聊天成品:", "不是可直接对话的成品" not in text)
    assert losses and losses[-1] < losses[0]


def lesson_40():
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    reports = [project / f"evaluations/stage{i}_v1/ASSESSMENT.md" for i in (4, 5, 6)]
    available = {path.parent.name: path.exists() for path in reports}
    print("SFT 阶段报告:", available)
    if all(available.values()):
        stage4 = reports[0].read_text(encoding="utf-8")
        stage6 = reports[2].read_text(encoding="utf-8")
        print("Stage4 自动规则 42/80:", "42/80" in stage4)
        print("Stage6 未升级:", "均不升级" in stage6)
        assert "42/80" in stage4 and "均不升级" in stage6


def lesson_41():
    from pathlib import Path
    project = Path(__file__).resolve().parents[3] / "gpt02b_lab"
    evidence = {
        "配置": project / "outputs/runs/gpt_0p2b_32k_pretrain_2b_v1/config.json",
        "基础评估": project / "evaluations/gpt_0p2b_32k_pretrain_2b_v1_final/ASSESSMENT.md",
        "SFT评估": project / "evaluations/stage6_v1/ASSESSMENT.md",
    }
    print("复盘证据矩阵:", {name: path.exists() for name, path in evidence.items()})
    print("在线 RL 和通用网关实作不列为已完成事实")


def lesson_42():
    import hashlib
    documents = ["我喜欢苹果。", "我喜欢梨。", "他喜欢香蕉。", "她喜欢葡萄。"]
    train, validation, sealed = documents[:2], documents[2:3], documents[3:]
    fingerprints = [set(hashlib.sha256(item.encode()).hexdigest() for item in part) for part in (train, validation, sealed)]
    print("自写数据 train/val/sealed 数量:", [len(part) for part in (train, validation, sealed)])
    assert not (fingerprints[0] & fingerprints[1] or fingerprints[0] & fingerprints[2])


def lesson_43():
    from collections import Counter
    train = "我喜欢苹果。我喜欢梨。"
    vocabulary = {char: i for i, char in enumerate(sorted(set(train)))}
    ids = [vocabulary[char] for char in train]
    restored = "".join({v: k for k, v in vocabulary.items()}[i] for i in ids)
    bigrams = Counter(zip(ids, ids[1:]))
    print("词表大小:", len(vocabulary), "基线不同 bigram 数:", len(bigrams))
    assert restored == train


def lesson_44():
    import json
    import uuid
    from pathlib import Path
    checkpoint = Path(__file__).resolve().parent / f"_demo_checkpoint_{uuid.uuid4().hex}.json"
    try:
        state = {"step": 0, "weight": 0.0, "optimizer_momentum": 0.0}
        for _ in range(3):
            gradient = 2 * (state["weight"] - 1.0)
            state["optimizer_momentum"] = 0.5 * state["optimizer_momentum"] + gradient
            state["weight"] -= 0.1 * state["optimizer_momentum"]
            state["step"] += 1
        checkpoint.write_text(json.dumps(state), encoding="utf-8")
        resumed = json.loads(checkpoint.read_text(encoding="utf-8"))
        resumed["step"] += 1
        print("暂停检查点 step:", state["step"], "恢复后 step:", resumed["step"])
        assert resumed["step"] == 4
    finally:
        checkpoint.unlink(missing_ok=True)


def lesson_45():
    examples = [("你好", "你好！"), ("我叫什么？", "我不知道你的名字。")]
    baseline = lambda prompt: prompt + "……"
    sft_toy = dict(examples)
    for prompt, expected in examples:
        before = baseline(prompt)
        after = sft_toy[prompt]
        print("提示:", prompt, "基础:", before, "玩具 SFT 目标:", after)
        assert after == expected
    print("这里是样本查找示意，不是神经网络泛化能力")


def lesson_46():
    import json
    model_id = "tiny-gpt-mock"
    request = {"model": model_id, "messages": [{"role": "user", "content": "你好"}], "stream": False}
    def gateway(req):
        if req.get("model") != model_id:
            return 404, {"error": "model_not_found"}
        return 200, {"model": model_id, "text": "你好！", "backend": "deterministic-mock"}
    status, body = gateway(request)
    stream_chunks = ["data: " + json.dumps({"delta": c}, ensure_ascii=False) + "\n\n" for c in body["text"]]
    print("非流式:", status, body)
    print("流式拼接:", "".join(json.loads(chunk[6:])["delta"] for chunk in stream_chunks))
    assert status == 200 and body["backend"] == "deterministic-mock"


def lesson_47():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    lessons = sorted(path for path in root.iterdir() if path.is_dir() and path.name[:2].isdigit())
    ready = [path for path in lessons if (path / "notes.md").is_file() and (path / "demo.py").is_file()]
    print("课程目录/含讲义与代码的目录:", len(lessons), len(ready))
    assert len(ready) == 48
