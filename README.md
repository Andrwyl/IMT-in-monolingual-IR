# The Impact of Incidental Multilingual Text on Cross-Lingual Transferring in Monolingual Retrieval

This repository provides the code for our paper <em>The Impact of Incidental Multilingual Text on Cross-Lingual Transferring in Monolingual Retrieval</em> published at ECIR 2025

<strong>Links</strong>:

[Paper](https://cs.uwaterloo.ca/~jimmylin/publications/Liu_etal_ECIR2025.pdf)

<strong>Abstract</strong>:

While great progress has been made in non-English monolingual passage retrieval in recent years, there have been few works exploring influential factors behind the cross-lingual transfer capabilities in monolingual passage retrieval. In a retrieval corpus such as Wikipedia, incidental multilingual texts occur in forms including code-switching, translated name entities, and so on. In this work, we study how these naturally occurring multilingual texts impact the crosslingual transfer of dense retrievers on monolingual passage retrieval. Results on 41 pairs of languages suggest that cross-lingual transfer capacity could be largely achieved (> 90% performance) with no incidental multilingual text, yet the effectiveness drop is indeed correlated with the number of queries and documents containing incidental multilingual text. This suggests that cross-lingual transfer may be based on pure semantic understanding of the inputs, but manually injecting more overlapping lexicons can possibly further enhance the transfer capacity.

## Installation

1. Install PyTorch based on your CUDA version
2. Install dependencies and Tevatron (cd to the `tevatron` subdirectory)

```bash
pip install transformers datasets peft
pip install deepspeed accelerate
pip install faiss
cd tevatron
pip install -e .
```

3. In order to faciliate the scoring of the ranks, [Pyserini](https://github.com/castorini/pyserini/tree/master) is required as well.

`pip install pyserini`

All the scripts in `shared_tokens` should be good to run now, as all they need is tevatron installed.

## Filtering datasets

`shared_tokens/scripts/python_scripts` contains the files and a description of how to run the filtering shared tokens section of the paper

## Training and Evaluation

`shared_tokens/scripts` contains the scripts and a description of how to run the training and evaluation comparison of the paper

## Layout of Repository

Our repository follows a relatively flat layout.
At the top level

- `tevatron` 
contains a (minorly) modified version of the Tevatron retrieval framework.

- `shared_tokens` 
contains the files and scripts relevant to our paper. Specifically:
     
     * `shared_tokens/dataset` contains the base training and evaluation datasets for the 14 training languages and 3 evaluation languages in our experiments.
     
     * `shared_tokens/indexes` contains the indexing (the gathering of tokens) of the datasets of the 18 languages supported by MIRACL.
     
     * `shared_tokens/overlapping_tokens` is where the list of non-self tokens for each language is stored. For example:
          - `shared_tokens/overlapping_tokens/th_overlapping_token_ids.json` contains all the token ids in the index of Thai that are not in the same script as Thai
     
     * `shared_tokens/qrels` The qrels for each of each evaluation language.

     * `shared_tokens/results` The bulk of experiment results are stored here.
         - `shared_tokens/results/filtered` contains the folders storing the models and the encoding results (when running filtering)
         - `shared_tokens/results/filtered/encodings` stores the encodings in the form `<model lang>_<eval lang>_corpus_emb.pt`
         - `shared_tokens/results/filtered/models` stores the models in each language
         - `shared_tokens/results/filtered/rankings` stores the rankings of each model language, eval language pair in the form `<model lang>_<eval lang>.trec`
     
         - `shared_tokens/results/baselines` stores an exact mirror of the `filtered` directory, but stores all the results of the baseline (unfiltered) experiments.
     
     * `shared_tokens/scripts` The scripts used for running the filtering, the training, and the evaluation. See details in the directory.
     
     * `shared_tokens/train_files` The MIRACL training data used to fine-tune each language.

## Citation

To do

