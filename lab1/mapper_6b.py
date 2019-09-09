import sys, json


for line in sys.stdin:
    json_text = json.loads(line)
    
    print('%s\t%s\t%s' % (json_file['thread']['site_full'], json_file['published'][0:7],"1"))
