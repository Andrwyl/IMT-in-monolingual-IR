import json

import itertools
import sys

from transformers import AutoTokenizer

from langdetect import detect
from tqdm import tqdm


lang = sys.argv[1]

do_not_filter = sys.argv[2:]

if len(sys.argv) < 3:
    print("Please provide at least one language to keep")
    exit()

tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')

with open(f'../../indexes/{lang}/results-top1.json') as f:
    obj = json.load(f)

lang2found = {k: obj[k] for k in obj if k != "sharded_tokens"}

lang2ntoken = {
    l: list(itertools.chain.from_iterable(lang2found[l])) for l in lang2found
}
all_tokens = lang2ntoken[lang]

#look through to find only non-arabic script

filtered_overlapping_tokens = []

for token in tqdm(all_tokens, 'Finding tokens to filter'):
    try:
        detection = detect(token)
        #this needs to be manually set
        if detection in do_not_filter:
            continue
        else:
            filtered_overlapping_tokens.append(token)
    except:
        continue

filtered_token_ids = tokenizer.convert_tokens_to_ids(filtered_overlapping_tokens)

with open(f'../../overlapping_tokens/{lang}_overlapping_token_ids.json', 'w') as file:
    json.dump(filtered_token_ids, file)