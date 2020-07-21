import PySimpleGUI as sg

class Ficha():

	def __init__(self,l,p):
		self._letra = l
		self._puntaje = p
		self._color = "#F1C40F"
		self._coor = 0
		self._boton = sg.Button(self._letra,button_color=('black',self.getColor()), size=(3, 2), pad=(0, 0), key=self)

	def getBoton(self):
		return self._boton

	def getColor(self):
		return self._color

	def getPuntaje(self):
		return self._puntaje

	def getLetra(self):
		return self._letra

	def getFicha(self):
		return self

	def setCoor(self,p):
		self._coor = p