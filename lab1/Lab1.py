import glob

import pathlib

path = pathlib.Path('Reuters/')


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return len(counts)


for file in glob.glob("/Users/evergarden/Documents/PyProyects/Lab1/Reuters/*.sgm"):
    print(file)
    currentDirectory = pathlib.Path(file)
    document_text = open(currentDirectory, 'r')
    text_string = document_text.read().lower()
    text_string = text_string.decode('unicode_escape').encode('utf-8')
    total = word_count(text_string)
    print(total)