import PySimpleGUI as sg
from tablero1 import Tablero1
from tablero2 import Tablero2
from tablero3 import Tablero3
class Partida():
  def CrearPartida(self):
    interfaz=[
      [sg.Text('Apodo/Nombre')],
      [sg.InputText(size=(15,1))],
      [sg.Button('Tablero 1')],
      [sg.Button('Tablero 2')],
      [sg.Button('Tablero 3')],
      [sg.Text('Casilla verde: Aumenta un 50% el puntaje de la ficha')],
      [sg.Text('Casilla roja: Disminuye un 50% el puntaje de la ficha')],
      [sg.Text('Casilla blanca: neutra')],
      [sg.Button('Volver')]
    ]
    window=sg.Window('Partida',interfaz)
    while True:
      event,values=window.read()
      if event=='Tablero 1':
        window.close()
        tab=Tablero1()
        tab.crearTablero()
      if event=='Tablero 2':
        window.close()
        tab=Tablero2()
        tab.crearTablero()
      if event=='Tablero 3':
        window.close()
        tab=Tablero3()
        tab.crearTablero()
