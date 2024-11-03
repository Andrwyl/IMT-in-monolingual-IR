if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <argument> <argument>"
    exit 1
fi

shared_token_dir="$(cd "$(pwd)/.." && pwd)"

model_lang="$1"
encoding_lang="$2"

python -m pyserini.eval.trec_eval -c -mrecip_rank -mrecall.100 -mndcg_cut.10 ${shared_token_dir}/qrels/${encoding_lang}.dev.tsv ${shared_token_dir}/results/filtered/rankings/${model_lang}_${encoding_lang}.trec