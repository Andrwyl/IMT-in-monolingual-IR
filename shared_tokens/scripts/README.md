# Training and Evaluation

These bash scripts run the experiments outlined in Section 3 of our paper. The experiments on based on a modified version of Tevatron, a framework that allows for the training and evaluation of retrieval models.

At the end, we will have an example workflow

## Training

`train_on_lang.sh <language>`

Fine-tune the model on the MIRACL training data in language, with all the tokens in a different script as language removed. 

## Evaluation

`encode_on_lang.sh <model language> <eval language>`
`encode_on_lang_query.sh <model language> <eval language>`

Load the model trained on the filtered `model language` data, and encode the evaluation passages and queries of `eval language`

## Ranking

`search_and_convert.sh <model language> <eval language>`

Get the `.trec` rankings representing the performance of the filtered `model language` model on evaluating `eval language` passages and queries. 

`run_eval.sh <model language> <eval language>`

Get the nDCG@10 and Recall@100 scores

## Example Workflow

Suppose we'd like the scores of a model trained on Thai (th) evaluated on Bengali (bn).

```
./train_on_lang.sh th
./encode_on_lang.sh th bn
./encode_on_lang_query.sh th bn
./search_and_convert.sh th bn
./run_eval th bn
```

## Note for Baselines

To run the same experiment on the baseline versions of the datasets (that is with no filtering done), simply do the exact same thing as outlined above but use the scripts with `baseline_` prepended. The baseline of version of the above example workflow is thus:

```
./baseline_train_on_lang.sh th
./baseline_encode_on_lang.sh th bn
./baseline_encode_on_lang_query.sh th bn
./baseline_search_and_convert.sh th bn
./baseline_run_eval th bn
```



