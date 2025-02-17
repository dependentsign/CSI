import argparse
import os
from datetime import datetime
import csv
import pandas as pd
import random
import re
import json
from tqdm import tqdm
from prompt import ch_prompt, eng_prompt
from utils import get_llm_response







def create_experiment_folder(model, context_num, test_count, base_path="./exp_results"):
    """
    Create an experiment folder with a timestamp, model name, test count, and context number.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    experiment_folder = os.path.join(base_path, f"{timestamp}_M{model}_TC{test_count}_CN{context_num}")
    os.makedirs(experiment_folder, exist_ok=True)
    return experiment_folder

def generate_testfile(test_count, testing_file, instruction_prompt, common_words):
    """
    Generate a test CSV file containing shuffled questions and response placeholders.
    """
    output_file = testing_file
    csv_output = []
    word_list = common_words  # All questions in the dictionary

    for shuffle_count in range(test_count):
        question_indices = list(word_list.keys())  # Get question indices

        # Shuffle question indices
        random.shuffle(question_indices)

        # Create questions based on shuffled indices
        questions = [f'{index}. {word_list[question]}' for index, question in enumerate(question_indices, 1)]
        # Add instruction prompt and questions to csv_output
        csv_output.append([f'Prompt: {instruction_prompt}'] + questions)
        # Add the order of questions
        csv_output.append([f'order-{shuffle_count}'] + question_indices)
        # Add placeholders for responses
        
        csv_output.append([f'shuffle{shuffle_count}'] + [''] * len(question_indices))

    # Transpose csv_output so each row corresponds to a column in the CSV file
    csv_output = list(zip(*csv_output))

    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_output)

def extract_items(text):
    """
    Extract items from the LLM response text.
    Each line should follow the format '1. Item - Category'.
    """
    pattern = r'^\d+.*$'

    results = []
    for line in text.splitlines():
        match = re.match(pattern, line.strip(), re.IGNORECASE)
        if match:
            results.append(f"{line}")
    return "\n".join(results)

def convert_results(result, column_header):
    """
    Convert the LLM response into a list of categories.
    """
    result = extract_items(result)
    if not result:
        print('please check the LLM\'s response')
        raise Exception
    pattern = r"喜剧|悲剧|comedy|tragedy"
    result_list = []
    for element in result.split('\n'):
        if element.strip():
            match = re.search(pattern, element, re.IGNORECASE)
            if match:
                if re.search('comedy', element, re.IGNORECASE) or re.search('喜剧', element, re.IGNORECASE):
                    result_list.append('COMEDY')
                elif re.search('tragedy', element, re.IGNORECASE) or re.search('悲剧', element, re.IGNORECASE):
                    result_list.append('TRAGEDY')
                else:
                    result_list.append('NEUTRAL')
            else:
                result_list.append('NEUTRAL')  # Append 'NEUTRAL' if no match is found
    return result_list

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run LLM experiments with different parameters.')
    parser.add_argument('--model', type=str, default='gpt-4o', help='Model name to use.')
    parser.add_argument('--context_num', type=int, default=30, help='Context length.')
    parser.add_argument('--test_count', type=int, default=2, help='Number of tests.')
    parser.add_argument('--lang', type=str, choices=['Chinese', 'English'], default='English', help='Language to use.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Set experiment parameters
    model = args.model
    context_num = args.context_num
    test_count = args.test_count
    lang = args.lang

    # Read common nouns from file and create a dictionary
    common_words = {}

    if lang == 'Chinese':
        with open('./comon_nouns/chn_words.jsonl', 'r', encoding='utf-8') as fr:
            for index, line in enumerate(fr):
                # Map index+1 to words (strip white space)
                common_words[index + 1] = json.loads(line)['word']
        instruction = ch_prompt
    elif lang == 'English':
        with open('./comon_nouns/eng_words.jsonl', 'r', encoding='utf-8') as fr:
            for index, line in enumerate(fr):
                # Map index+1 to words (strip white space)
                common_words[index + 1] = json.loads(line)['word']
        instruction = eng_prompt
    else:
        raise ValueError(f"Unsupported language: {lang}. Please use 'Chinese' or 'English'.")

    # Create experiment folder
    experiment_folder = create_experiment_folder(model=model, context_num=context_num, test_count=test_count)

    print(f"Experiment folder: {experiment_folder}")

    # Generate test file (CSV)
    testing_file = os.path.join(experiment_folder, f"{model}-{lang}.csv")
    generate_testfile(
        test_count=test_count,
        testing_file=testing_file,
        instruction_prompt=instruction,
        common_words=common_words,
    )

    # Main execution
    total_iterations = test_count

    # Read generated CSV file into DataFrame
    df = pd.read_csv(testing_file, encoding='utf-8')

    # Identify columns that start with 'order' (these columns represent question order)
    order_columns = [col for col in df.columns if col.startswith("order")]

    insert_count = 0  # For tracking insertion count in the DataFrame
    CONTEXT_LEN = context_num

    # If folders don't exist, create prompts and responses folders
    prompts_folder = os.path.join(experiment_folder, "prompts")
    responses_folder = os.path.join(experiment_folder, "responses")
    os.makedirs(prompts_folder, exist_ok=True)
    os.makedirs(responses_folder, exist_ok=True)

    # Initialize progress bar
    with tqdm(total=total_iterations) as pbar:
        for shuffle_count, order_col in enumerate(order_columns):
            questions_column_index = df.columns.get_loc(order_col) - 1

            # Get list of questions for this shuffle
            word_list = df.iloc[:, questions_column_index].astype(str)

            # Split questions into CONTEXT_LEN sized chunks
            separated_questions = [
                word_list[j:j + CONTEXT_LEN]
                for j in range(0, len(word_list), CONTEXT_LEN)
            ]

            # Prepare question strings
            word_list_chunks = [
                '\n'.join([f"{idx + 1}.{q.split('.', 1)[1]}" for idx, q in enumerate(questions)])
                for questions in separated_questions
            ]
            print(f"This test will run for {len(word_list_chunks)} iterations.")

            column_header = f'shuffle{shuffle_count}'

            result_string_list = []
            for questions_string in tqdm(word_list_chunks):
                inputs = [
                    {"role": "user", "content": instruction + '\n' + questions_string}
                ]
                result = get_llm_response(inputs, model=model)

                # Append result to list
                result_string_list.append(result.strip())

                # Write prompt and response to files
                with open(f'{prompts_folder}/{model}-shuffle{shuffle_count}.txt', "a", encoding='utf-8') as prompt_file:
                    prompt_file.write(f'{inputs}\n====\n')
                with open(f'{responses_folder}/{model}-shuffle{shuffle_count}.txt', "a", encoding='utf-8') as response_file:
                    response_file.write(f'{result}\n====\n')

            result_string = '\n'.join(result_string_list)

            # Convert LLM results to a list of categories
            result_list = convert_results(result_string, column_header)

            # Insert results into DataFrame
            if column_header in df.columns:
                df[column_header] = result_list
            else:
                df.insert(
                    loc=questions_column_index + insert_count + 2,
                    column=column_header,
                    value=result_list
                )
                insert_count += 1

            # Update progress bar
            pbar.update(1)

    # Write updated DataFrame back to CSV after all iterations are complete
    df.to_csv(testing_file, index=False, encoding='utf-8')

if __name__ == "__main__":
    main()