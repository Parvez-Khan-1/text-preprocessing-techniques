import spacy

# Need to install spacy english model as >> python -m spacy download en
spacy_model = spacy.load('en')


def get_stop_words():
    return spacy_model.Defaults.stop_words


def add_custom_stop_words(custom_stop_words):
    # To single stop word ===> spacy_model.Defaults.stop_words.add("abc")

    # To add multiple stop words at a time
    spacy_model.Defaults.stop_words |= set(custom_stop_words)


def remove_stop_word(stop_word_to_remove):
    # To remove single stop word ==> spacy_model.Defaults.stop_words.remove("whatever")

    # To remove multiple stop words at a time
    spacy_model.Defaults.stop_words.remove(stop_word_to_remove)


def tokenize_sentence(sentence):
    doc = spacy_model(sentence)
    return [str(token) for token in doc]


def remove_stop_words(word_tokens, stop_words):
    filter = lambda x: [word for word in word_tokens if word not in stop_words]
    return filter(word_tokens)


def convert_list_to_string(word_tokens):
    return ' '.join(word_tokens)


if __name__ == '__main__':
    sentence = "He like to eat cake and chochlate of a starwberry flavour!!"
    word_tokens = tokenize_sentence(sentence)

    add_custom_stop_words(['!'])
    stop_words = get_stop_words()

    filtered_tokens = remove_stop_words(word_tokens, stop_words)
    filtered_sentence = convert_list_to_string(filtered_tokens)

    print("Original Sentence : ", sentence)
    print("Filtered Sentence : ", filtered_sentence)