import PySimpleGUI as sg

class Boton():
  def __init__(self,color):
    self._color = color


  def get_boton(self):
    if self._color == 0:
      return sg.Button("",button_color=('black','white'), size=(2, 2), pad=(0, 0) )
    elif self._color == 1:
      return sg.Button("",button_color=('black','green'), size=(2, 2), pad=(0, 0) )
    elif self._color == 2:
      return sg.Button("",button_color=('black','red'), size=(2, 2), pad=(0, 0) )