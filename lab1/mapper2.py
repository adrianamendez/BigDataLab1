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


# In[43]:


# PREGUNTA 2
print('%s\t%s\t%s' % (json_file['thread']['site_full'], json_file['published'][5:7],1))


# In[44]:


# PREGUNTA 3
texto = json_file['text'].lower().split()
for z in range(len(texto)-1):
    print ('%s\t%s' % (texto[z] + ' ' + texto[z+1], 1))


# In[ ]:




