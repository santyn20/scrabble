import PySimpleGUI as sg
from pozo import Pozo
from ficha import Ficha
class Atril():

  def __init__(self):
    self._cant_letras = 7
    self._atril = []
    self._pozo = Pozo()
    self._cache = []

    self.cargarAtril()

  def cargarAtril(self,cant = 7):
    for i in range(cant):
      f = self._pozo.getFicha()
      f.setCoor(i)
      self.agregarLetras(f)

  def agregarLetras(self, l):
      self._atril.append(l)

  def getLetra(self, i):
      return self._atril[i]

  def getCantLetras(self):
    return self._cant_letras

  def mostrarAtril(self):
    layout = []
    for i in self._atril:
      button = i.getBoton()
      layout.append(button)
    return layout

  def limpiarCache(self):
    self._cache.clear()

  def actualizarAtril(self,f = None,ok = False):
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
    if (len(self._cache) != 0):
      for i in self._cache:
        indx = self._atril.index(i)
        self._atril[indx].actualizar(self._pozo.getFicha())
      self.limpiarCache()
    for i in self._atril:
      i.getBoton().Update(disabled=False)
      i.getBoton().Update(button_color=("black","#F1C40F"))


  def devolverFicha(self):
    for i in self._atril:
      if (not (i in self._cache)):
        i.getBoton().Update(disabled=False)
        i.getBoton().Update(button_color=("black","#F1C40F"))

    

      
    
