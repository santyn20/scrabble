import pattern.es
class Check():


  def __init__(self):
    self._posIni = (0,0)
    self._posAct = (0,0)
    self._derecha = False
    self._abajo = False
    self._casillas = []



  def checkLugar(self,pos):

    if (self._posIni == (0,0)):
      return True

    if (self._derecha):
      if ( (pos[1] - self._posAct[1] == 1) and (pos[0] == self._posAct[0]) ):
        self._posAct = pos
        return self._derecha
      else:
        return False


    if (self._abajo):
      if ( (pos[0] - self._posAct[0] == 1) and (pos[1] == self._posAct[1]) ):
        self._posAct = pos
        return self._abajo
      else:
        return False


    if ( (pos[0] - self._posAct[0] == 1) and (pos[1] == self._posAct[1]) ):
      self._posAct = pos
      self._abajo = True
      return self._abajo
    if ( (pos[1] - self._posAct[1] == 1) and (pos[0] == self._posAct[0]) ):
      self._posAct = pos
      self._derecha = True
      return self._derecha
    else:
      return False

  def getPosIni(self):
    return self._posIni

  def setPosIni(self,pos):
    self._posAct = pos
    self._posIni = pos



  def agregarLetra(self,let):
    self._casillas.append(let)


  
  def buscar(self):

    palabra = ''
    for i in self._casillas:
      palabra += i.getFicha().getLetra()

    encuentro = False
    if ( (palabra in pattern.es.spelling.keys()) and (palabra != '')):
      encuentro = True
    return encuentro

  
