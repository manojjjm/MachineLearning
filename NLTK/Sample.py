import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
example_text="Hello  Mr. smith there, how are you doing today ? the weather is good and pythonn is great . sky is  pinkish blue. you shouldnot eat cardboard."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))


for i in (word_tokenize(example_text)):
    print(i)



