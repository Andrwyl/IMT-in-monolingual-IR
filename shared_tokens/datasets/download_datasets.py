from datasets import load_dataset
import os

train_files_path = os.path.abspath(os.path.join(os.getcwd(), '../train_files'))

#load and save every training dataset
langs = ['fa', 'hi', 'bn', 'ru', 'fr', 'es', 'fi', 'id',
         'sw', 'te', 'ar', 'th', 'zh', 'ja']

for lang in langs:
    data_files = {'train': [f'{train_files_path}/miracl_train_bm25_neg_top100_random30.{lang}.jsonl']}
    ds = load_dataset('Tevatron/msmarco-passage',
                      'default',
                      data_files=data_files, cache_dir = None, use_auth_token=True)['train']
    ds.save_to_disk(f'{lang}-training-unfiltered')

#load and save all the encoding datasets
langs = ['fa', 'bn', 'hi']

for lang in langs:
    ds_query = load_dataset('miracl/miracl',
                            lang,
                            data_files = None, cache_dir = None, use_auth_token = None)['dev']
    
    ds_corpus = load_dataset('miracl/miracl',
                             lang,
                             data_files = None, cache_dir = None, use_auth_token = True)['train']
    
    ds_query.save_to_disk(f'{lang}-queryencodings-unfiltered')
    ds_corpus.save_to_disk(f'{lang}-encodings-unfiltered')

