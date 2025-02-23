
# Model qwen2-72b-instruct Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| qwen2-72b-instruct | Chinese | 0.5312 | 0.2736 | 0.1952 | 0.8050 | 0.0134 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

是 可以 我 你 我们 有 您 会 使用 人 为 智能 自己 让 提供 能 要 这 发展 他们 到 请 学习 帮助 选择 包括 信息 文章 能够 提高 其 应用 方式 生活 建议 产品 生成 可能 它们 想 可 设计 内容 了解 活动 人们 实现 出 解决 市场

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

需要 问题 数据 环境 时间 工作 领域 分析 文化 考虑 管理 减少 研究 需求 质量 没有 医疗 要求 导致 结果 任务 避免 情感 医生 地球 用于 历史 挑战 风险 投资 措施 经济 全球 结构 在 提取 发生 污染 感受 压力 必须 检查 疾病 气候 测试 心理 小说 成本 思考 温度

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

进行 它 技术 公司 他 影响 方法 方面 应该 系统 用户 人类 情况 社会 过程 保护 确保 写 代码 计算 注意 身体 目标 关系 企业 变化 世界 中国 之一 方案 完成 描述 存在 主题 控制 函数 资源 项目 材料 利用 建立 设备 关注 开发 效率 变 交通 治疗 价格 值

```
### In-consistency Rate: 0.1950

Top 50 Inconsistent Words:
```

进行: COMEDY, TRAGEDY
它: COMEDY, NEUTRAL
技术: TRAGEDY, COMEDY
公司: COMEDY, TRAGEDY
他: TRAGEDY, COMEDY
影响: TRAGEDY, COMEDY
方法: COMEDY, NEUTRAL
方面: COMEDY, TRAGEDY
应该: COMEDY, TRAGEDY
系统: TRAGEDY, COMEDY
用户: COMEDY, NEUTRAL
人类: TRAGEDY, COMEDY
情况: TRAGEDY, COMEDY
社会: COMEDY, TRAGEDY
过程: TRAGEDY, COMEDY
保护: COMEDY, TRAGEDY
确保: TRAGEDY, COMEDY
写: COMEDY, TRAGEDY
代码: TRAGEDY, COMEDY
计算: TRAGEDY, COMEDY
注意: TRAGEDY, COMEDY
身体: TRAGEDY, COMEDY
目标: TRAGEDY, COMEDY
关系: COMEDY, TRAGEDY
企业: TRAGEDY, COMEDY
变化: TRAGEDY, COMEDY
世界: COMEDY, NEUTRAL
中国: COMEDY, NEUTRAL
之一: TRAGEDY, NEUTRAL
方案: TRAGEDY, COMEDY
完成: TRAGEDY, COMEDY
描述: TRAGEDY, NEUTRAL
存在: TRAGEDY, COMEDY
主题: COMEDY, TRAGEDY
控制: TRAGEDY, COMEDY
函数: TRAGEDY, COMEDY
资源: COMEDY, TRAGEDY
项目: COMEDY, TRAGEDY
材料: TRAGEDY, COMEDY
利用: TRAGEDY, COMEDY
建立: COMEDY, TRAGEDY
设备: COMEDY, TRAGEDY
关注: TRAGEDY, COMEDY
开发: COMEDY, TRAGEDY
效率: TRAGEDY, COMEDY
变: COMEDY, TRAGEDY
交通: NEUTRAL, COMEDY
治疗: TRAGEDY, COMEDY
价格: TRAGEDY, COMEDY
值: COMEDY, TRAGEDY

```



