import json 
import datasets 
import sys
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')
target_lang = sys.argv[1]

training_dataset = datasets.load_from_disk(f'../../datasets/{target_lang}-training-unfiltered')

with open(f'../../overlapping_tokens/{target_lang}_overlapping_token_ids.json', 'r') as file:
    filtered_token_ids = json.load(file)


def filter_train_overlapping(example):
    query = example['query']
    positives = example['positives']
    negatives = example['negatives']

    

    filtered_query = [token for token in query if token not in filtered_token_ids]
    filtered_positives = [[token for token in passage if token not in filtered_token_ids] for passage in positives]
    filtered_negatives = [[token for token in passage if token not in filtered_token_ids] for passage in negatives]

    example['query'] = filtered_query
    example['positives'] = filtered_positives
    example['negatives'] = filtered_negatives
    return example

filtered_dataset = training_dataset.map(filter_train_overlapping)

filtered_dataset.save_to_disk(f'../../datasets/{target_lang}-training-filtered')



