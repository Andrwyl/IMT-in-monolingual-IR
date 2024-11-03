#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

shared_token_dir="$(cd "$(pwd)/.." && pwd)"

echo $shared_token_dir

language="$1"

torchrun --nproc_per_node 2 ../../tevatron/src/tevatron/driver/train.py \
  --output_dir ${shared_token_dir}/results/filtered/models/${language} \
  --model_name_or_path bert-base-multilingual-cased \
  --tokenizer_name bert-base-multilingual-cased \
  --save_steps 20000 \
  --dataset_name Tevatron/msmarco-passage \
  --per_device_train_batch_size 64 \
  --train_dir ${shared_token_dir}/train_files/miracl_train_bm25_neg_top100_random30.${language}.jsonl \
  --train_n_passages 2 \
  --learning_rate 1e-5 \
  --q_max_len 32 \
  --p_max_len 256 \
  --num_train_epochs 40 \
  --logging_steps 10 \
  --run_filter true \
  --overwrite_output_dir --negatives_x_device --target_lang ${language}