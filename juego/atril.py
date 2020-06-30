import PySimpleGUI as sg
class Atril():

  def __init__(self):
    self._cant_letras = 7
    self._atril = []

  def agregarLetras(self, l):
      self._atril.append(l)

  def get_let(self, i):
      return self._atril[i]

  def getCantLetras(self):
    return self._cant_letras

  def mostrarAtril(self, a):
    layout = []
    row = []
    for i in range(self._cant_letras):
      button = sg.Button(a.get_let(i), size=(2, 2), pad=(0, 0) )
      row.append(button)
    return row
