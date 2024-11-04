# Running the Filtering Scripts

Below are descriptions of the four python scripts used for filtering. The end of the markdown contains an example workflow

## 1. get_overlapping.py 

```
get_overlapping.py <base language> <languages to keep>
```

Argument 1 will be the language we are analyzing. Argument 2 will be the language of all the tokens we would like to keep from the datasets of the language Argument 1. The output is a list of token ids that appear in the corpora of Argument 1 that are not in the same script as Argument 1. 

Note we are actually keeping all languages in the same script as specified in Section 2.2 of our paper. As such, a language can have multiple 'languages to keep.' `filtering.md` tells you for each base language, which languages to use as the languages to keep.

Important Note: In order to run any of the filterings below for a language (whether you are filtering the training, the passages, or the queries), this script must be run first for the language at least once. ` shared_tokens/overlapping_tokens/{lang}_overlapping_token_ids.json ` must exist.

## 2. filter_dataset_training.py 

```
filter_dataset_training.py language
```

This will load in the base training dataset in the language, and output a new dataset that has all non-self script tokens removed. 

## 3. filter_dataset_encoding[_query].py

```
filter_dataset_encoding[_query].py language
```

This will load in the base encoding dataset (or the queries) in the language, and output a new dataset with all non-self script tokens removed just like above

## Example Workflow

Suppose we'd like to get the filtered training dataset for the language thai (th) and the filtered eval datasets for the language bengali (bn).

Remember, since we'd like to filter in the two languages th and bn, their respective ` shared_tokens/overlapping_tokens/{lang}_overlapping_token_ids.json ` must exist

### First, get the list of token ids we'd like to filter

```
python get_overlapping.py th th
python get_overlapping.py bn bn
```

### Next run the filtering scripts

```
python filter_dataset_training.py th
python filter_dataset_encoding.py bn
python filter_dataset_encoding_query.py bn
```
Now, the filtered datasets should be stored in

` shared_tokens/datasets `


