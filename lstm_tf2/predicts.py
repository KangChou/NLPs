import os
import matplotlib.pyplot as plt
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from  sklearn.metrics import classification_report

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


from datasets import output_datasets
X_train, X_validation, Y_train, Y_validation,dfs=output_datasets()

vocab_size = 5000
embedding_dim = 64
max_length = 150
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<OOV>'


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),
    tf.keras.layers.Dense(embedding_dim, activation='relu'),
    tf.keras.layers.Dense(11, activation='softmax')
])

# model.load("my_model")
model.load_weights("my_model")
print(model)


tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(X_train.cut_review.values)

X_validation_sequences = tokenizer.texts_to_sequences(X_validation.cut_review.values)
X_validation_padded = pad_sequences(X_validation_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

y_pred = model.predict(X_validation_padded)
y_pred = y_pred.argmax(axis=1)

label_tokenizer = Tokenizer()
label_tokenizer.fit_on_texts(dfs.cat.values)

Y_validation_cat_seq = np.array(label_tokenizer.texts_to_sequences(Y_validation.cat.values))
label_word_index = label_tokenizer.word_index

labels=[1,2,3,4,5,6,7,8,9,10]
conf_mat = confusion_matrix(Y_validation_cat_seq, y_pred)
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(conf_mat, annot=True, fmt='d',xticklabels=labels, yticklabels=labels)
plt.ylabel('actual results',fontsize=18)
plt.xlabel('predict result',fontsize=18)
plt.savefig('result2.png')


print(dict(list(label_word_index.items())))
print('accuracy %s' % accuracy_score(y_pred, Y_validation_cat_seq))
print(classification_report(Y_validation_cat_seq, y_pred,target_names=[str(w) for w in labels]))
print(dict(list(label_word_index.items())))