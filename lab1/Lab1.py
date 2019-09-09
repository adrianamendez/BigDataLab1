import glob

import pathlib
from bs4 import BeautifulSoup,SoupStrainer

path = pathlib.Path('Reuters/')

def mapperp1(document):

    f = open("demofile2.txt", "w")

    soup = BeautifulSoup(document,features="lxml")
    title = soup.findAll('title')
    places = soup.findAll('places')
    topics = soup.findAll('topics')

    for wordtitle in title:
        title_final = str(wordtitle.string)
        title_final = title_final.split()

        for wordtitlefinal in title_final:
            print(('%s\t%s' % (wordtitlefinal, "1")), file=f)

    for wordplaces in places:
        places_final = str(wordplaces.string)

        places_final = places_final.split()

        for wordplacesfinal in places_final:
            print(('%s\t%s' % (wordplacesfinal, "1")), file=f)

    for wordtopics in topics:
        topics_final = str(wordtopics.string)
        topics_final = topics_final.split()

        for wordtopicsfinal in topics_final:
            print(('%s\t%s' % (wordtopicsfinal,"1")), file=f)




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

    word2titles2 = sorted(word2titles.items(), key=lambda x: x[1], reverse=True)
    for word in word2titles2:
        print(word)



    document.close()

for file in glob.glob("/Users/evergarden/Documents/PyProyects/Lab1/Reuters/*.sgm"):
    currentDirectory = pathlib.Path(file)
    document_text = open(currentDirectory, 'r')
    mapperp1(document_text)
    reducerp1()
