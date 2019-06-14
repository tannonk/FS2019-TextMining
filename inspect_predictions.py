# usr/bin/env python3
# -*- coding: utf8 -*-

import csv
import sys

pred_file = sys.argv[1]

c = 0
n = 0

with open(pred_file, 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter='\t')
    for sent, label, pred in reader:
        n += 1
        # print(sent, label, pred)
        # print()
        if int(label[-1]) == int(pred[1]):
            c += 1

print(f'{c} out of {n} matches')
