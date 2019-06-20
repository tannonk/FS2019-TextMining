# usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import csv

file = sys.argv[1]

with open(file, 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter='\t')

    uniq = set()

    c = 0

    for row in reader:
        try:
            x = hash(row[1])
            if x not in uniq:
                uniq.add(x)
                c += 1
        except IndexError:
            pass

    print(c)
