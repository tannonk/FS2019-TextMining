# usr/bin/env python3
# -*- coding: utf8 -*-

import csv

with open('train.csv', 'r', encoding='utf8') as inf, open('fasttext_train.txt', 'w', encoding='utf8') as train_out, open('fasttext_test.txt', 'w', encoding='utf8') as test_out, open('fasttext_dev.txt', 'w', encoding='utf8') as dev_out:
    reader = csv.reader(inf)
    train_writer = csv.writer(train_out, delimiter='\t')
    test_writer = csv.writer(test_out, delimiter='\t')
    dev_writer = csv.writer(dev_out, delimiter='\t')

    next(reader) # skip header
    for i, row in enumerate(reader):
        if i % 10 == 0:
            test_writer.writerow(['CLASS#'+row[2], row[1].lower()])
        elif i % 10 == 1:
            dev_writer.writerow(['CLASS#'+row[2], row[1].lower()])
        else:
            train_writer.writerow(['CLASS#'+row[2], row[1].lower()])

print('Done.')
