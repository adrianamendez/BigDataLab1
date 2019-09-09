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


def mapperp1(document):

    f = open("demofile2.txt", "w")
    f.write("Now the file has more content!")

    for line in list(document):
        # --- remove leading and trailing whitespace---
        line = line.strip()

        if "<TITLE>" in line:
            # --- split the line into words ---
            words = line.split()

            # --- output tuples [word, 1] in tab-delimited format---
            for word in words:
                print(('%s\t%s' % (word, "1")), file=f)

        if "<PLACES>" in line:
            # --- split the line into words ---
            words = line.split()

            # --- output tuples [word, 1] in tab-delimited format---
            for word in words:
                print(('%s\t%s' % (word, "1")), file=f)

        if "<TOPICS>" in line:
            # --- split the line into words ---
            words = line.split()

            # --- output tuples [word, 1] in tab-delimited format---
            for word in words:
                print(('%s\t%s' % (word, "1")), file=f)

    f.close()


def reducerp1():
    word2titles = {}
    word2places = {}
    top = 10
    document = open("demofile2.txt", "r")
    for line in list(document):
        line = line.strip()

        # parse the input we got from mapper.py
        word_titles, count_titles = line.split('\t', 1)
        word_places, count_places = line.split('\t', 1)
        # convert count (currently a string) to int
        try:
            count_titles = int(count_titles)
            count_places = int(count_places)
        except ValueError:
            continue

        try:
            word2titles[word_titles] = word2titles[word_titles] + count_titles
            word2places[word_places] = word2places[word_places] + count_places
        except:
            word2titles[word_titles] = count_titles
            word2places[word_places] = count_places

        # write the tuples to stdout
        # Note: they are unsorted

    for word_titless in word2titles.keys():
        print('%s\t%s' % (word_titless, word2titles[word_titless]))

    for word_placess in word2places.keys():
        print('%s\t%s' % (word_placess, word2places[word_placess]))

    document.close()

for file in glob.glob("/Users/evergarden/Documents/PyProyects/Lab1/Reuters/*.sgm"):
    print(file)
    currentDirectory = pathlib.Path(file)
    document_text = open(currentDirectory, 'r')
    mapperp1(document_text)
    reducerp1()
