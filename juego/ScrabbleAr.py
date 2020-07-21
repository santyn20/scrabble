import PySimpleGUI as sg
import json
from config import Configuracion
from partida import Partida
from top import Top

menu=[
        [sg.Submit('Nueva partida')],
        [sg.Button('Continuar')],
        [sg.Button('Top 10')],
        [sg.Button('Configuracion')],
        [sg.Button('Salir')]
    ]
diseño=[
        [sg.Column(menu,size=(125,175))]
        ]
ok = True
window = sg.Window('ScrabbleAr').Layout(diseño)
while ok:
  event,values=window.Read()
  if event == 'Configuracion':
    conf = Configuracion()
    dif = conf.crearMenu()
    conf.cerrarMenu()
    print(dif)
  if event == 'Nueva partida':
    ok = False
    p=Partida()
    p.CrearPartida()
  if event == 'Top 10':
    archivo= open("puntos.txt","r")
    tabla=Top()
    tabla.CrearTop(archivo)
  if event == 'Salir':
    ok = False
window.close()