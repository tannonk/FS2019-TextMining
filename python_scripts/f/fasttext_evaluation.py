import os, csv
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Get true labels
true = []
with open('/Users/aiolf1/Desktop/tm_miniproject_fat32/fasttext/tokenized/test_labels.txt', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      # Get label as int
      last_char = row[0][-1]
      last_int = int(last_char)
      true.append(last_int)

# Get predicted labels
pred = []
with open('/Users/aiolf1/Desktop/tm_miniproject_fat32/fasttext/train_downsampled.predictions.txt', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter=' ')
  for row in reader:
      # Get label as int
      last_char = row[0][-1]
      last_int = int(last_char)
      pred.append(last_int)

# pred is too long
pred.remove(pred[0])
pred.remove(pred[0])

# Evaluation
print('***')
print(os.path.basename(tsvfile.name))
print('***')
print('Accuracy:')
print(accuracy_score(true, pred))
print()
print('Precision, Recall, f-score (binary):')
print(precision_recall_fscore_support(true, pred, pos_label=0, average='binary'))
print()
print('Precision, Recall, f-score (micro):')
print(precision_recall_fscore_support(true, pred, average='micro'))
print()
print('Precision, Recall, f-score (macro):')
print(precision_recall_fscore_support(true, pred, average='macro'))
print()
print('Precision, Recall, f-score (weighted):')
print(precision_recall_fscore_support(true, pred, average='weighted'))
print()
