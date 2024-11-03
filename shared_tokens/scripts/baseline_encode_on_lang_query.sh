if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <argument> <argument>"
    exit 1
fi

shared_token_dir="$(cd "$(pwd)/.." && pwd)"


model_lang="$1"
encoding_lang="$2"

torchrun --nproc_per_node 1 ../../tevatron/src/tevatron/driver/encode.py \
  --output_dir=temp_out \
  --model_name_or_path ${shared_token_dir}/results/baselines/model/${model_lang} \
  --per_device_eval_batch_size 156 \
  --dataset_name miracl/miracl:${encoding_lang}/dev \
  --encode_is_qry \
  --q_max_len 64 \
  --run_filter false \
  --encoded_save_path ${shared_token_dir}/results/baselines/encodings/${model_lang}_${encoding_lang}_queries_emb.pt --negatives_x_device