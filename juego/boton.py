import PySimpleGUI as sg

class Boton:


	def __init__(self,tipo,color,coor,boton,ficha=None):
		self._tipo = tipo
		self._color = color
		self._coor = coor
		self._ficha = ficha
		self._boton = boton

#INICIO GETTERS Y SETTERS

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

#FIN GETTERS Y SETTERS

	def limpiarFicha(self):
		'''Este metodo elimina la ficha que tenga el boton'''
		self._ficha = None
		self._boton.Update("")