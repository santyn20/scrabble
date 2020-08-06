import PySimpleGUI as sg
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from pozo import Pozo
from chequear import Check
import sys
class Tablero3():

  
  def __init__(self):
    self._matriz=[[1,0,0,2,0,0,0,0,0,0,0,1,0,0,2],
                 [0,1,0,0,0,2,0,0,0,1,0,0,0,2,0],
                 [0,0,1,0,0,0,2,0,1,0,0,0,2,0,0],
                 [2,0,0,1,0,0,0,0,0,0,0,2,0,0,1],
                 [0,0,0,0,1,0,0,0,0,0,2,0,0,0,0],
                 [0,2,0,0,0,1,0,0,0,2,0,0,0,1,0],
                 [0,0,2,0,0,0,1,0,2,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,1,0,0,0,2,0,1,0,0,0,2,0,0],
                 [0,1,0,0,0,2,0,0,0,1,0,0,0,2,0],
                 [0,0,0,0,2,0,0,0,0,0,1,0,0,0,0],
                 [1,0,0,2,0,0,0,0,0,0,0,1,0,0,2],
                 [0,0,2,0,0,0,1,0,2,0,0,0,1,0,0],
                 [0,2,0,0,0,1,0,0,0,2,0,0,0,1,0],
                 [2,0,0,1,0,0,0,0,0,0,0,2,0,0,1]
    ]
    self._botones = []



  def crearTablero(self):
    layout = []
    x = 0
    y = 0
    for i in self._matriz:
      x += 1
      y = 0
      row = []
      for j in i:
        y += 1
        coor = (x,y)
        if (j == 0):
          bot = Boton0(coor)
        elif (j == 1):
          bot = Boton1(coor)
        elif (j == 2):
          bot = Boton2(coor)
        self._botones.append(bot)
        button = bot.getBoton()
        row.append(button)
      layout.append(row)
      
    return layout

  def getBotones(self):
    return self._botones

  def getBotonByPos(self,pos):
    for i in self._botones:
      if (i.getCoor() == pos):
        return i
    return (0,0)