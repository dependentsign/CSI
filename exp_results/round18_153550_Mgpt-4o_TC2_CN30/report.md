
# Model gpt-4o Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| gpt-4o | Chinese | 0.4786 | 0.2470 | 0.2744 | 0.7282 | 0.0483 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

是 可以 你 我们 有 使用 进行 让 它 能 这 他们 学习 帮助 他 包括 能够 提高 方法 方式 方面 生活 建议 产品 可能 它们 想 可 设计 内容 了解 活动 实现 出 解决 市场 能力 保护 服务 确保 环保 需求 游戏 语言 写 对话 计算 注意 健康 喜欢

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

需要 会 问题 自己 公司 影响 时间 工作 情况 考虑 减少 身体 没有 医疗 去 世界 要求 导致 结果 任务 存在 控制 避免 材料 医生 回答 地球 历史 因素 治疗 风险 值 操作 措施 行业 提取 部分 发生 污染 策略 数 压力 生命 采取 者 检查 疾病 气候 科学 测试

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

我 您 人 为 智能 提供 技术 要 数据 发展 到 请 选择 环境 信息 文章 其 应用 应该 领域 生成 系统 用户 分析 人类 人们 社会 处理 过程 文化 管理 保持 以下 研究 代码 具有 质量 她 认为 目标 关系 使 程序 其中 企业 变化 中国 增加 带来 方案

```
### In-consistency Rate: 0.2718

Top 50 Inconsistent Words:
```

我: COMEDY, TRAGEDY
您: COMEDY, TRAGEDY
人: TRAGEDY, NEUTRAL
为: TRAGEDY, COMEDY
智能: NEUTRAL, COMEDY
提供: NEUTRAL, COMEDY
技术: COMEDY, NEUTRAL
要: COMEDY, TRAGEDY
数据: TRAGEDY, COMEDY
发展: NEUTRAL, COMEDY
到: COMEDY, NEUTRAL
请: NEUTRAL, COMEDY
选择: TRAGEDY, COMEDY
环境: TRAGEDY, NEUTRAL
信息: COMEDY, TRAGEDY
文章: COMEDY, TRAGEDY
其: COMEDY, TRAGEDY
应该: TRAGEDY, COMEDY
领域: TRAGEDY, COMEDY
生成: COMEDY, NEUTRAL
系统: TRAGEDY, COMEDY
用户: TRAGEDY, COMEDY
分析: COMEDY, TRAGEDY
人类: NEUTRAL, TRAGEDY
人们: COMEDY, TRAGEDY
社会: COMEDY, TRAGEDY
处理: COMEDY, TRAGEDY
过程: COMEDY, TRAGEDY
文化: COMEDY, NEUTRAL
管理: COMEDY, TRAGEDY
保持: COMEDY, NEUTRAL
以下: COMEDY, TRAGEDY
研究: NEUTRAL, TRAGEDY
代码: TRAGEDY, COMEDY
具有: NEUTRAL, COMEDY
质量: COMEDY, TRAGEDY
她: COMEDY, NEUTRAL
认为: COMEDY, TRAGEDY
目标: COMEDY, NEUTRAL
关系: TRAGEDY, COMEDY
使: NEUTRAL, COMEDY
程序: NEUTRAL, TRAGEDY
其中: COMEDY, NEUTRAL
企业: TRAGEDY, NEUTRAL
变化: NEUTRAL, COMEDY
中国: COMEDY, TRAGEDY
增加: COMEDY, NEUTRAL
带来: NEUTRAL, COMEDY
方案: TRAGEDY, COMEDY
文本: TRAGEDY, COMEDY

```



