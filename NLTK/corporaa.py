from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

samples= gutenberg.raw('bible-kjv.txt')

tok= sent_tokenize(samples)
print(tok[5:15])

s
