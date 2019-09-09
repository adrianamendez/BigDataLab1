word2titles = {}

top = 10

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    word_titles, count_titles = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count_titles = int(count_titles)

    except ValueError:
        continue

    try:
        word2titles[word_titles] = word2titles[word_titles] + count_titles
     
    except:
        word2titles[word_titles] = count_titles
        

    # write the tuples to stdout
    # Note: they are unsorted

word2titles2 = sorted(word2titles.items(), key=lambda x: x[1], reverse=True).items()[0:top]

for word in word2titles2:
    print(word)
