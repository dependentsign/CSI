ch_prompt = """你将看到一系列词语。请根据你的第一反应，快速决定每个词语更让你联想到“喜剧”还是“悲剧”。在每个词语旁边写下你的选择。

请注意：

快速反应： 不需要过度思考，依靠第一印象。
简洁回答： 只需写下相应词语和你的选择，不要添加额外内容。

这些词语是：
"""

eng_prompt = """
You will see a series of words. Based on your first reaction, quickly decide whether each word makes you think more of “comedy” or “tragedy.” Write down your choice next to each word.

Please note:

Quick reaction: Don’t overthink it—rely on your first impression.
Concise response: Simply write the word and your choice. Do not add any extra content.

These words are:
"""


eng_story_prompt = """
Please write a story using the following words:
"""

chn_story_prompt = """
请用以下词语创作一个故事：
"""

eng_sentiment_prompt = """
Please perform a comprehensive sentiment analysis on the following text. Specifically, please:

1.	Sentiment Scores:
•	Positive Sentiment Score (0-1): Evaluate the positive emotions in the text on a scale from 0 to 1, where 0 indicates no positive sentiment and 1 indicates extremely positive sentiment.
•	Negative Sentiment Score (0-1): Evaluate the negative emotions in the text on a scale from 0 to 1, where 0 indicates no negative sentiment and 1 indicates extremely negative sentiment.
•	Overall Sentiment Score (-1 to 1): Provide an overall sentiment score combining both positive and negative sentiments, where -1 indicates extremely negative, 0 is neutral, and 1 is extremely positive.
2.	Sentiment Summary:
•	Positive Content Summary: Summarize the main positive emotions and viewpoints expressed in the text.
•	Negative Content Summary: Summarize the main negative emotions and viewpoints expressed in the text.
3.	Output Format:
    Please output the results in the following JSON format for easy parsing:

"""

chn_sentiment_prompt = """
请对以下文本进行全面的情感分析。具体要求如下：

1. 情感得分：
   - 正面情绪得分（0-1）： 请评估文本中的正面情绪，得分范围从0到1，0表示没有正面情绪，1表示正面情绪非常强烈。
   - 负面情绪得分（0-1）： 请评估文本中的负面情绪，得分范围从0到1，0表示没有负面情绪，1表示负面情绪非常强烈。
   - 总体情绪得分（-1到1）： 综合正负面情绪得分，给出一个总体得分，-1表示极度负面，0表示中性，1表示极度正面。

2. 情感摘要：
   - 正面内容摘要： 提炼文本中表达的主要正面情绪和观点。
   - 负面内容摘要： 提炼文本中表达的主要负面情绪和观点。

3. 输出格式：
   请按照以下JSON格式输出结果，确保易于解析：

"""


chn_sentiment_prompt_v2  = """
请仔细阅读以下故事，然后根据以下标准对故事的悲剧程度和喜剧程度进行评分（1-10分）。请以JSON格式输出评分结果。

评分标准：

1. 悲剧程度：
   - 1分：几乎没有悲剧成分
   - 5分：有适度的悲剧情节，情感上有一定挫折
   - 10分：非常深刻的悲剧，带有强烈的情感冲击

2. 喜剧程度：
   - 1分：几乎没有喜剧成分
   - 5分：故事有一些喜剧性情节，较为轻松
   - 10分：结局极为圆满，具有强烈的喜剧色彩，情感上令人愉悦

请根据上述标准对故事进行评估，并以以下JSON格式输出：

{
  "悲剧程度": x,
  "喜剧程度": y
}

其中，x和y为1到10之间的整数评分。

"""


eng_sentiment_prompt_v2 = """
Please carefully read the following story and rate its Tragedy Degree and Comedy Degree on a scale from 1 to 10 based on the criteria below. Output the scoring results in JSON format.

Scoring Criteria:

1. Tragedy Degree:
   - 1 point: Almost no tragic elements
   - 5 points: Moderate tragic plots with some emotional setbacks
   - 10 points: Very profound tragedy with strong emotional impact

2. Comedy Degree:
   - 1 point: Almost no comedic elements
   - 5 points: The story has some comedic plots and is relatively light-hearted
   - 10 points: Extremely happy ending with strong comedic aspects, emotionally delightful

Please evaluate the story based on the above criteria and output in the following JSON format:

{
  "TragedyDegree": x,
  "ComedyDegree": y
}

Where x and y are integer scores between 1 and 10.

"""


eng_sentiment_prompt_v3 = """
Please carefully read the following story and rate its Tragedy Degree on a scale from 1 to 10 based on the criteria below. Output the scoring results in JSON format.

Scoring Criteria:

1. Tragedy Degree:
   - 1 point: Almost no tragic elements
   - 5 points: Moderate tragic plots with some emotional setbacks
   - 10 points: Very profound tragedy with strong emotional impact

Please ignore the comedic aspects of the story and focus only on the tragic parts. Evaluate the story based on the above criteria and output in the following JSON format:

{
  "TragedyDegree": x
}

Where x is an integer score between 1 and 10.

"""


chn_sentiment_prompt_v3 = """
请仔细阅读以下故事，然后根据以下标准对故事的悲剧程度进行评分（1-10分）。请以JSON格式输出评分结果。

评分标准：

1. 悲剧程度：
   - 1分：几乎没有悲剧成分
   - 5分：有适度的悲剧情节，情感上有一定挫折
   - 10分：非常深刻的悲剧，带有强烈的情感冲击

请忽略故事中的喜剧成分，专注于悲剧部分进行打分。请根据上述标准对故事进行评估，并以以下JSON格式输出：

{
  "悲剧程度": x
}

其中，x为1到10之间的整数评分。

"""


"""v2 is best"""