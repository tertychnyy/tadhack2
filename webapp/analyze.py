import collections
from webapp.core import tickets


vocabulary_size = 50000


def get_words(word):
    words = list()
    words_no_split = list()

    for ticket in tickets:
        save = False
        for item in ticket:
            try:
                if word in item["desc"].lower():
                    save = True
            except:
                pass
        if save:
            for item in ticket:
                try:
                    words += item["desc"].lower().split()
                    words_no_split.append(item["desc"].lower())
                except:
                    pass
    return words, words_no_split


def build_dataset(words):
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


def get_good_from_name(name, dictionary):
    d = dict()

    for item in dictionary:
        if name in item:
            if item in d.keys():
                d[item] += 1
            else:
                d[item] = 1

    ret_name = None
    ret_count = 0
    for item in d.keys():
        if d[item] > ret_count:
            ret_name = item
            ret_count = d[item]

    return ret_name.title()


