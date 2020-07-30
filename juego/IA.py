import pattern.es
import re
from ficha import Ficha
class InteligenciaArtificial():
  def __init__(self, palabra):    
    self._lista1 = palabra
  
  def datosBuenos(self):
    listanueva = []
    for i in self._lista1:
      listanueva.append(i.getLetra())
    return listanueva
  
  def buscar(self):
    pal = []
    for x in pattern.es.lexicon.keys():
      if x in pattern.es.spelling.keys():
        regex="("+".*?".join(x) + ")"
        lista1Cadena=" ".join(self.datosBuenos())
        encontrados = re.finditer(regex, lista1Cadena, re.MULTILINE)
        cantidad=len([matchNum for matchNum, match in enumerate(encontrados, start=1)])
        if cantidad >= 1:
          pal.append(x)
    pal.sort(key = lambda s: len(s))
    return(pal.pop())

# Recibe el mismo atril que el jugador, se fija cuantas veces aparece una palabra en ese atril, y devuelve la palabra mas grande que aparece

