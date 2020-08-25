import json
import random
import PySimpleGUI as sg
from ficha import Ficha

class Pozo():

	pozoFichas = []


	def __init__(self):

		try:
			archivo = open("fichas.json", "r")
			datos = json.load(archivo)
		except FileNotFoundError:

			dicc ={
				'a':[11,1],
				'b':[3,3],
				'c':[4,2],
				'd':[4,2],
				'e':[11,1],
				'f':[2,4],
				'g':[2,2],
				'h':[2,4],
				'i':[6,1],
				'j':[2,6],
				'k':[1,7],
				'l':[4,1],
				'll':[1,7],
				'm':[3,3],
				'n':[5,1],
				'ñ':[1,7],
				'o':[8,1],
				'p':[2,3],
				'q':[1,7],
				'r':[4,1],
				'rr':[1,7],
				's':[7,1],
				't':[4,1],
				'u':[6,1],
				'v':[2,4],
				'w':[1,7],
				'x':[1,7],
				'y':[1,4],
				'z':[1,10]

			}
		else:

			dicc ={
				'a':[datos["A"]["cant"],datos["A"]["punt"]],
				'b':[datos["B"]["cant"],datos["B"]["punt"]],
				'c':[datos["C"]["cant"],datos["C"]["punt"]],
				'd':[datos["D"]["cant"],datos["D"]["punt"]],
				'e':[datos["E"]["cant"],datos["E"]["punt"]],
				'f':[datos["F"]["cant"],datos["F"]["punt"]],
				'g':[datos["G"]["cant"],datos["G"]["punt"]],
				'h':[datos["H"]["cant"],datos["H"]["punt"]],
				'i':[datos["I"]["cant"],datos["I"]["punt"]],
				'j':[datos["J"]["cant"],datos["J"]["punt"]],
				'k':[datos["K"]["cant"],datos["K"]["punt"]],
				'l':[datos["L"]["cant"],datos["L"]["punt"]],
				'll':[datos["LL"]["cant"],datos["LL"]["punt"]],
				'm':[datos["M"]["cant"],datos["M"]["punt"]],
				'n':[datos["N"]["cant"],datos["N"]["punt"]],
				'ñ':[datos["Ñ"]["cant"],datos["Ñ"]["punt"]],
				'o':[datos["O"]["cant"],datos["O"]["punt"]],
				'p':[datos["P"]["cant"],datos["P"]["punt"]],
				'q':[datos["Q"]["cant"],datos["Q"]["punt"]],
				'r':[datos["R"]["cant"],datos["R"]["punt"]],
				'rr':[datos["RR"]["cant"],datos["RR"]["punt"]],
				's':[datos["S"]["cant"],datos["S"]["punt"]],
				't':[datos["T"]["cant"],datos["T"]["punt"]],
				'u':[datos["U"]["cant"],datos["U"]["punt"]],
				'v':[datos["V"]["cant"],datos["V"]["punt"]],
				'w':[datos["W"]["cant"],datos["W"]["punt"]],
				'x':[datos["X"]["cant"],datos["X"]["punt"]],
				'y':[datos["Y"]["cant"],datos["Y"]["punt"]],
				'z':[datos["Z"]["cant"],datos["Z"]["punt"]]

			}
		for key in dicc:
			for i in range(int(dicc[key][0])):
				f = Ficha(key,int(dicc[key][1]))
				self.pozoFichas.append(f)
		random.shuffle(self.pozoFichas)

	def getFicha(self):
		ficha = self.pozoFichas.pop()
		return ficha
		
	def getP(self):
		return self.pozoFichas

	def agregarFichas(self,fichas):
		'''Metodo para agregar una ficha al pozo'''
		for i in fichas:
			self.pozoFichas.append(i)
		random.shuffle(self.pozoFichas)


