# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:55:16 2020

@author: compute
"""


from gensim.models import KeyedVectors, Word2Vec
import gensim.downloader as api
import time
import tempfile

#%%
start_time = time.time()
model_google = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print("--- Loaded model in %s seconds ---" % (time.time() - start_time))

start_time = time.time()
word= "water"
candidate_words = model_google.most_similar(word, topn=5)
word_choose= candidate_words[0][0]
print(word_choose.lower().replace('_', ' '))
print("--- Found word in %s seconds ---" % (time.time() - start_time))

#%%
start_time = time.time()
model_local= api.load('word2vec-google-news-300')
print("--- Loaded model in %s seconds ---" % (time.time() - start_time))

start_time = time.time()
word= "water"
candidate_words = model_local.most_similar(word, topn=5)
print(word_choose.lower().replace('_', ' '))
print("--- Found word in %s seconds ---" % (time.time() - start_time))

# =============================================================================
# for candidate_word, _ in candidate_word_tuples:
#     candidate_word = candidate_word.lower()
# 
#     # Ignore a candidate word if
#     # it shares prefix (4 character) with original word
#     # it has more than 10 characters
#     # it has been tried earlier for this word
#     if word[:4] == candidate_word[:4] or len(candidate_word) > 10 or candidate_word:
#         continue
# 
#     # associated_word_mapping[word].append(candidate_word)
#     print(candidate_word.lower().replace('_', ' '))
# =============================================================================
