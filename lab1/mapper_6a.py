#!/usr/bin/env python
# coding: utf-8

# In[42]:


#!/usr/bin/env python
"""mapper2.py"""

import sys, json

# input comes from STDIN (standard input)

 

for line in sys.stdin:
    json_text = json.loads(line)
    
    b = "!@#$<>/&.;,"
    for char in b:
        json_text['title'] = json_text['title'].replace(char,"")

    for word in json_text['title'].lower().split():
        print ('%s\t%s' % (word, "1"))



