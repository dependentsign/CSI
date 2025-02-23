from prompt import eng_sentiment_scoring_prompt, chn_sentiment_scoring_prompt
from tqdm import tqdm
import os
from utils import get_llm_response, list_subdirs


testing_folder = './exp_results'
subdirs = list_subdirs(testing_folder)
for subdir in subdirs:
    files_in_subdir = os.listdir(subdir)
    csv_files = [file for file in files_in_subdir if file.endswith('.csv')]
    csv_files = next(iter(csv_files))
    testing_file = os.path.join(subdir, csv_files)
    if not os.path.exists(testing_file):
        continue
    else:
        file_name = testing_file.split('/')[-1]
        parts = file_name.replace('.csv', '').split('-')
        lang = parts[-1]
        model = '-'.join(parts[:-1])

        print(f"Experiment folder: {subdir}")
        print(f"Model: {model}")
        print(f"Language: {lang}")

        stories_folder = os.path.join(subdir, "stories")

        score_degree = {}
        for i in range(6):
            score_degree[f'positive_{i}'] = []

        if lang == 'Chinese':
            instruction = chn_sentiment_scoring_prompt
        else:
            instruction = eng_sentiment_scoring_prompt

        score_folder = os.path.join(subdir, "story_scores")
        os.makedirs(score_folder, exist_ok=True)

        # Iterate through all .txt files in the directory
        for filename in tqdm(os.listdir(stories_folder)):
            if filename.endswith('.txt'):
                file_path = os.path.join(stories_folder, filename)
                degree = filename.split('-')[0]
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    story = file.read()
                    
                content = instruction + story
                inputs = [{"role": "user", "content": content}]

                result = get_llm_response(inputs, model="qwen2-72b-instruct")
                score_file_path = os.path.join(score_folder, f'score_{filename}')
                
                with open(score_file_path, "a", encoding='utf-8') as response_file:
                    response_file.write(f'{result}\n')
                