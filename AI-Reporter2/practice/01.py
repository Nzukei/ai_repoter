import tensorflow as tf

sentences = [
    'I love my dog',
    'I love my cat'
]

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)