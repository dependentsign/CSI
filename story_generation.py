# story generation

from tqdm import tqdm
import os


import random


from prompt import eng_story_prompt, chn_story_prompt

from utils import (
    list_subdirs,
    get_llm_response,
    compare_multiple_dicts,
    load_test_datas,
    load_csi
)



def main():

    testing_folder = './exp_results'
    subdirs = list_subdirs(testing_folder)
    print(f"Subdirectories in {testing_folder}: {subdirs}")
    for subdir in subdirs:
        files_in_subdir = os.listdir(subdir)
        csv_files = [file for file in files_in_subdir if file.endswith('.csv')]
        csv_files = next(iter(csv_files))
        testing_file = os.path.join(subdir, csv_files)
        if os.path.exists(testing_file):
            file_name = testing_file.split('/')[-1]
            parts = file_name.replace('.csv', '').split('-')
            lang = parts[-1]
            model = '-'.join(parts[:-1])
            common_words = load_csi(lang)

            print(f"Experiment folder: {subdir}")
            print(f"Model: {model}")
            print(f"Language: {lang}")

        
            test_datas = load_test_datas(testing_file)
            _, comedy_words, tragedy_words, _ = compare_multiple_dicts(test_datas, common_words)
            
        
            # Seed words generation
            seed_words_dict = dict()
            for i in range(6):
                seed_words_dict[f'positive_{i}'] = []

            for i in range(6):
                for j in range(100):
                    sampled_items = random.sample(tragedy_words, 5 - i) + random.sample(comedy_words, i)
                    random.shuffle(sampled_items)
                    seed_words_dict[f'positive_{i}'].append(sampled_items)

            # Create folders for stories and prompts
            stories_folder = os.path.join(subdir, "stories")
            prompts_folder = os.path.join(subdir, "prompts")
            os.makedirs(stories_folder, exist_ok=True)
            os.makedirs(prompts_folder, exist_ok=True)

            # Loop through degrees and seed words with progress bar
            for degree, seed_words in tqdm(seed_words_dict.items(), desc="Generating stories"):

                prompt_file_path = os.path.join(prompts_folder, f'prompt_{degree}.txt')
                
                with open(prompt_file_path, "a", encoding='utf-8') as prompt_file:
                    for seed_word in tqdm(seed_words):
                        if lang == 'Chinese':
                            words_str = '，'.join(seed_word)
                            instruction = chn_story_prompt
                        else:
                            words_str = ', '.join(seed_word)
                            instruction = eng_story_prompt
                        
                        content = instruction + words_str
                        inputs = [{"role": "user", "content": content}]
                        
                        # Save prompt used in the story
                        prompt_file.write(f'Prompt: {content}\n')
                        
                        # Get the response from LLM
                        result = get_llm_response(inputs, model=model)
                        
                        # Save the story to the corresponding file
                        story_file_path = os.path.join(stories_folder, f'{degree}-seed_{words_str}.txt')
                        with open(story_file_path, "a", encoding='utf-8') as response_file:
                            response_file.write(f'{result}\n')



if __name__ == "__main__":
    main()
