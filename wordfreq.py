import operator
from sys import argv

def word_freq():

    word_dict = {}

    with open(argv[1]) as work_file:
        contents = work_file.read().lower().replace(',', '').replace('.', '').replace('?', '').replace(':', '').replace('"', '').replace('!', '').replace(';', '').replace('-', ' ').split()

    with open("ignored_words") as ignored_words:
        blocklist = ignored_words.read().replace('\n', ',').split(',')

    clean_word_list = [x for x in contents if x not in blocklist]

    for word in contents:
        word_dict[word] = clean_word_list.count(word)

    sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    high_num = [item[1] for item in sorted_word_dict]

    if high_num[0] > 50:
        hist_ratio = 50 / high_num[0]
    else:
        hist_ratio = 1

    for w in sorted_word_dict[:20]:
        if len(w[0]) < 10:
            print(w[0] + "\t\t", "#" * int(w[1] * hist_ratio))
        else:
            print(w[0] + "\t", "#" * int(w[1] * hist_ratio))


word_freq()