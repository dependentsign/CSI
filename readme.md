# **Model Evaluation and CSI Analysis**


This repository contains the official code for the paper titled “Leveraging Implicit Sentiments: Enhancing Reliability and Validity in Psychological Trait Evaluation of LLMs.” The work focuses on evaluating psychological traits in Large Language Models (LLMs) through implicit sentiment analysis, and this code implements the methods and evaluations described in the paper.



## **Setup**



Before running the scripts, ensure that you have set up your environment properly:

​	1.	**Set Your OpenAI API Key**

First, export your OpenAI API key:

```
export OPENAI_API_KEY='Your API Key'
```



​	2.	**Install Dependencies**

Install the necessary dependencies using pip:

```
pip install -r requirements.txt
```





## **Model Evaluation**



Evaluate the model using the following command:

```
python main.py --model gpt-4o --context_num 30 --test_count 2 --lang English --temperature 0
```

​	•	**Arguments:**

​	•	--model: The model to evaluate (e.g., gpt-4o).

​	•	--context_num: The number of contexts to be used during evaluation.

​	•	--test_count: The number of tests to run.

​	•	--lang: The language of the evaluation (e.g., English).



Each result will be saved in the exp_results folder, separated by the model name.



## **CSI Analysis**



Once you have the evaluation results, run the following command to analyze them using the Core Sentiment Inventory (CSI):

```
python analize_CSI.py
```

The results will be saved in a .md file for each model.



## **Story Generation Task**



To test the validity of the CSI, you can use the story generation task. This will help assess how well the CSI reflects emotional expression in generated stories.



Run the task with the following command:

```
python story_generation.py
```

### **Results**



#### **Numerical Reports**

| **Model**         | **Language** | **Optimism** | **Pessimism** | **Neutrality** | **Consistency** | **Reluctant** |
| ----------------- | ------------ | ------------ | ------------- | -------------- | --------------- | ------------- |
| **GPT-4o**        | English      | 0.4792       | 0.2726        | 0.2482         | 0.7536          | 0.0400        |
| **GPT-4o**        | Chinese      | 0.4786       | 0.2470        | 0.2744         | 0.7282          | 0.0483        |
| **GPT-4 (1106)**  | English      | 0.4658       | 0.2642        | 0.2700         | 0.7408          | 0.0871        |
| **GPT-4 (1106)**  | Chinese      | 0.6524       | 0.1934        | 0.1542         | 0.8462          | 0.0125        |
| **GPT-4 (0125)**  | English      | 0.5732       | 0.2638        | 0.1630         | 0.8370          | 0.0025        |
| **GPT-4 (0125)**  | Chinese      | 0.6256       | 0.2098        | 0.1646         | 0.8358          | 0.0033        |
| **GPT-3.5 Turbo** | English      | 0.7328       | 0.1288        | 0.1384         | 0.8616          | 0.0000        |
| **GPT-3.5 Turbo** | Chinese      | 0.6754       | 0.1598        | 0.1648         | 0.8352          | 0.0038        |
| **Qwen2-72B**     | English      | 0.5964       | 0.2314        | 0.1722         | 0.8280          | 0.0028        |
| **Qwen2-72B**     | Chinese      | 0.5312       | 0.2736        | 0.1952         | 0.8050          | 0.0134        |
| **LLaMA 3.1**     | English      | 0.4492       | 0.3056        | 0.2452         | 0.7552          | 0.0055        |
| **LLaMA 3.1**     | Chinese      | 0.2790       | 0.4794        | 0.2416         | 0.7584          | 0.0022        |




## CSI Example: Top Words Distribution

| **Frequency** | **English**                                                  | **Chinese**                                                  |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Top 100**   | I, has, help, have, use, were, people, We, AI, him, made, take, individuals, research, practices, improve, industry, team, sense, found, does, ... | 是, 我, 会, 自己, 学习, 帮助, 他, 信息, 应用, 时间, 工作, 可能, 系统, 设计, 人们, 情况, 研究, 需求, 对话, 质量, ... |
| **Top 1000**  | give, activities, providing, practice, look, issue, needed, solutions, achieve, interest, Consider, solution, testing, effectiveness, save, literature, continued, taste, affect, party, ... | 程序, 做, 主题, 行为, 购买, 请问, 压力, 形式, 表格, 瑜伽, 美国, 排序, 显示, 交易, 话题, 保障, 氛围, 声音, 表明, 倒入, ... |
| **Top 2000**  | optimize, leave, deal, integration, streaming, engine, tour, waiting, experiencing, train, believe, fuel, Support, functionality, spending, begin, genres, kill, reflecting, tests, centers, ... | 评论, 成就, 深度, 加密, 整理, 删除, 毕业, 二氧化碳, 精力, 差, 取, 球员, 涵盖, 编码, 电, 芝士, 端, 享用, 进化, 感激, ... |
| **Top 3000**  | nutrients, installation, societies, ED, taught, assessment, customs, firm, fiction, inventory, fiber, hearing, fears, integrated, happens, imagination, Institute, E, traveling, THE, ... | 德国, 火车, 集成, 加快, 装, 鉴别, 废物, 贾宝玉, 掉, 挑战性, 举行, 针对性, 不确定性, 玫瑰, 遭受, 沉浸, 牌, 用餐, 船, 积分, ... |
| **Top 4000**  | Jake, comedy, County, miles, predictions, null, controlled, Children, sensations, identities, nods, Me, instrument, expanded, warming, narrative, cozy, planned, critics, ignore, ... | 租金, 生抽, 攻略, 销售量, 教堂, 对抗, 神经元, 仙人掌, 体检, 外貌, 乘积, 工作者, 样子, 企鹅, 心得, 资格, 入睡, 证言, 饮水, 生效, ... |
| **Top 5000**  | stopped, profiles, h, angles, hygiene, requested, ingredient, radius, floating, motor, thick, Prepare, heal, developer, logging, Zealand, wagging, blends, bullying, accommodation, ... | 医药, 接, 意境, 阳台, 公主, 鸡腿, 周期表, 高山, 开设, 元音, 买卖, 滑动, 遗迹, 密钥, 举例, 猫科, 仿真, 恭喜, 携手, 吸气, ... |