import operator

with open("sample.txt") as work_file:
    contents = work_file.read().lower().replace(',', '').replace('.', '').replace('?', '').replace(':', '').replace('"', '').replace('!', '').replace(';', '').replace('-', ' ').split()

word_dict = {}
for word in set(contents):
    word_dict[word] = contents.count(word)

sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

for word in sorted_word_dict[:19]:
    print(str(word).replace('(', '').replace(')', '').replace("'", "").replace(',', ''))
