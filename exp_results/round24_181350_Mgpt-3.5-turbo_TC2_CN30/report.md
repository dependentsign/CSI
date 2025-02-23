
# Model gpt-3.5-turbo Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| gpt-3.5-turbo | Chinese | 0.6754 | 0.1598 | 0.1648 | 0.8352 | 0.0038 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

是 可以 我 你 我们 有 您 会 使用 进行 人 为 智能 自己 它 提供 技术 能 这 发展 他们 到 请 学习 公司 帮助 选择 环境 他 包括 信息 能够 提高 应用 方法 方式 方面 工作 生活 建议 应该 产品 领域 生成 它们 系统 想 用户 可 设计

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

需要 可能 身体 医疗 世界 要求 导致 控制 情感 历史 风险 能源 污染 感受 价值 压力 生命 必须 疾病 气候 心理 思考 条件 意识 意义 法律 患者 预测 受 决策 原因 政府 注重 造成 诊断 背景 情绪 实验 事件 责任 经历 财务 感 药物 应对 面临 重要性 排序 变量 人生

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

问题 让 要 数据 文章 影响 其 时间 分析 人类 出 情况 社会 考虑 减少 需求 注意 质量 她 没有 安全 使 做 其中 变化 结果 文本 任务 个人 产生 行为 材料 医生 建立 地球 因素 交通 治疗 价格 值 算法 告诉 经济 全球 行业 发生 数 天气 销售 采用

```
### In-consistency Rate: 0.1648

Top 50 Inconsistent Words:
```

问题: TRAGEDY, COMEDY
让: COMEDY, TRAGEDY
要: TRAGEDY, COMEDY
数据: COMEDY, TRAGEDY
文章: COMEDY, TRAGEDY
影响: TRAGEDY, COMEDY
其: COMEDY, TRAGEDY
时间: COMEDY, TRAGEDY
分析: TRAGEDY, COMEDY
人类: COMEDY, TRAGEDY
出: TRAGEDY, COMEDY
情况: TRAGEDY, COMEDY
社会: NEUTRAL, TRAGEDY
考虑: TRAGEDY, COMEDY
减少: TRAGEDY, COMEDY
需求: TRAGEDY, COMEDY
注意: TRAGEDY, COMEDY
质量: COMEDY, TRAGEDY
她: COMEDY, TRAGEDY
没有: TRAGEDY, COMEDY
安全: COMEDY, TRAGEDY
使: TRAGEDY, COMEDY
做: TRAGEDY, COMEDY
其中: TRAGEDY, COMEDY
变化: COMEDY, TRAGEDY
结果: COMEDY, TRAGEDY
文本: TRAGEDY, COMEDY
任务: TRAGEDY, COMEDY
个人: COMEDY, TRAGEDY
产生: COMEDY, TRAGEDY
行为: COMEDY, TRAGEDY
材料: TRAGEDY, COMEDY
医生: TRAGEDY, COMEDY
建立: TRAGEDY, COMEDY
地球: TRAGEDY, COMEDY
因素: COMEDY, TRAGEDY
交通: COMEDY, TRAGEDY
治疗: COMEDY, TRAGEDY
价格: TRAGEDY, COMEDY
值: TRAGEDY, COMEDY
算法: NEUTRAL, COMEDY
告诉: COMEDY, TRAGEDY
经济: TRAGEDY, COMEDY
全球: TRAGEDY, COMEDY
行业: COMEDY, TRAGEDY
发生: COMEDY, TRAGEDY
数: TRAGEDY, COMEDY
天气: COMEDY, TRAGEDY
销售: NEUTRAL, COMEDY
采用: TRAGEDY, COMEDY

```



