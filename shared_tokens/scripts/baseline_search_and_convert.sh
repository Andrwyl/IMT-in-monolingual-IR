if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <argument> <argument>"
    exit 1
fi


model_lang="$1"
encoding_lang="$2"

shared_token_dir="$(cd "$(pwd)/.." && pwd)"


python -m tevatron.faiss_retriever \
--query_reps ${shared_token_dir}/results/baselines/encodings/${model_lang}_${encoding_lang}_queries_emb.pt \
--passage_reps ${shared_token_dir}/results/baselines/encodings/${model_lang}_${encoding_lang}_corpus_emb.pt \
--depth 100 \
--batch_size -1 \
--save_text \
--save_ranking_to ${shared_token_dir}/results/baselines/rankings/${model_lang}_${encoding_lang}.txt

python -m tevatron.utils.format.convert_result_to_trec --input ${shared_token_dir}/results/baselines/rankings/${model_lang}_${encoding_lang}.txt --output ${shared_token_dir}/results/baselines/rankings/${model_lang}_${encoding_lang}.trec
