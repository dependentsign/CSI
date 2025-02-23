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


chn_sentiment_scoring_prompt  = """
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


eng_sentiment_scoring_prompt = """
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

