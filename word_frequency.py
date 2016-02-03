import operator
import reprlib

with open("sample.txt") as work_file:
    contents = work_file.read().lower().replace(',', '').replace('.', '').replace('?', '').replace(':', '').replace('"', '').replace('!', '').replace(';', '').replace('-', ' ').split()

#print(contents)

word_dict = {}
for word in set(contents):
    word_dict[word] = contents.count(word)
#print(word_dict)
#print(word_dict, sorted(word_dict.values()))
sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse = True)
#r = reprlib.repr()
#r.maxdict = 20
#for sorted_word in sorted_word_dict:
#    print(r.repr(sorted_word))
for word in sorted_word_dict[:19]:
    print(str(word).replace('(', '').replace(')', '').replace("'", "").replace(',', ''))
    