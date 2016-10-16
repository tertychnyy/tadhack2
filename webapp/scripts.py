import collections
from webapp.analyze import get_words, build_dataset, get_good_from_name


def get_suggestions_by_name(name):
    name = name.lower()
    res_list = list()

    words, words_no_split = get_words(name)

    data, count, dictionary, reverse_dictionary = build_dataset(words)
    del words  # Hint to reduce memory.

    sugs = count[2:5]
    print sugs

    for sug in sugs:
        good = get_good_from_name(sug[0], words_no_split)
        res_list.append(good)

    return res_list




def get_recipe_by_name(name):
    return name


def get_discount(name):
    return 0.0


def get_count(words):
    vocabulary_size = 50000
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count = unk_count + 1
        data.append(index)
    count[0][1] = unk_count
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reverse_dictionary
