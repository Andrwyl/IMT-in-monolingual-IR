if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <argument> <argument>"
    exit 1
fi

shared_token_dir="$(cd "$(pwd)/.." && pwd)"

model_lang="$1"
encoding_lang="$2"

torchrun --nproc_per_node 1 ../../tevatron/src/tevatron/driver/encode.py \
  --output_dir=temp_out \
  --model_name_or_path ${shared_token_dir}/results/baselines/models/${model_lang} \
  --per_device_eval_batch_size 256 \
  --dataset_name miracl/miracl-corpus:${encoding_lang} \
  --p_max_len 256 \
  --run_filter false \
  --encoded_save_path ${shared_token_dir}/results/baselines/encodings/${model_lang}_${encoding_lang}_corpus_emb.pt --negatives_x_device
