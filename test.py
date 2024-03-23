import collections
import os
import io
import math
import torch
from torch import nn
import torch.nn.functional as F
import torchtext.vocab as Vocab
import torch.utils.data as Data
import spacy
from spacy.tokens import Doc
PAD, BOS, EOS = '<pad>', '<bos>', '<eos>'  # 序列符

texts = [
    "这是一个例子句子。",
    "另一个用于演示的例子。"
]

# 将一个序列中所有的词记录在all_tokens中以便之后构造词典，然后在该序列后面添加PAD直到序列
# 长度变为max_seq_len，然后将序列保存在all_seqs中
def process_one_seq(seq_tokens, all_tokens, all_seqs, max_seq_len):
    all_tokens.extend(seq_tokens)
    seq_tokens += [EOS] + [PAD] * (max_seq_len - len(seq_tokens) - 1)
    all_seqs.append(seq_tokens)

# 使用所有的词来构造词典。并将所有序列中的词变换为词索引后构造Tensor
def build_data(all_tokens, all_seqs):
    vocab = Vocab.Vocab(collections.Counter(all_tokens))
    indices = [[vocab.stoi[w] for w in seq] for seq in all_seqs]
    return vocab, torch.tensor(indices)

all_tokens = []
all_seqs = []

max_seq_len = 10




for text in texts:
    seq_tokens = list(text)  # 这里假设每个字符为一个词
    process_one_seq(seq_tokens, all_tokens, all_seqs, max_seq_len)
print(all_tokens)
print(all_seqs)
nlp = spacy.load("zh_core_web_sm")
counter=collections.Counter(all_tokens)
doc = Doc(nlp.vocab, words=list(counter.keys()), spaces=[True]*len(counter))

words = list(counter.keys())
vocab = [word for word in words if nlp.vocab[word].is_alpha]

print("词汇表:", vocab)