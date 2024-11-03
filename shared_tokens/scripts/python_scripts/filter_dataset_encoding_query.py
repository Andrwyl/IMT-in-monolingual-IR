import json 
import datasets 
import sys

target_lang = sys.argv[1]

encode_dataset = datasets.load_from_disk(f'../../datasets/{target_lang}-queryencodings-unfiltered')

#load in overlapping tokens
with open(f'../../overlapping_tokens/{target_lang}_overlapping_token_ids.json', 'r') as file:
    overlapping_tokens = json.load(file)

def filter_overlapping(example):
    text = example['text']
    filtered_text = [token for token in text if token not in overlapping_tokens]
    example['text'] = filtered_text
    return example


filtered_dataset = encode_dataset.map(filter_overlapping)
filtered_dataset.save_to_disk(f'../../datasets/{target_lang}-queryencodings-filtered')