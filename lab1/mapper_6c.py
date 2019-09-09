import sys, json

palabras = str(input('Ingrese las dos palabras separadas por un espacio:  ')).split()

for line in sys.stdin:
    json_text = json.loads(line)

    if (palabras[0] in json_file['text']) and (palabras[0] in json_file['text']):

        print ('%s\t%s' % (json_file['title'], 'Palabras presentes'))
