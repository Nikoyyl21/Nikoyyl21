<!-- ==========================================================
     已上线版本。每个可编辑区块都用注释标了出来。
     全局规则：不出现中文姓名、不出现未授权客户名、不出现候选人信息。
     术语原则：写方法族、真实取舍和开放问题，不堆关键词。
     改稿清单见 EDIT-ME.md
     ========================================================== -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Petry, multimodal inputs converging into a shared latent space" width="100%">
</picture>

<div align="center">

**完整介绍页 → [nikoyyl21.github.io](https://nikoyyl21.github.io/)**　点开即读，无需登录

**我在帮做基模和多模态的研究员，判断下一个值得投入的问题**

`foundation models`　`post-training`　`multimodal generation`　`systems`

**想聊就直接发一封邮件：[18357766985@163.com](mailto:18357766985@163.com)**　或加微信 `Hello_le_0502`　15 分钟，可以先不透露姓名和现单位

[方向](#scope) · [怎么读报告](#method) · [我在找谁](#who) · [怎么联系](#contact) · [English](#english)

</div>

---

<!-- ===== 区块 1：定位（改这里） ===== -->

## 我在做什么

以公开技术报告、论文和开源实现为一手材料，跟踪基模与多模态方向的方法演进和组织分工，还原一条路线真正在解什么问题。

聊的是方法取舍、数据配比和算力约束，不是岗位清单。

<!-- ===== 区块 2：方向（改这里，术语可替换） ===== -->

<a name="scope"></a>

## 方向

- **文本基座 / 后训练**（重点）
  - 预训练与架构：MoE 专家路由与稀疏激活、数据配比与 mid-training 退火、RoPE 外推与 KV cache 成本
  - 后训练与对齐：DPO / PPO / GRPO 一族、RLVR 与可验证奖励、process reward model、扩散语言模型上的 RL 对齐（dLLM / EBPO）
  - 真实代价：reward hacking、KL 约束的取舍、scaling law 之外的数据墙；后训练收益有多少来自基座能力本身，仍是开放问题
- **多模态 / 视频**
  - 生成架构：DiT 与 flow matching、时空 VAE 压缩比、长时序一致性
  - 奖励与可控：基于 GRPO 的奖励优化（Flow-GRPO / VideoReward）、运动物理合理性；可控性仍缺可靠的自动评测代理
  - 数据与算力：训练数据配比与时空压缩的取舍，VBench 等自动指标和人类偏好之间仍有差距
- **语音**
  - 端到端语音：离散 codec token、流式推理与实时交互时延
  - 多模态衔接：语音与文本、视觉的共享表征，副语言信息建模；自然度上去之后可控性怎么保证
  - 工程约束：首包时延、长语音稳定性与端侧推理成本
- **Infra / 推理系统**
  - 训练侧：TP / PP / EP 并行策略、MFU、训练稳定性
  - 推理侧：prefill-decode 分离、KV cache 与量化、SLO 下的单位 token 成本
  - 效率取舍：集群利用率与弹性调度、量化带来的精度损失
- **评测 / 落地**
  - 评测口径：pass@k 与 RLVR 可验证奖励、人类偏好与 LLM-as-a-judge、VBench 与时序一致性
  - 业务落地：按业务场景拆口径，再落到灰度 A/B、时延与单位成本、安全合规和人工抽检的回归集；榜单涨分不等于线上收益

<!-- ===== 区块 3：方法论（这段是专业度的主要支撑） ===== -->

<a name="method"></a>

## 怎么读一份技术报告

1. 按方法族归档，不按产品名归档。同一条路线在不同实现里的差异，比发布顺序更有信息量。
2. 关键结论做多源交叉核验，OpenReview、arXiv、DBLP、机构主页和开源实现互相印证；同名歧义保留候选，不强行合并。
3. 每条判断标注来源与置信度。查不到就写查不到，不补推测，不把推断伪装成事实。

置顶仓库是这套方法的产出：技术图谱、作者索引、方向时间线，全部基于公开资料。

<!-- ===== 区块 4：我在找谁（改这里，可复用分人群话术） ===== -->

<a name="who"></a>

## 我在找谁

<details>
<summary><b>研究员</b>　想判断方向，或比较不同实现的路线差异</summary>

<br>

从你在做的具体问题聊起，基模能力边界、奖励信号设计，或者一个方法在更大规模上还成不成立。可以直接问我某条路线走到哪一步、瓶颈在哪。

</details>

<details>
<summary><b>Infra 与系统</b>　关心 MFU、并行策略和推理成本</summary>

<br>

TP / PP / EP 怎么切、prefill-decode 分离是不是真落地、集群拓扑和 SLO 的实际约束，都能摊开讲，包括不那么好看的部分。

</details>

<details>
<summary><b>多模态与生成</b>　视频、图像、语音生成方向</summary>

<br>

数据配比、时空压缩比、奖励模型怎么建、评测靠 VBench 还是人类偏好对齐，这些比岗位清单更值得先聊清楚。

</details>

<details>
<summary><b>暂时不想动的人</b>　只想先了解发生了什么</summary>

<br>

不做任何决定也没关系，这类聊天我同样欢迎。

</details>

<!-- ===== 区块 5：可信度（有公开文章就把链接加在这段） ===== -->

## 为什么可以跟我聊

按方法族和算力约束做梳理，不按 JD 关键词做匹配。

能说清一条路线为什么被选中、代价是什么，以及同一技术维度上不同实现的取舍。

不合适会直说，不硬推。

<!-- ===== 区块 6：联系（已上线，以后有预约链接或二维码再加行） ===== -->
<!-- 顶部还有一条落地页入口，指向 https://nikoyyl21.github.io/ -->

<a name="contact"></a>

## 怎么联系

| | |
| :--- | :--- |
| 邮箱 | [18357766985@163.com](mailto:18357766985@163.com) |
| 微信 | `Hello_le_0502`（添加时备注想聊的方向，不用附简历） |
| 15 分钟 | 邮件或微信约时间都可以，标题写想聊的方向就行 |

> 一对一沟通，不共享给任何第三方。可以先不透露姓名和现单位，只聊方向。你的信息不会出现在任何公开仓库或公开列表里。

<div align="center">

**发一封邮件，先匿名聊 15 分钟**

</div>

<!-- ===== 区块 7：每周动态（自动，不用手改） ===== -->

## 最近在看的

<!-- WEEKLY-NOTE:START -->
最近更新 2026-11-05　|　最近在看扩散语言模型上的 RL 对齐（dLLM / EBPO），以及视频生成奖励模型在 flow matching 下的可迁移性与 reward hacking。
<!-- WEEKLY-NOTE:END -->

---

<a name="english"></a>

<!-- ===== 英文版（改这里） ===== -->

## English

I track how foundation model and multimodal methods actually evolve, using public technical reports, papers and open-source implementations as primary sources.

**What I cover** — foundation models and post-training as one track: MoE routing and sparse activation, data mixture and mid-training annealing, RoPE extrapolation and KV cache economics, then DPO / PPO / GRPO, RLVR and verifiable rewards, process reward models, and RL alignment for diffusion language models. Also multimodal and video generation (DiT / flow matching, spatial-temporal VAE compression, Flow-GRPO / VideoReward), speech (discrete codec tokens, streaming inference), systems (TP / PP / EP parallelism, MFU, prefill-decode disaggregation, unit token cost under SLO), and evaluation practice (verifiable rewards, human preference and LLM-as-a-judge, VBench-style metrics, and how offline scores translate into production guardrails).

**How I read a report** — archive by method family rather than product name, cross-check claims against OpenReview, arXiv, DBLP and institutional pages, keep ambiguous author candidates separate, and label every conclusion with a source and a confidence level.

**The only ask** — a 15-minute anonymous conversation. One-to-one, never shared with third parties, no need to reveal your name or current employer.

**Contact** — [18357766985@163.com](mailto:18357766985@163.com) or WeChat `Hello_le_0502`. A short message is enough; no CV, no name, no current employer needed. **Full profile** — https://nikoyyl21.github.io/

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agi-strip-dark.svg">
  <img src="assets/agi-strip-light.svg" alt="Motif: sparse activation flowing into shared representations" width="100%">
</picture>

<div align="center">

<sub>公开资料整理　|　不含候选人信息与在招团队细节</sub>

</div>
