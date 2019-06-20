# usr/bin/env python3
# -*- coding: utf8 -*-

# from spacy.lang.en.stop_words import STOP_WORDS
import random
from nltk.corpus import stopwords
import csv

original_train_file = '/Users/tannon/G-Drive/tm_miniproject_fat32/tokenized/train.txt'

STOP_WORDS = set(stopwords.words('english'))

def replace_stopwords(sentence):
    sentence = sentence.split()
    for tok_idx, tok in enumerate(sentence):
        if tok in STOP_WORDS:
            sentence[tok_idx] = random.sample(STOP_WORDS, 1)[0]
    return ' '.join(sentence)

def main():
    upsamples = []
    with open(original_train_file, 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter='\t')

        while len(upsamples) <= 980318-64578:
            for row in reader:
                if row[0] == '__label__1':
                    replacement = replace_stopwords(row[1])
                    if replacement:
                        upsamples.append(replacement)
            f.seek(0)

        print('sampling complete.')

        f.seek(0)

        with open('/Users/tannon/G-Drive/tm_miniproject_fat32/tokenized/train_upsampled_replaced.txt', 'w+', encoding='utf8') as outf:
            writer = csv.writer(outf, delimiter='\t')
            for row in reader:
                writer.writerow(row)
            for sample in upsamples[:980318-64578]:
                writer.writerow(['__label__1', sample])

    print('finished writing file.')

if __name__ == '__main__':
    main()
