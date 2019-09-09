import sys


country_month = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word_site, month, count_months = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count_months = int(count_months)
    except ValueError:
        continue

    try:
        country_month[word_site][month] = country_month[word_site][month] + count_months
    except:
        country_month[word_site][month] = count_months

    # write the tuples to stdout
    # Note: they are unsorted



for word in country_month :
    print(word)
