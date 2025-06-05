import random
import nltk
from nltk.corpus import brown

nltk.download('brown')


def frequent_words_generator(n):
    if not (1 <= n <= 10000):
        raise ValueError("n must be between 1 and 10_000")

    words = [w.lower() for w in brown.words() if w.isalpha()]
    unique_words = list(set(words))

    sampled_words = random.sample(unique_words, n)
    for i in sampled_words:
        yield i


for word in frequent_words_generator(1000):
    print(word)