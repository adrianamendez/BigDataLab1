#!/usr/bin/env python
# reducer.py
import sys

# maps words to their counts

word2titles = {}
word2places = {}
word2OptionA = {}
word2OptionB = {}
word2OptionC = {}
counterA = 0
counterB = 0
counterC = 0
top = 9

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
    menu = word[0].split()
    final_word = str(menu[1]) + " " + str(word[1])

    if menu[0] == "A":
        if counterA <= top:
            word2OptionA[counterA] = final_word
            counterA += 1
    if menu[0] == "B":
        word2OptionB[counterB] = final_word
        counterB += 1
    if menu[0] == "C":
        word2OptionC[counterC] = final_word
        counterC += 1

print("Encuentre las 10 palabras más frecuentes que aparecen en los títulos de las noticias que hay en el dataset ")
for word in word2OptionA.values():
    print(word)

print("Indique cuáles son los países donde se reportan las noticias y cuántas veces aparece cada uno en el dataset. ")
for word in word2OptionB.values():
    print(word)

print("Indique cuántas noticias se publican en cada tema que aparece en el dataset. ")
for word in word2OptionC.values():
    print(word)
