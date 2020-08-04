import PySimpleGUI as sg
from pozo import Pozo
from ficha import Ficha
class Atril():

  def __init__(self,p):
    self._cant_letras = 7
    self._atril = []
    self._pozo = p
    self._cache = []
    self.cargarAtril()

  def cargarAtril(self,cant = 7):
    '''Cargo el atril con la cantidad de fichas por defecto'''
    for i in range(cant):
      f = self._pozo.getFicha()
      f.setCoor(i)
      self.agregarLetras(f)

  def agregarLetras(self, l):
    '''Agrego una ficha en particular al atril'''
      self._atril.append(l)

#INICIO GETTERS Y SETTERS

  def getLetra(self, i):
      return self._atril[i]

  def getCantLetras(self):
    return self._cant_letras

  def getCache(self):
      return self._cache

#FIN GETTERS Y SETTERS

  def mostrarAtril(self):
    '''Devuelvo el layout que se usara en la ventana principal del juego'''
    layout = []
    for i in self._atril:
      button = i.getBoton()
      layout.append(button)
    return layout

  def limpiarCache(self):
    '''Se limpia el cache'''
    self._cache.clear()

  def agregarCache(self,f):
    '''Agrego una letra en particular al cache'''
    self._cache.append(f)

  def seleccionarFicha(self,f):
    ''' Este metodo se usa cuando se quiere hacer un cambio de fichas. Marca o desmarca las fichas con un color y
        las agrega o las quita del cache'''
    for i in self._atril:
      if (i == f):
        if (i in self._cache):
          i.getBoton().Update(button_color=("black","#F1C40F"))
          self._cache.remove(f)
        else:
          self.agregarCache(f)
          i.getBoton().Update(button_color=("black","green"))

  def deseleccionarFicha(self):
    ''' Este metodo se usa cuando se quiere cancelar el cambio de fichas. 
        Remueve todas las fichas que se encontraban en el cache con el fin de ser REEMPLAZADAS'''
    for i in self._cache:
      if i in self._atril:
        i.getBoton().Update(button_color=("black","#F1C40F"))
    self.limpiarCache()

  def actualizarAtril(self,f = None,ok = False):
    ''' Metodo con el porposito principal de dar una ayuda visual al jugador.
        Agrega las fichas con las que se esta formando la palabra al cache'''
    for i in self._atril:
      if (i != f):
        i.getBoton().Update(disabled=True)
        i.getBoton().Update(button_color=("black","#B7950B"))
    if (ok):
      self._cache.append(f)
      for i in self._atril:
        if (i in self._cache):
          i.getBoton().Update(disabled=True)
          i.getBoton().Update(button_color=("black","#B7950B"))
        else: 
          i.getBoton().Update(disabled=False)
          i.getBoton().Update(button_color=("black","#F1C40F"))

  def renovarFichas(self):
    ''' Este metodo se usa cuando se quiere confirmar el cambio de fichas.
        Reemplaza las fichas seleccionadas (las que estan en el cache) con unas nuevas del pozo.'''
    if (len(self._cache) != 0):
      for i in self._cache:
        indx = self._atril.index(i)
        self._atril[indx].actualizar(self._pozo.getFicha())
      self.limpiarCache()
    for i in self._atril:
      i.getBoton().Update(disabled=False)
      i.getBoton().Update(button_color=("black","#F1C40F"))

  #DEBERIA CREAR METODO DE RENOVAR FICHAS PARA LA IA (SIN LOS UPDATE DE COLOR Y DISABLED)

  def devolverFicha(self):
    '''Metodo para cancelar la seleccion de una ficha que se queria ingresar al tablero'''
    for i in self._atril:
      if (not (i in self._cache)):
        i.getBoton().Update(disabled=False)
        i.getBoton().Update(button_color=("black","#F1C40F"))


  def getFichaByLetra(self,l):
    for i in self._atril:
      if (i.getLetra() == l):
        return i
      else:
        return None

    

      
    
