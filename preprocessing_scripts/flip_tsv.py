# usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import csv

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r', encoding='utf8') as inf, open(outfile, 'w+', encoding='utf8') as outf:
    reader = csv.reader(inf, delimiter='\t')
    writer = csv.writer(outf, delimiter='\t')
    for row in reader:
        writer.writerow([row[1], row[0]])
