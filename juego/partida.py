import PySimpleGUI as sg
import layout1 as ly1
import layout2 as ly2
import layout3 as ly3
class Partida():
  def CrearPartida(self,conf):
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
    ok = True
    while ok:
      event,values=window.read()
      if event=='Tablero 1':
        nom = values[0]
        ok = False
        ly1.main(conf,nom)
      if event=='Tablero 2':
        ok = False
        ly2.main(conf)
      if event=='Tablero 3':
        ok = False
        ly3.main(conf)
    window.close()
