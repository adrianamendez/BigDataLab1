#!/usr/bin/env python
# mapper.py
import sys
from bs4 import BeautifulSoup,SoupStrainer

soup = BeautifulSoup(sys.stdin, features="lxml")
title = soup.findAll('title')
places = soup.findAll('places')
topics = soup.findAll('topics')

for wordtitle in title:
    title_final = str(wordtitle.string)
    title_final = title_final.split()

    for wordtitlefinal in title_final:
        print('%s\t%s' % (wordtitlefinal, "1"))

for wordplaces in places:
    places_final = str(wordplaces.string)
    places_final = places_final.split()

    for wordplacesfinal in places_final:
        print('%s\t%s' % (wordplacesfinal, "1"))

for wordtopics in topics:
    topics_final = str(wordtopics.string)
    topics_final = topics_final.split()

    for wordtopicsfinal in topics_final:
        print('%s\t%s' % (wordtopicsfinal, "1"))

