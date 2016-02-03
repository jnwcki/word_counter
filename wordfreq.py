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

    for word in sorted_word_dict[:19]:
        print(str(word).replace('(', '').replace(')', '').replace("'", "").replace(',', ''))
word_freq()