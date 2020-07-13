import PySimpleGUI as sg
from boton import Boton
from atril import Atril
from pozo import Pozo
from chequear import Check
import sys
class Tablero1():
  def __init__(self):
    self.matriz=[[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                 [0,0,2,0,0,0,1,0,1,0,0,0,2,0,0],
                 [0,2,0,0,0,1,0,0,0,1,0,0,0,2,0],
                 [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
                 [0,0,0,1,0,0,2,0,2,0,0,1,0,0,0],
                 [0,0,1,0,0,1,0,0,0,1,0,0,1,0,0],
                 [0,1,0,0,2,0,0,2,0,0,2,0,0,1,0],
                 [1,0,0,1,0,0,2,0,2,0,0,1,0,0,1],
                 [0,1,0,0,2,0,0,2,0,0,2,0,0,1,0],
                 [0,0,1,0,0,1,0,0,0,1,0,0,1,0,0],
                 [0,0,0,1,0,0,2,0,2,0,0,1,0,0,0],
                 [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
                 [0,2,0,0,0,1,0,0,0,1,0,0,0,2,0],
                 [0,0,2,0,0,0,1,0,1,0,0,0,2,0,0],
                 [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    ]
  def crearTablero(self):
    layout = []
    for i in self.matriz:
      row = []
      for j in i:
        button = Boton(j).get_boton()
        row.append(button)
      layout.append(row)
    pozo = Pozo()
    atril = Atril()

    for i in range(atril.getCantLetras()):
      atril.agregarLetras(pozo.getFicha()[0])

    layout.append(atril.mostrarAtril(atril))
    layout.append([sg.Button("Check"), sg.Button("Cerrar")])
    window = sg.Window('Tablero', layout)
    letra = ''
    pal=[]
    valor={}
    cont = 0
    sg.popup('La primer letra se debe ubicar en el centro del tablero')
    while True:
      event,values = window.Read()
      try:
        if event == "Cerrar":
          break
        elif event == "Check":
          c = Check()
          buscado = c.buscar("".join(pal))
          print(buscado) 
          pal.clear()
        elif event.isalpha():
          letra = event
          window.Element(event).Update('')
        elif ((event.isalpha() == False) and (letra != '') and (valor[event]==False) ):
          window.Element(event).Update(letra)
          cont = cont + 1
          pal.append(letra)
          num = event
          valor[event]=True
          letra=""
      except AttributeError:
        sys.exit()
      except KeyError:
        window.Element(event).Update(letra)
        pal.append(letra)
        num = event
        valor[event]=True
        letra=""
    window.close()


    
