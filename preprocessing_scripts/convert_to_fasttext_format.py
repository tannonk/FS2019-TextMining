# usr/bin/env python3
# -*- coding: utf8 -*-

import csv
import argparse
import spacy
from tqdm import tqdm

nlp = spacy.load('en')

print(type(nlp))

ap = argparse.ArgumentParser()
ap.add_argument('-i', help='original training set for splitting')
ap.add_argument('-lc', help='if given, performs simple lowercase preprocessing', action='store_true')
args = ap.parse_args()

def tokenize(s, lc=True):
    sent = nlp(s)
    if lc:
        return ' '.join([token.text.lower() for token in sent])
    else:
        return ' '.join([token.text for token in sent])

def count_lines(file):
    num_lines = sum(1 for line in open(file))
    return num_lines

lines = count_lines(args.i)

with open(args.i, 'r', encoding='utf8') as inf, open('data/train.txt', 'w', encoding='utf8') as train_out, open('data/test.txt', 'w', encoding='utf8') as test_out, open('data/valid.txt', 'w', encoding='utf8') as dev_out:
    train_writer = csv.writer(train_out, delimiter='\t')
    test_writer = csv.writer(test_out, delimiter='\t')
    dev_writer = csv.writer(dev_out, delimiter='\t')


    for i, row in enumerate(tqdm(csv.reader(inf), total=lines)):
        if i % 10 == 0:
            test_writer.writerow(['__label__'+row[2], tokenize(row[1], args.lc)])
        elif i % 10 == 1:
            dev_writer.writerow(['__label__'+row[2], tokenize(row[1], args.lc)])
        else:
            train_writer.writerow(['__label__'+row[2], tokenize(row[1], args.lc)])

print('Done.')
