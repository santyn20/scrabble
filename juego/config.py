import PySimpleGUI as sg
class Configuracion():
  def __init__(self):
    diseño = [
      [sg.Text('Configuracion')],
      [sg.Column([
      [sg.Text('Dificultad:'), sg.Listbox(values=('Facil','Normal','Dificil'),size=(8,3), enable_events=True, key = 'dif')],
      [sg.Text('Facil: Se tomara en cuenta cualquier palabra')],
      [sg.Text('Normal y dificil: Solo se tomaran en cuenta adjetivos y verbos')]
    ])],
      [sg.Button('Guardar'), sg.Button('Cancelar')]
    ]
    self._window = sg.Window('Configuracion').Layout(diseño)

  def crearMenu(self):
    while True:
      event, values = self._window.Read()
      if (event == 'Guardar'):
        if (len(values['dif']) > 0):
          return (values['dif'][0])
        else:
          return('Normal')
  
  def cerrarMenu(self):
    self._window.close()