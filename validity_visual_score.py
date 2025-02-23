import os
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import matplotlib.patches as mpatches

def contains_chinese(text):
    """Check if the text contains Chinese characters."""
    return re.search(r'[\u4e00-\u9fff]', text) is not None

def process_file(file_path, filename):
    """Process the file and extract the tragedy degree score."""
    with open(file_path, 'r', encoding='utf-8') as file:
        result = file.read()
    
    try:
        if contains_chinese(filename):
            res = json.loads(result)
            score = res['悲剧程度']
        else:
            res = json.loads(result)
            score = res['TragedyDegree']
    except:
        pattern = r'{(.*?)}'
        match = re.search(pattern, result, re.DOTALL)
        if match:
            json_content = f"{{{match.group(1)}}}"
            res = json.loads(json_content)
            score = res['悲剧程度'] if contains_chinese(filename) else res['TragedyDegree']
        else:
            print(f"No valid JSON found in {filename}.")
            return None
    
    return score

def collect_data(base_folder):
    """Collect data from all experiment files."""
    all_data = []
    mapping = {
        'score_positive_0': '5/5',
        'score_positive_1': '4/5',
        'score_positive_2': '3/5',
        'score_positive_3': '2/5',
        'score_positive_4': '1/5',
        'score_positive_5': '0/5'
    }
    for testing in tqdm(os.listdir(base_folder)):
        if testing.startswith('.'):
            continue
        model = testing.split('_')[2][1:]
        experiment_folder = os.path.join(base_folder, testing)
        score_folder = os.path.join(experiment_folder, "story_scores")
        if not os.path.exists(score_folder):
            continue
        
        for filename in os.listdir(score_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(score_folder, filename)
                degree = filename.split('-')[0]
                score = process_file(file_path, filename)
                if score is not None:
                    lang = 'Chinese' if contains_chinese(filename) else 'English'
                    all_data.append({
                        'Model': model,
                        'Language': lang,
                        'Groups': mapping[degree],
                        'Sentiment Score': score
                    })
    
    return pd.DataFrame(all_data)

def plot_model_data(data, model, output_folder):
    """Plot the sentiment score data for a specific model."""
    sns.set_context("paper", font_scale=2)
    
    groups = sorted(data['Groups'].unique())
    positions = range(len(groups))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 8))

    # Define specific RGB color values
    light_green = (235/255, 254/255, 232/255)  # Green (235, 254, 232)
    light_blue = (230/255, 230/255, 253/255)   # Blue (230, 230, 253)
    
    colors = {'Chinese': light_green, 'English': light_blue}
    box_plots = []
    for i, lang in enumerate(['Chinese', 'English']):
        lang_data = data[data['Language'] == lang]
        
        stats = lang_data.groupby('Groups')['Sentiment Score'].agg(['mean', 'std', 'min', 'max', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])
        stats.columns = ['mean', 'std', 'min', 'max', 'q1', 'q3']

        means = stats['mean']
        ax.plot([p + (i-0.5)*width for p in positions], means, marker='o', linestyle='-' if lang == 'Chinese' else '--',
                color='black', label=f'{lang} Mean', zorder=3)

        bp = ax.boxplot([lang_data[lang_data['Groups'] == group]['Sentiment Score'] for group in groups],
                        positions=[p + (i-0.5)*width for p in positions],
                        widths=width,
                        patch_artist=True,
                        showfliers=False,
                        zorder=2)

        for patch in bp['boxes']:
            patch.set_facecolor(colors[lang])
        
        box_plots.append(mpatches.Patch(facecolor=colors[lang], edgecolor='black', label=f'{lang} Data'))

    ax.set_xlabel('Proportion of Tragedy Words', fontsize=30)
    ax.set_ylabel('Generated Story Sentiment Score', fontsize=30)
    plt.text(0.23, 0.94, f'{model}', fontsize=30, transform=plt.gca().transAxes, ha='center', color='blue')

    ax.set_xticks([p + width/2 for p in positions])
    ax.set_xticklabels(groups)
    ax.set_yticks([i+1 for i in range(10)])

    # Set Y-axis limits
    ax.set_ylim(0, 11)

    legend_elements = [plt.Line2D([0], [0], color='black', linestyle='-', marker='o', label='Chinese Mean'),
                       plt.Line2D([0], [0], color='black', linestyle='--', marker='o', label='English Mean')]
    legend_elements.extend(box_plots)
    
    # Position the legend in the upper right inside the plot
    ax.legend(handles=legend_elements, fontsize=30, 
              loc='upper right', bbox_to_anchor=(0.45, 0.93))
    
    ax.grid(True, linestyle='--', alpha=0.6, zorder=1)

    save_path = os.path.join(output_folder, f'{model}_sentiment_score.png')
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Main function to process data and generate plots."""
    base_folder = './exp_results_bcs'
    output_folder = './model_reports'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    all_data = collect_data(base_folder)
    
    for model in all_data['Model'].unique():
        model_data = all_data[all_data['Model'] == model]
        plot_model_data(model_data, model, output_folder)
    
    print("All plots have been generated and saved.")

if __name__ == "__main__":
    main()