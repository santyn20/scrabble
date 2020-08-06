from boton import Boton
import PySimpleGUI as sg
class Boton1(Boton):

	def __init__(self,coor):
		boton = sg.Button("",button_color=('black',"#239B56"), size=(3, 2), pad=(0, 0), key=self)
		super().__init__("plus","#239B56",coor,boton)

#INICIO GETTERS Y SETTERS

	def getPuntaje(self):
		self.deshabilitarLugar()
		return (self._ficha.getPuntaje()*2)

#FIN GETTERS Y SETTERS

	def deshabilitarLugar(self):
		'''Este metodo deshabilita los botones del tablero donde ya hay una ficha'''
		self._boton.Update(disabled=True)
		self._boton.Update(button_color=("black","#186A3B"))
