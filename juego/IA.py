import pattern.es

    
lista1 = ['r','t','c','d','h','p','o','t','r','l','a','l','a']
palabra = ''

import re
for x in pattern.es.lexicon.keys():
  if x in pattern.es.spelling.keys():
    regex="("+".*?".join(x) + ")"

    lista1Cadena=" ".join(lista1)

    encontrados = re.finditer(regex, lista1Cadena, re.MULTILINE)
    cantidad=len([matchNum for matchNum, match in enumerate(encontrados, start=1)])

    print("Se encontraron {} palabra(s) {} en la lista".format(cantidad,x))

# Aun no hace nada relacionado al juego, solo busca la cantidad de veces que aparece palabras de pattern en una lista de caracteres
