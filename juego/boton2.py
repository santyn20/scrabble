
import PySimpleGUI as sg
class Boton2():

	def __init__(self,coor):
		self._tipo = "menos"
		self._color = "#A93226"
		self._coor = coor
		self._ficha = None
		self._boton = sg.Button("",button_color=('black',self.getColor()), size=(3, 2), pad=(0, 0), key=self)

	def getTipo(self):
		return self._tipo

	def getColor(self):
		return self._color

	def getCoor(self):
		return self._coor

	def getBoton(self):
		return self._boton

	def getFicha(self):
		return self._ficha

	def setFicha(self,f):
		self._ficha = f
		self._boton.Update(f.getLetra())

	def getPuntaje(self):
		self.deshabilitarLugar()
		return (self._ficha.getPuntaje()-2)

	def deshabilitarLugar(self):
		self._boton.Update(disabled=True)
		self._boton.Update(button_color=("black","#7B241C"))

	def limpiarFicha(self):
		self._ficha = None
		self._boton.Update("")