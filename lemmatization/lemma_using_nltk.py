import nltk
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Example Test
sentence = "The striped bats are hanging on their feet for best"

# Tokenize: Split the sentence into words
word_list = nltk.word_tokenize(sentence)
print(word_list)
# ['The', 'striped', 'bats', 'are', 'hanging', 'on', 'their', 'feet', 'for', 'best']

# Lemmatize list of words and join
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
print(lemmatized_output)
# The striped bat are hanging on their foot for best


# print(lemmatizer.lemmatize("Running", pos='n'))
# print(lemmatizer.lemmatize("Studies"))
# print(lemmatizer.lemmatize("communities"))
#
# print(lemmatizer.lemmatize("feet", pos='n'))
