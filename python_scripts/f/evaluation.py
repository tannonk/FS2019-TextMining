import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support #average_precision_score

# Accuracy
a_y_pred = [0, 1, 1, 0]
a_y_true = [0, 1, 0, 0]
print('Accuracy:')
print(accuracy_score(a_y_true, a_y_pred))
print()

# Precision, Recall, f-score
y_pred = np.array([0, 1, 1, 0])
y_true = np.array([0, 1, 0, 0])
print('Precision, Recall, f-score:')
print(precision_recall_fscore_support(y_true, y_pred, average='binary'))
print()
