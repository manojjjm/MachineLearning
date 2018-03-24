#porter stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps= PorterStemmer()

example_words=['pythoner','python','pythoning','pythoned','pythonly']
##for  w in example_words:
##    print(ps.stem(w))

new_text ='Itis very important to be pythonly while you are pythonning with python . All pythoner have pythoned once'

words= word_tokenize(new_text)
for  w in words:
    print(ps.stem(w))
