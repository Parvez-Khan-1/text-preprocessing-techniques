from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def get_stop_words():
    return set(stopwords.words('english'))


def add_custom_stop_words(custom_stop_words, standard_stop_words):
    standard_stop_words.update(set(custom_stop_words))
    return standard_stop_words


def tokenize_sentence(sentence):
    return word_tokenize(sentence)


def remove_stop_words(token_list, stop_word_list):
    filter = lambda x: [word for word in token_list if word not in stop_word_list]
    return filter(token_list)


def convert_list_to_string(word_tokens):
    return ' '.join(word_tokens)


def version_1():
    sentence = "Computers are like old testaments gods, lots of rule and no mercy!!"

    stop_words_list = get_stop_words()

    sentence_tokens = tokenize_sentence(sentence)

    filtered_tokens = remove_stop_words(sentence_tokens, stop_word_list=stop_words_list)

    filtered_sentence = convert_list_to_string(filtered_tokens)

    print("Sentence With Stop Words : {}".format(sentence))
    print("Filtered Sentence : {} ".format(filtered_sentence))


def version_2():
    # We can add custom or domain specific stop words as well. For example we want to add '!' to stopwords
    sentence = "Computers are like old testaments gods, lots of rule and no mercy!!"

    stop_words_list = get_stop_words()

    # Add Custom Stop Words
    stop_words_list = add_custom_stop_words(['!', '.'], stop_words_list)

    sentence_tokens = tokenize_sentence(sentence)

    filtered_tokens = remove_stop_words(sentence_tokens, stop_word_list=stop_words_list)

    filtered_sentence = convert_list_to_string(filtered_tokens)

    print("Sentence With Stop Words : {}".format(sentence))
    print("Filtered Sentence : {} ".format(filtered_sentence))


if __name__ == '__main__':
    version_1()
    # version_2()
