import pattern.es
class Check():
  
  def buscar(self, palabra):
    encuentro = False
    if palabra in pattern.es.spelling.keys():
      encuentro = True
    else:
      return(encuentro)
    s = (pattern.es.parse(palabra)).split()
    if (encuentro == True):
      for cada in s:
        for c in cada:
          if c[1] == 'VB':
            return('VERBO')
          elif c[1] ==  "NNS" or c[1] ==  "NN":
            return('SUSTANTIVO')
          elif c[1] ==  "JJ":
            return('ADJETIVO')
          else:
            return('OTRO')
