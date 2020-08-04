
import PySimpleGUI as sg
class Boton0():

	def __init__(self,coor):
		self._tipo = "normal"
		self._color = "#EBF5FB"
		self._coor = coor
		self._ficha = None
		self._boton = sg.Button("",button_color=('black',self.getColor()), size=(3, 2), pad=(0, 0), key=self)

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

	def getPuntaje(self):
		self.deshabilitarLugar()
		return self._ficha.getPuntaje()

#FIN GETTERS Y SETTERS
		
	def deshabilitarLugar(self):
		'''Este metodo deshabilita los botones del tablero donde ya hay una ficha'''
		self._boton.Update(disabled=True)
		self._boton.Update(button_color=("black","#CCD1D1"))

	def limpiarFicha(self):
		'''Este metodo elimina la ficha que tenga el boton'''
		self._ficha = None
		self._boton.Update("")