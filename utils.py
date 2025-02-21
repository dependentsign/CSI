import os
from openai import OpenAI
import random
import json
import csv

# Set up OpenAI client

client = OpenAI()
def get_llm_response(inputs, model, temp=0, seed=1):
    response = client.chat.completions.create(
        model=model,
        messages=inputs,
        temperature=temp,
        seed=seed
    )
    res = response.choices[0].message.content
    return res

def load_csi(lang):
    common_words = dict()
    if lang == 'Chinese':
        with open('./comon_nouns/chn_words.jsonl', 'r', encoding='utf-8') as fr:
            for index, line in enumerate(fr):
                common_words[index + 1] = json.loads(line)['word']
    elif lang == 'English':
        with open('./comon_nouns/eng_words.jsonl', 'r', encoding='utf-8') as fr:
            for index, line in enumerate(fr):
                common_words[index + 1] = json.loads(line)['word']
    else:
        raise ValueError(f"Unsupported language: {lang}. Please use 'Chinese' or 'English'.")
        
    return common_words

def list_subdirs(directory):
    return [f.path for f in os.scandir(directory) if f.is_dir()]


def compare_multiple_dicts(dict_list, common_words):
    """
    Compare multiple dictionaries and find inconsistencies.
    Returns a dictionary of inconsistencies.
    """
    if len(dict_list) < 2:
        print('Need at least two dictionaries to compare.')
        raise Exception

    inconsistencies = []
    comedy_words = []
    tragedy_words = []
    neutral_words = []
    reference_dict = dict_list[0]

    for key in reference_dict.keys():
        values = [d.get(key, "缺失") for d in dict_list]
        if len(set(values)) > 1:
            inconsistencies.append({common_words[key]: values})
        elif set(values) == {'COMEDY'}:
            comedy_words.append(common_words[key])
        elif set(values) == {'TRAGEDY'}:
            tragedy_words.append(common_words[key])
        elif set(values) == {'NEUTRAL'}:
            neutral_words.append(common_words[key])
    return inconsistencies, comedy_words, tragedy_words, neutral_words

def load_test_datas(testing_file):
    test_datas = []
    with open(testing_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        order_indices = [index for index, column in enumerate(header) if column.startswith("order")]
        
        for i in range(len(order_indices)):
            start = order_indices[i] + 1
            end = order_indices[i+1] - 1 if order_indices[i] != order_indices[-1] else len(header)
            for column_index in range(start, end):
                column_data = {}
                csvfile.seek(0)
                next(reader)
                for row in reader:
                    try:
                        column_data[int(row[start-1])] = row[column_index]
                    except ValueError:
                        print(f'Column {column_index + 1} has error.')
                test_datas.append(column_data)

    return test_datas