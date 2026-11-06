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

**想聊就点开下面「简单聊 15 mins」看电话**　或加微信 `Hello_le_0502`　15 分钟，可以先不透露姓名和现单位

[方向](#scope) · [自我介绍](#intro) · [我在找谁](#who) · [怎么联系](#contact) · [English](#english)

</div>

<details>
<summary><b>简单聊 15 mins · 点开看电话</b></summary>

电话 **18357766985**，直接拨或者存一下都行。

一对一沟通，可以先不透露姓名和现单位，不用附简历。

</details>
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
- **多模态 / 视频与图像生成**（重点）
  - 预训练数据：视频与图像语料的清洗去重、质量过滤与配比，时空一致性与运动标注、图文对齐；数据配比基本决定可控性上限
  - 生成结构：DiT 与 flow matching、时空 VAE 压缩比、长时序建模与分辨率外推，图像侧的控制分支与条件注入
  - 参考与编辑生成：reference-based 生成与主体 / ID 一致性、指令式编辑与局部重绘、Flow-GRPO / VideoReward 一类奖励优化；可控性仍缺可靠的自动评测代理
  - 语音并入同一共享表征下的另一路模态，顺带覆盖，不单独展开
- **Infra / 推理系统**
  - 训练侧：TP / PP / EP 并行策略、MFU、训练稳定性
  - 推理侧：prefill-decode 分离、KV cache 与量化、SLO 下的单位 token 成本
  - 效率取舍：集群利用率与弹性调度、量化带来的精度损失
- **大模型评测**（横切维度，单独列出）
  - 评测口径：pass@k 与 RLVR 可验证奖励、人类偏好与 LLM-as-a-judge / pairwise arena、VBench 与时序一致性；按业务场景拆，不套通用榜单
  - 业务落地：离线指标落到灰度 A/B、时延与单位成本、安全合规和人工抽检的回归集
  - 指标失真：judge 自偏好、benchmark 污染、评测集与真实分布偏移；榜单涨分不等于线上收益，离线代理指标怎么对齐真实业务收益仍是开放问题

<!-- ===== 区块 3：自我介绍（口语化、亲近，不写客户名与未证实消息） ===== -->

<a name="intro"></a>

## 自我介绍

我平时最在意的，是那些还没写进公告的变化：一条方法族突然被加注、某家团队悄悄调了组织与投入、技术报告里署名顺序的微调，往往比榜单涨分更早说明方向往哪走。各家最近在聊什么、哪些动向有公开资料能互相印证、哪些只是噪声，我会先自己交叉核验一遍；能讲的讲清楚，没把握的就说没把握，传言到我这儿为止。这一年也陆续陪不少同学做过咨询：有人想确认手上的问题还值不值得继续投入，有人在两三条路线之间权衡，也有人最后什么都没换，只是把整张行业地图看清楚了。我挺喜欢这种没有结论、聊完却踏实一点的对话。所以你哪怕暂时完全不看机会，也欢迎加个微信，就当多一个能聊行业、也守得住分寸的朋友；等哪天真的想动了，我们再聊也不迟。

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
<summary><b>多模态与生成</b>　视频、图像生成方向</summary>

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
| 电话 | 点开上方「简单聊 15 mins」查看，直接聊 15 分钟 |
| 微信 | `Hello_le_0502`（添加时备注想聊的方向，不用附简历） |
| 邮箱 | [18357766985@163.com](mailto:18357766985@163.com)（备选） |

> 一对一沟通，不共享给任何第三方。可以先不透露姓名和现单位，只聊方向。你的信息不会出现在任何公开仓库或公开列表里。

<div align="center">

**点开「简单聊 15 mins」，看号码后先匿名聊 15 分钟**

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

**What I cover** — foundation models and post-training as one track: MoE routing and sparse activation, data mixture and mid-training annealing, RoPE extrapolation and KV cache economics, then DPO / PPO / GRPO, RLVR and verifiable rewards, process reward models, and RL alignment for diffusion language models. Multimodal generation is the second main track, with video and image at the center: pretraining data curation and mixture, DiT / flow matching and spatial-temporal VAE compression, reference-based generation and instruction-driven editing; speech is only mentioned as another modality under the same shared representation. Also systems (TP / PP / EP parallelism, MFU, prefill-decode disaggregation, unit token cost under SLO) and, as a separate cross-cutting track, LLM evaluation (verifiable rewards, human preference and LLM-as-a-judge, VBench-style metrics, and how offline scores translate into production guardrails).

**A bit about me** — I tend to notice the changes that never make it into an announcement: a method family suddenly getting more investment, a quiet shift in how a team is organized, a small change in the author order of a technical report. Those signals often move earlier than leaderboard scores. I cross-check what can be verified against public sources, say plainly when something is still unconfirmed, and let rumors stop with me. Over the past year I have also helped many researchers think things through: some weighing whether a problem is still worth their time, some comparing two or three routes, some simply leaving with a clearer map of the field and no decision at all. Those are the conversations I enjoy most. Even if you are not looking at any opportunity right now, adding me on WeChat just to talk shop is more than welcome.

**The only ask** — a 15-minute anonymous conversation. One-to-one, never shared with third parties, no need to reveal your name or current employer.

**Contact** — open the "15-min chat" panel above to reveal my phone number, or add WeChat `Hello_le_0502`. A short call is enough; no CV, no name, no current employer needed. **Full profile** — https://nikoyyl21.github.io/

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agi-strip-dark.svg">
  <img src="assets/agi-strip-light.svg" alt="Motif: sparse activation flowing into shared representations" width="100%">
</picture>

<div align="center">

<sub>公开资料整理　|　不含候选人信息与在招团队细节</sub>

</div>
