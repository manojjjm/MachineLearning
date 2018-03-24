##'''
##concept is to give up the un nesecary words  during the analysis
##
##it is used to trace the words that we will ignore
##'''



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence =  'This is an example off stop word filtration'
stop_words= set(stopwords.words('english'))
words= word_tokenize(example_sentence)
filtered_sentences= []
for w in words:
    if w not in stop_words:
        filtered_sentences.append(w)

print(filtered_sentences)

