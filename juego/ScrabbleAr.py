import PySimpleGUI as sg
import json
from config import Configuracion
from partida import Partida
from top import Top
sg.theme('Dark Brown')
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
conf = Configuracion()
while ok:
  event,values=window.Read()
  if event == 'Configuracion':
    conf.crearMenu()
  if event == 'Nueva partida':
    p=Partida()
    p.CrearPartida(conf)
  if event == 'Top 10':
    archivo= open("datos_juego.json","r")
    tabla=Top()
    tabla.CrearTop(archivo)
  if event == 'Salir':
    ok = False
  if (event == sg.WIN_CLOSED):
    ok = False
window.close()