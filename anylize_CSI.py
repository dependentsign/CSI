
# Calculate model consistency
# Read the updated CSV into a DataFrame



from wordcloud import WordCloud
import matplotlib.pyplot as plt

import pandas as pd
import csv
import json
from collections import Counter
import os
from utils import (
    list_subdirs,
    compare_multiple_dicts,
    load_csi,
    load_test_datas

)








def generate_word_cloud(words, filename, lang, reverse_dict):
    # 给每个单词赋一个默认频率值
    word_freq = {word: reverse_dict[word] for word in words}
    
    # 生成词云，设置模式为 RGBA 以支持透明背景
    if lang == 'Chinese':
        wordcloud = WordCloud(font_path='./comon_nouns/PingFang.ttc', width=800, height=400, background_color=None, mode='RGBA').generate_from_frequencies(word_freq)
    else:
        wordcloud = WordCloud( width=600, height=300, background_color=None, mode='RGBA').generate_from_frequencies(word_freq)
    # 保存为透明背景的图片
    wordcloud.to_file(f"{filename}.png")
    
    # 显示词云并保存
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(f'{filename}.png', transparent=True, dpi=300)
    plt.close()



def analyze_result(testing_file, common_words, reverse_dict, lang, experiment_folder, model):
    
    
    test_datas = load_test_datas(testing_file)
    inconsistent_words, comedy_words, tragedy_words, neutral_words = compare_multiple_dicts(test_datas, common_words)
    
    # Calculate scores
    reluctations = coms = trage = 0
    for ts_data in test_datas:
        ts_count = Counter(ts_data.values())
        reluctations += ts_count['NEUTRAL']
        trage += ts_count['TRAGEDY']
        coms += ts_count['COMEDY']

    reluct_score = reluctations / 10000

    neu_score = (len(neutral_words) + len(inconsistent_words)) / 5000
    com_score = len(comedy_words) / 5000
    tgd_score = len(tragedy_words) / 5000
    
    # Generate word clouds
    neutral_words_ad = neutral_words[:]
    for word in inconsistent_words:
        neutral_words_ad.append(next(iter(word)))

    generate_word_cloud(neutral_words_ad, f'{experiment_folder}/neutral_words', lang, reverse_dict)
    generate_word_cloud(comedy_words, f'{experiment_folder}/comedy_words', lang, reverse_dict)
    generate_word_cloud(tragedy_words, f'{experiment_folder}/tragedy_words', lang, reverse_dict)

    # Output markdown report
    inconsistent_words_str = "\n".join([f"{key}: {', '.join(value)}" for d in inconsistent_words[:50] for key, value in d.items()])
    

    md_out = f"""
# Model {model} Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| {model} | {lang} | {com_score:.4f} | {tgd_score:.4f} | {neu_score:.4f} | {(1-(len(inconsistent_words) / 5000)):.4f} | {reluct_score} |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

{' '.join(comedy_words[:50])}

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

{' '.join(tragedy_words[:50])}

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

{' '.join(neutral_words_ad[:50])}

```
### In-consistency Rate: {(len(inconsistent_words) / 5000):.4f}

Top 50 Inconsistent Words:
```

{inconsistent_words_str}

```



"""



    report_path = os.path.join(experiment_folder, 'report.md')
    with open(report_path, 'w', encoding='utf-8') as fout:
        fout.write(md_out)



# 使用参数
if __name__ == "__main__":

    testing_folder = './exp_results'
    subdirs = list_subdirs(testing_folder)
    print(f"Subdirectories in {testing_folder}: {subdirs}")
    for subdir in subdirs:
        files_in_subdir = os.listdir(subdir)

        # 过滤出以 .csv 结尾的文件
        csv_files = [file for file in files_in_subdir if file.endswith('.csv')]
        csv_files = next(iter(csv_files))
        testing_file = os.path.join(subdir, csv_files)
        if os.path.exists(testing_file):
            file_name = testing_file.split('/')[-1]
            parts = file_name.replace('.csv', '').split('-')
            lang = parts[-1]
            model = '-'.join(parts[:-1])
            common_words = load_csi(lang)
            reverse_dict = {}
            reverse_dict = {v: k for k, v in common_words.items()}
            print(f"Experiment folder: {subdir}")
            print(f"Model: {model}")
            print(f"Language: {lang}")
            analyze_result(testing_file, common_words, reverse_dict, lang, subdir, model)
    