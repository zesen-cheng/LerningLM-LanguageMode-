# 从零训练语言模型：逐课索引

每课都有独立撰写的 `notes.md` 与可运行的 `demo.py`；每个主题末尾都设有解答与复习时间。

## 基础知识与 GPT

- [00｜AI 的任务地图](00_ai_map/notes.md) · [运行代码](00_ai_map/demo.py)
- [01｜从样本到预测](01_prediction_loop/notes.md) · [运行代码](01_prediction_loop/demo.py)
- [02｜实验环境与可复现](02_environment/notes.md) · [运行代码](02_environment/demo.py)
- [03｜训练所需数学直觉](03_math_intuition/notes.md) · [运行代码](03_math_intuition/demo.py)
- [04｜训练、验证与测试](04_data_splits/notes.md) · [运行代码](04_data_splits/demo.py)
- [05｜损失函数与任务](05_loss_functions/notes.md) · [运行代码](05_loss_functions/demo.py)
- [06｜神经网络与反向传播](06_backpropagation/notes.md) · [运行代码](06_backpropagation/demo.py)
- [07｜优化器与泛化](07_optimizer_generalization/notes.md) · [运行代码](07_optimizer_generalization/demo.py)
- [08｜文本如何变成 token ID](08_token_ids/notes.md) · [运行代码](08_token_ids/demo.py)
- [09｜Embedding 与位置](09_embedding_position/notes.md) · [运行代码](09_embedding_position/demo.py)
- [10｜Bigram 语言模型](10_bigram_lm/notes.md) · [运行代码](10_bigram_lm/demo.py)
- [11｜因果 Attention](11_causal_attention/notes.md) · [运行代码](11_causal_attention/demo.py)
- [12｜Transformer Block](12_transformer_block/notes.md) · [运行代码](12_transformer_block/demo.py)
- [13｜GPT 的下一个 token 目标](13_gpt_next_token/notes.md) · [运行代码](13_gpt_next_token/demo.py)
- [14｜采样与回复](14_sampling/notes.md) · [运行代码](14_sampling/demo.py)

### 解答与复习时间

先回答本主题关键问题：token 是切分后的单位；tokenizer 是编码规则。32K 词表不等于 32K 上下文。

[进入完整问答、自测与答案](reviews/01_foundations.md)


## 预训练

- [15｜语料来源与许可](15_corpus_provenance/notes.md) · [运行代码](15_corpus_provenance/demo.py)
- [16｜清洗、去重与审计](16_cleaning_audit/notes.md) · [运行代码](16_cleaning_audit/demo.py)
- [17｜训练与检验 tokenizer](17_tokenizer_check/notes.md) · [运行代码](17_tokenizer_check/demo.py)
- [18｜预训练实验设计](18_training_plan/notes.md) · [运行代码](18_training_plan/demo.py)
- [19｜从随机权重训练 Tiny GPT](19_tiny_gpt_training/notes.md) · [运行代码](19_tiny_gpt_training/demo.py)
- [20｜检查点与恢复](20_checkpoint_resume/notes.md) · [运行代码](20_checkpoint_resume/demo.py)
- [21｜训练监控与异常](21_progress_monitoring/notes.md) · [运行代码](21_progress_monitoring/demo.py)
- [22｜基础模型评估](22_base_model_eval/notes.md) · [运行代码](22_base_model_eval/demo.py)

### 解答与复习时间

先回答本主题关键问题：step 是一次参数更新；checkpoint 保存可恢复状态；KV cache 用于推理复用。

[进入完整问答、自测与答案](reviews/02_pretraining.md)


## 后训练

- [23｜基础模型与聊天模型](23_base_vs_chat/notes.md) · [运行代码](23_base_vs_chat/demo.py)
- [24｜对话样本与损失掩码](24_sft_masking/notes.md) · [运行代码](24_sft_masking/demo.py)
- [25｜小规模 SFT](25_sft_update/notes.md) · [运行代码](25_sft_update/demo.py)
- [26｜封存评估与回归](26_sealed_eval/notes.md) · [运行代码](26_sealed_eval/demo.py)
- [27｜偏好数据与 DPO](27_preference_dpo/notes.md) · [运行代码](27_preference_dpo/demo.py)
- [28｜RLHF 与在线强化学习](28_rlhf_bandit/notes.md) · [运行代码](28_rlhf_bandit/demo.py)
- [29｜后训练验收](29_posttrain_acceptance/notes.md) · [运行代码](29_posttrain_acceptance/demo.py)

### 解答与复习时间

先回答本主题关键问题：SFT 学示范回答；DPO 学离线偏好；在线 RL 根据奖励更新策略。

[进入完整问答、自测与答案](reviews/03_posttraining.md)


## 推理与网关

- [30｜推理模型文件](30_inference_artifacts/notes.md) · [运行代码](30_inference_artifacts/demo.py)
- [31｜HTTP/JSON 最小接口](31_http_json/notes.md) · [运行代码](31_http_json/demo.py)
- [32｜流式输出与 SSE](32_sse_stream/notes.md) · [运行代码](32_sse_stream/demo.py)
- [33｜结构化输出与工具调用](33_tool_calling/notes.md) · [运行代码](33_tool_calling/demo.py)
- [34｜协议适配](34_protocol_adapter/notes.md) · [运行代码](34_protocol_adapter/demo.py)
- [35｜网关与可观察性](35_gateway_controls/notes.md) · [运行代码](35_gateway_controls/demo.py)
- [36｜端到端联调](36_end_to_end/notes.md) · [运行代码](36_end_to_end/demo.py)

### 解答与复习时间

先回答本主题关键问题：模型提出工具调用，宿主程序验证并执行；推理服务与网关各有职责。

[进入完整问答、自测与答案](reviews/04_serving.md)


## 真实案例

- [37｜案例：设备、配置与目标](37_case_config/notes.md) · [运行代码](37_case_config/demo.py)
- [38｜案例：数据与 tokenizer](38_case_data_tokenizer/notes.md) · [运行代码](38_case_data_tokenizer/demo.py)
- [39｜案例：预训练与基础评估](39_case_pretrain_eval/notes.md) · [运行代码](39_case_pretrain_eval/demo.py)
- [40｜案例：SFT 收益与回退](40_case_sft_results/notes.md) · [运行代码](40_case_sft_results/demo.py)
- [41｜案例：证据链](41_case_evidence/notes.md) · [运行代码](41_case_evidence/demo.py)

### 解答与复习时间

先回答本主题关键问题：将配置、日志、评估与失败样本合在一起，才能解释 0.2B 实验。

[进入完整问答、自测与答案](reviews/05_case.md)


## 学员结课

- [42｜结课：选择可完成的任务](42_capstone_data/notes.md) · [运行代码](42_capstone_data/demo.py)
- [43｜结课：tokenizer 基线](43_capstone_tokenizer/notes.md) · [运行代码](43_capstone_tokenizer/demo.py)
- [44｜结课：训练与恢复](44_capstone_train_resume/notes.md) · [运行代码](44_capstone_train_resume/demo.py)
- [45｜结课：SFT 与评估](45_capstone_sft_eval/notes.md) · [运行代码](45_capstone_sft_eval/demo.py)
- [46｜结课：接口与网关](46_capstone_gateway/notes.md) · [运行代码](46_capstone_gateway/demo.py)
- [47｜结课：展示与边界](47_capstone_report/notes.md) · [运行代码](47_capstone_report/demo.py)

### 解答与复习时间

先回答本主题关键问题：先封存评估，再训练、恢复、对比和报告。

[进入完整问答、自测与答案](reviews/06_capstone.md)
