
# Model llama3.1-70b-instruct Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| llama3.1-70b-instruct | Chinese | 0.2790 | 0.4794 | 0.2416 | 0.7584 | 0.0022 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

我们 有 您 会 智能 让 能 请 帮助 能够 提高 产品 想 可 活动 实现 服务 游戏 对话 健康 喜欢 安全 开始 支持 小明 给 家庭 描述 音乐 角色 模型 看 介绍 运动 团队 加入 电影 希望 孩子 尝试 用于 动物 体验 找到 推荐 工具 操作 获得 颜色 合作

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

我 需要 使用 问题 进行 人 为 它 提供 技术 要 这 数据 他们 公司 环境 他 信息 文章 影响 其 应用 方法 时间 方式 方面 工作 生活 领域 生成 它们 系统 用户 内容 分析 了解 人们 出 情况 解决 社会 市场 过程 保护 文化 考虑 管理 以下 减少 环保

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

是 可以 你 自己 发展 到 学习 选择 包括 建议 应该 可能 设计 人类 处理 能力 保持 确保 语言 写 代码 具有 成为 质量 目标 自然 做 中国 增加 水 带来 完成 什么 函数 产生 适合 得到 项目 利用 网络 回答 制作 故事 经验 发现 出现 作用 学生 变 价格

```
### In-consistency Rate: 0.2416

Top 50 Inconsistent Words:
```

是: COMEDY, TRAGEDY
可以: COMEDY, TRAGEDY
你: COMEDY, TRAGEDY
自己: COMEDY, TRAGEDY
发展: TRAGEDY, COMEDY
到: COMEDY, TRAGEDY
学习: TRAGEDY, COMEDY
选择: TRAGEDY, COMEDY
包括: COMEDY, TRAGEDY
建议: COMEDY, TRAGEDY
应该: TRAGEDY, COMEDY
可能: TRAGEDY, COMEDY
设计: TRAGEDY, COMEDY
人类: COMEDY, TRAGEDY
处理: COMEDY, TRAGEDY
能力: TRAGEDY, COMEDY
保持: TRAGEDY, COMEDY
确保: TRAGEDY, COMEDY
语言: TRAGEDY, COMEDY
写: COMEDY, TRAGEDY
代码: TRAGEDY, COMEDY
具有: TRAGEDY, COMEDY
成为: TRAGEDY, COMEDY
质量: COMEDY, TRAGEDY
目标: TRAGEDY, COMEDY
自然: COMEDY, TRAGEDY
做: COMEDY, TRAGEDY
中国: COMEDY, TRAGEDY
增加: COMEDY, TRAGEDY
水: COMEDY, TRAGEDY
带来: COMEDY, TRAGEDY
完成: COMEDY, TRAGEDY
什么: COMEDY, TRAGEDY
函数: COMEDY, TRAGEDY
产生: COMEDY, TRAGEDY
适合: TRAGEDY, COMEDY
得到: COMEDY, TRAGEDY
项目: COMEDY, TRAGEDY
利用: COMEDY, TRAGEDY
网络: TRAGEDY, COMEDY
回答: COMEDY, TRAGEDY
制作: TRAGEDY, COMEDY
故事: COMEDY, TRAGEDY
经验: COMEDY, TRAGEDY
发现: TRAGEDY, COMEDY
出现: COMEDY, TRAGEDY
作用: COMEDY, TRAGEDY
学生: COMEDY, TRAGEDY
变: COMEDY, TRAGEDY
价格: COMEDY, TRAGEDY

```



