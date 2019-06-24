import os, csv
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Get true labels
true = []
with open('/Users/aiolf1/Desktop/tm_miniproject_fat32/G_Drive/test_tk_upsampling_replaced.tsv', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      # Get label as int
      last_char = row[1][2]
      last_int = int(last_char)
      true.append(last_int)

# Get predicted labels
pred = []
with open('/Users/aiolf1/Desktop/tm_miniproject_fat32/G_Drive/test_tk_upsampling_replaced.tsv', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      # Get label as int
      last_char = row[2][2]
      last_int = int(last_char)
      pred.append(last_int)

# Evaluation
print('***')
print(os.path.basename(tsvfile.name))
print('***')
print('Accuracy:')
print(accuracy_score(true, pred))
print()
print('Precision, Recall, f-score (binary), pos_label=0 :')
print(precision_recall_fscore_support(true, pred, pos_label=0, average='binary'))
print()
print('Precision, Recall, f-score (binary), pos_label=1 :')
print(precision_recall_fscore_support(true, pred, pos_label=1, average='binary'))
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


# Test Data
# test_true = [0,1,1,0,0,0]
# test_pred = [0,1,0,0,0,0]

# Test Evaluation
# print('Accuracy:')
# print(accuracy_score(test_true, test_pred))
# print()
# print('Precision, Recall, f-score (binary):')
# print(precision_recall_fscore_support(test_true, test_pred, pos_label=0, average='binary'))
# print()
# print('Precision, Recall, f-score (binary), pos_label=1:')
# print(precision_recall_fscore_support(test_true, test_pred, pos_label=1, average='binary'))
# print()
# print('Precision, Recall, f-score (binary):')
# print(precision_recall_fscore_support(test_true, test_pred, labels=[1]))
# print()
# print('Precision, Recall, f-score (micro):')
# print(precision_recall_fscore_support(test_true, test_pred, average='micro'))
# print()
# print('Precision, Recall, f-score (macro):')
# print(precision_recall_fscore_support(test_true, test_pred, average='macro'))
# print()
# print('Precision, Recall, f-score (weighted):')
# print(precision_recall_fscore_support(test_true, test_pred, average='weighted'))
# print()
