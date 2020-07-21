
import random
import PySimpleGUI as sg
from ficha import Ficha

class Pozo():

	pozoFichas = []


	def __init__(self):
		dicc ={
			'a':[11,1],
			'e':[11,1],
			'o':[8,1],
			's':[7,1],
			'i':[6,1],
			'u':[6,1],
			'n':[5,1],
			'l':[4,1],
			'r':[4,1],
			't':[4,1],
			'c':[4,2],
			'd':[4,2],
			'g':[2,2],
			'm':[3,3],
			'b':[3,3],
			'p':[2,3],
			'f':[2,4],
			'h':[2,4],
			'v':[2,4],
			'y':[1,4],
			'j':[2,6],
			'k':[1,7],
			'll':[1,7],
			'ñ':[1,7],
			'q':[1,7],
			'rr':[1,7],
			'w':[1,7],
			'x':[1,7],
			'z':[1,10]

		}
		for key in dicc:
			for i in range(dicc[key][0]):
				f = Ficha(key,dicc[key][1])
				self.pozoFichas.append(f)
		random.shuffle(self.pozoFichas)

	def getFicha(self):
		ficha = self.pozoFichas.pop()
		return ficha
	def getP(self):
		return self.pozoFichas


