"""Anthony Tran
PSID: 1957342
ZyLab 9.10"""

import csv

import_file = input()
with open(import_file) as csv.file:
    split = csv.reader(csv.file, delimiter=',')
    word_dict = {}
    for line in split:
        for phrase in line:
            if phrase in word_dict:
                word_dict[phrase] += 1
            elif phrase not in word_dict:
                word_dict[phrase] = 1

for keys in word_dict.keys():
    print(str(keys), str(word_dict[keys]))
