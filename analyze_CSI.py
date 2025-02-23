from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import os
from utils import (
    list_subdirs,
    compare_multiple_dicts,
    load_csi,
    load_test_datas

)

import re








def generate_word_cloud(words, filename, lang, reverse_dict):
    # 给每个单词赋一个默认频率值
    word_freq = {word: len(words) - reverse_dict[word] + 1 for word in words}
    
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



def analyze_result(testing_file, common_words, reverse_dict, lang, experiment_folder, model, TC):
    
    
    test_datas = load_test_datas(testing_file)
    inconsistent_words, comedy_words, tragedy_words, neutral_words = compare_multiple_dicts(test_datas, common_words)
    
    # Calculate scores
    reluctations = 0
    for ts_data in test_datas:
        ts_count = Counter(ts_data.values())
        reluctations += ts_count['NEUTRAL']

    reluct_score = reluctations / (TC * len(common_words)) # test times * number of test set size

    neu_score = (len(neutral_words) + len(inconsistent_words)) / len(common_words)
    com_score = len(comedy_words) / len(common_words)
    tgd_score = len(tragedy_words) / len(common_words)
    
    # Generate word clouds
    neutral_words_ad = neutral_words[:]
    for word in inconsistent_words:
        neutral_words_ad.append(next(iter(word)))
    neutral_words_ad = sorted(neutral_words_ad, key = lambda x: reverse_dict[x])

    generate_word_cloud(neutral_words_ad, f'{experiment_folder}/neutral_words', lang, reverse_dict)
    generate_word_cloud(comedy_words, f'{experiment_folder}/comedy_words', lang, reverse_dict)
    generate_word_cloud(tragedy_words, f'{experiment_folder}/tragedy_words', lang, reverse_dict)

    # Output markdown report
    inconsistent_words_str = "\n".join([f"{key}: {', '.join(value)}" for d in inconsistent_words[:50] for key, value in d.items()])
    consistency_score = 1-(len(inconsistent_words) / len(common_words))

    md_out = f"""
# Model {model} Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| {model} | {lang} | {com_score:.4f} | {tgd_score:.4f} | {neu_score:.4f} | {consistency_score:.4f} | {reluct_score} |

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
### In-consistency Rate: {(len(inconsistent_words) / len(common_words)):.4f}

Top 50 Inconsistent Words:
```

{inconsistent_words_str}

```



"""



    report_path = os.path.join(experiment_folder, 'report.md')
    with open(report_path, 'w', encoding='utf-8') as fout:
        fout.write(md_out)

    return {
        'Model': model,
        'Language': lang,
        'Optimism': com_score,
        'Pessimism': tgd_score,
        'Neutrality': neu_score,
        'Consistency': consistency_score,
        'Reluctant': reluct_score
    }

def generate_summary_report(all_scores, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    summary_md = "# Summary Report of All Models\n\n"
    summary_md += "| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |\n"
    summary_md += "|-------|----------|----------|-----------|------------|-------------|-----------|\n"
    
    for scores in all_scores:
        summary_md += f"| {scores['Model']} | {scores['Language']} | {scores['Optimism']:.4f} | {scores['Pessimism']:.4f} | {scores['Neutrality']:.4f} | {scores['Consistency']:.4f} | {scores['Reluctant']:.4f} |\n"
    
    summary_path = os.path.join(output_folder, 'summary_report.md')
    with open(summary_path, 'w', encoding='utf-8') as fout:
        fout.write(summary_md)
    print(f"Summary reports into: {summary_path}")




if __name__ == "__main__":
    testing_folder = './exp_results_bcs'
    output_folder = './model_reports'
    all_scores = []
    
    subdirs = list_subdirs(testing_folder)
    print(f"Found subdirectories in {testing_folder}: {', '.join(subdirs)}")
    
    for subdir in subdirs:
        files_in_subdir = os.listdir(subdir)
        csv_files = [file for file in files_in_subdir if file.endswith('.csv')]
        if csv_files:
            csv_file = csv_files[0]
            testing_file = os.path.join(subdir, csv_file)
            file_name = csv_file.replace('.csv', '')
            parts = file_name.split('-')
            TestCount = int(re.search(r"(?<=TC)\d+", subdir).group())
            lang = parts[-1]
            model = '-'.join(parts[:-1])
            common_words = load_csi(lang)
            reverse_dict = {v: k for k, v in common_words.items()}
            print(f"Processing experiment directory: {subdir}")
            print(f"Model: {model}, Language: {lang}")
            scores = analyze_result(testing_file, common_words, reverse_dict, lang, subdir, model, TestCount)
            all_scores.append(scores)
        else:
            print(f"No CSV file found in {subdir}")