#!/usr/bin/env python
# reducer.py
import sys

# maps words to their counts
word2titles = {}
word2places = {}
top = 10

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
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

word2titles2 = sorted(word2titles.items(), key=lambda x: x[1], reverse=True)
for word in word2titles2:
    print(word)
