import streamlit as st
import matplotlib.pyplot as plt

import tensorflow as tf
import pandas as pd
import os

data = pd.read_csv('../data/titles.csv')
titles = data['title'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
word_count = len(tokenizer.word_index) + 1

x = []
y = []

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    for i in range(1, len(sequence)):
        x.append(sequence[:i])
        y.append(sequence[i])

max_len = max(len(i) for i in x)
x = tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=max_len, padding='pre')
y = tf.keras.utils.to_categorical(y, num_classes=len(tokenizer.word_index) + 1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(word_count, 10),
    tf.keras.layers.SimpleRNN(32),
    tf.keras.layers.Dense(word_count),
    tf.keras.layers.Softmax()
])

loss = tf.keras.losses.CategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
history = model.fit(x, y, epochs=100)

fig = plt.figure()
cnt = 1
for k, v in history.history.items():
    ax = fig.add_subplot(len(history.history), 1, cnt)
    ax.title.set_text(k)
    ax.plot(v)
    cnt += 1

st.pyplot(fig)