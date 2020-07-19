import PySimpleGUI as sg
from boton import Boton
from atril import Atril
from pozo import Pozo
from chequear import Check
import sys
class Tablero3():

  
  def __init__(self):
    self.matriz=[[1,0,0,2,0,0,0,0,0,0,0,1,0,0,2],
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



  def crearTablero(self):
    layout = []
    for i in range(15):
      row = []
      for j in range(15):
        button = Boton(self.matriz[i][j]).get_boton(i,j)
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
        if event == sg.WIN_CLOSED or event == 'Cerrar':
          break
        elif event == "Check":
          c = Check()
          buscado = c.buscar("".join(pal))
          print(buscado) 
          pal.clear()
        elif (not(event is tuple)):
          letra = event
          window.Element(event).Update('')
        elif ((event is tuple) and (letra != '')): #and (valor[event]==False) ):
          print(valor)
          window[event].Update(Text = letra)
          cont = cont + 1
          pal.append(letra)
          num = event
          valor[event]=True
          letra=""
      except AttributeError as e:
        raise e
        #sys.exit()
      except KeyError:
        window[event].Update(Text = letra)
        pal.append(letra)
        num = event
        valor[event]=True
        letra=""
    window.close()
