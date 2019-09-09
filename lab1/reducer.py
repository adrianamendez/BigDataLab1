#!/usr/bin/env python
# reducer.py
import sys

# maps words to their counts
word2titles = {}
word2places = {}

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

for word_titless in word2titles.keys():

    print('%s\t%s' % (word_titless, word2titles[word_titless]))

for word_placess in word2places.keys():

    print('%s\t%s' % (word_placess, word2places[word_placess]))
