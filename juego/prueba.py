import PySimpleGUI as sg
import sys


class Prueba():

	def __init__(self,val):
		self._pr = val
		self._boton = sg.Button("aaaaa",button_color=('black','white'), size=(10, 5), pad=(0, 0), key=self)

	def getPr(self):
		return self._pr

	def getBoton(self):
		return self._boton

	def upd(self,boton):
		boton.Update('')


layout = []
val = 0
pr = Prueba(val)
val = 1
pr1 = Prueba(val)

print(pr.getPr())

layout.append([pr.getBoton(),
	pr1.getBoton(),sg.Button("Cerrar")])
window = sg.Window('Prueba', layout)
ok = True

while(ok):
	event,values = window.read()
	if (type(event) is Prueba):
		event.upd(event.getBoton())
	if (event == "Cerrar"):
		ok = False

window.close()
