from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("Cats"))
print(lemmatizer.lemmatize("Cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("rocked"))
print(lemmatizer.lemmatize("python"))

