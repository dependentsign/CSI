
# Model gpt4-1106-preview Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| gpt4-1106-preview | Chinese | 0.6524 | 0.1934 | 0.1542 | 0.8462 | 0.0125 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

是 可以 我 你 我们 有 您 会 使用 进行 人 智能 自己 让 它 提供 技术 能 要 这 数据 发展 他们 学习 帮助 选择 环境 包括 信息 能够 提高 影响 应用 方法 方式 方面 工作 生活 建议 产品 生成 可能 它们 用户 可 设计 内容 分析 了解 活动

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

需要 问题 时间 情况 管理 减少 关系 没有 医疗 要求 导致 结果 函数 避免 情感 利用 历史 风险 投资 经济 污染 压力 生命 必须 疾病 心理 成本 意义 法律 患者 受到 降低 受 执行 原因 政府 造成 金融 诊断 事件 责任 经历 财务 数学 报告 决定 竞争 药物 诗歌 状况

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

为 到 请 公司 他 文章 其 应该 领域 系统 想 人类 处理 过程 保护 考虑 确保 需求 计算 成为 质量 她 目标 程序 去 企业 方案 文本 任务 功能 存在 控制 医生 作用 步骤 知道 因素 变 交通 治疗 值 机器 制定 措施 风格 训练 结构 成 在 感到

```
### In-consistency Rate: 0.1538

Top 50 Inconsistent Words:
```

为: COMEDY, TRAGEDY
到: NEUTRAL, COMEDY
请: COMEDY, NEUTRAL
公司: COMEDY, TRAGEDY
他: TRAGEDY, COMEDY
文章: COMEDY, TRAGEDY
其: COMEDY, TRAGEDY
应该: COMEDY, NEUTRAL
领域: NEUTRAL, COMEDY
系统: NEUTRAL, TRAGEDY
想: COMEDY, TRAGEDY
人类: COMEDY, TRAGEDY
处理: TRAGEDY, COMEDY
过程: COMEDY, TRAGEDY
保护: TRAGEDY, COMEDY
考虑: COMEDY, TRAGEDY
确保: TRAGEDY, COMEDY
需求: TRAGEDY, COMEDY
计算: COMEDY, TRAGEDY
成为: NEUTRAL, COMEDY
质量: COMEDY, TRAGEDY
她: COMEDY, NEUTRAL
目标: TRAGEDY, COMEDY
程序: TRAGEDY, COMEDY
去: COMEDY, TRAGEDY
企业: COMEDY, TRAGEDY
方案: TRAGEDY, COMEDY
文本: TRAGEDY, COMEDY
任务: COMEDY, NEUTRAL
功能: TRAGEDY, COMEDY
存在: COMEDY, TRAGEDY
控制: TRAGEDY, COMEDY
医生: COMEDY, TRAGEDY
作用: COMEDY, TRAGEDY
步骤: TRAGEDY, COMEDY
知道: TRAGEDY, COMEDY
因素: COMEDY, TRAGEDY
变: TRAGEDY, COMEDY
交通: TRAGEDY, COMEDY
治疗: TRAGEDY, COMEDY
值: TRAGEDY, COMEDY
机器: TRAGEDY, COMEDY
制定: COMEDY, TRAGEDY
措施: COMEDY, TRAGEDY
风格: COMEDY, NEUTRAL
训练: COMEDY, TRAGEDY
结构: COMEDY, TRAGEDY
成: TRAGEDY, COMEDY
在: NEUTRAL, COMEDY
感到: COMEDY, TRAGEDY

```



