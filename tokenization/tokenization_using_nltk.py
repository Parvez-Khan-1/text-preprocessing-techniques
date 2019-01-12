from nltk.tokenize import word_tokenize, sent_tokenize

text = "I am learning Machine Learning. I want to utilize AI techniques to make human " \
       "life more easie, and comfortable"

print(sent_tokenize(text))
print(word_tokenize(text))
