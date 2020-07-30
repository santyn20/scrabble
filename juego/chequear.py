import pattern.es
class Check():


  def __init__(self):
    self._posIni = (0,0)
    self._posAct = (0,0)
    self._derecha = False
    self._abajo = False
    self._casillas = []
    self._palabra = ''



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

  def getPalabra(self):
    return self._palabra

  def setPosIni(self,pos):
    self._posAct = pos
    self._posIni = pos


  def calcularPuntaje(self,p):
    for i in self._casillas:
      p += i.getPuntaje()
    return p


  def reiniciarPalabra(self):
    self._casillas.clear()


  def agregarLetra(self,let):
    self._casillas.append(let)


  def limpiar(self):
    for i in self._casillas:
      i.limpiarFicha()
    self.reiniciarPalabra()

  
  def buscar(self):

    self._palabra = ''
    for i in self._casillas:
      self._palabra += i.getFicha().getLetra()
    encuentro = False
    if ( (self._palabra in pattern.es.spelling.keys()) and (self._palabra != '')):
      encuentro = True
      self._derecha = False
      self._abajo = False
    return encuentro

  
