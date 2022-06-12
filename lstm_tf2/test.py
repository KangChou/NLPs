import os

import matplotlib.pyplot as plt

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from  sklearn.metrics import classification_report
from main import *
y_pred = model.predict(X_validation_padded)
y_pred = y_pred.argmax(axis=1)

labels=[1,2,3,4,5,6,7,8,9,10]
conf_mat = confusion_matrix(Y_validation_cat_seq, y_pred)
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(conf_mat, annot=True, fmt='d',xticklabels=labels, yticklabels=labels)
plt.ylabel('actual results',fontsize=18)
plt.xlabel('predict result',fontsize=18)
plt.savefig('result.png')
print(dict(list(label_word_index.items())))


print('accuracy %s' % accuracy_score(y_pred, Y_validation_cat_seq))
print(classification_report(Y_validation_cat_seq, y_pred,target_names=[str(w) for w in labels]))
print(dict(list(label_word_index.items())))