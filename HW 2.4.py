user_words = input('Введите слова, через пробел: ')
words = user_words.split()
for i, word, in enumerate(words, 1):
    print(i, word[:10])



