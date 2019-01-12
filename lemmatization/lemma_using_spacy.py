from spacy.lemmatizer import Lemmatizer
import spacy

# make sure your downloaded the english model with "python -m spacy download en"
nlp = spacy.load('en')

doc = nlp(u"Apples and oranges are communities favorite fruits")

for token in doc:
    print(token, token.lemma, token.lemma_)