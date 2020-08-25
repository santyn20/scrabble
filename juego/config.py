import PySimpleGUI as sg
from configFichas import ConfigFichas
class Configuracion():
  def __init__(self):
    self._nivel='Normal'

  def crearMenu(self):
    ok = True
    diseño = [
      [sg.Text('Configuracion')],
      [sg.Column([
      [sg.Text('Dificultad:'), sg.Listbox(values=('Facil','Normal','Dificil'),size=(8,3), enable_events=True, key = 'dif')],
      [sg.Text('Facil: Se tomara en cuenta cualquier palabra')],
      [sg.Text('Normal y dificil: Solo se tomaran en cuenta adjetivos y verbos')]
    ])],
      [sg.Button('Guardar'), sg.Button('Cancelar'), sg.Button("Configurar Fichas")]
    ]
    window = sg.Window('Configuracion').Layout(diseño)
    self._nivel='Normal'

    while ok:
      event, values = window.Read()
      if (event == "Configurar Fichas"):
        cfg = ConfigFichas()
        cfg.main()
      if (event == 'Guardar'):
        ok = False
        if (len(values['dif']) > 0):
          self._nivel=values['dif'][0]
      if (event == sg.WIN_CLOSED):
        ok = False
    window.close()
    
  def cerrarMenu(self):
    self._window.close()

  def Nivel(self):
    return self._nivel