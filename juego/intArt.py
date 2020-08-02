import random
import PySimpleGUI as sg
from chequear import Check
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from ficha import Ficha
from tablero1 import Tablero1



class IntArt():

	def __init__(self,tab):
		self._atril = Atril()
		self._atril.cargarAtril()
		self._tablero = tab.getBotones()


	def selecPos(self):
		palabra = self.buscar()
		seguir = True
		derecha = True
		abajo = True
		while (seguir):
			lugar = random.choice(self._tablero)
			if (lugar.getFicha() == None):
				for i in (len(palabra)-1):
					if (tablero.getBotonByPos( (lugar.getCoor()[0]+i,lugar.getCoor()[1]) ).getFicha() != None):
						derecha = False
						break
				if (not derecha):
					for i in len(palabra):
						if (tablero.getBotonByPos( (lugar.getCoor()[0],lugar.getCoor()[1]+i) ).getFicha() != None):
							abajo = False
							break

				if (derecha):
					for i in len(palabra):
						tablero.getBotonByPos( (lugar.getCoor()[0]+i,lugar.getCoor()[1]) ).setFicha(self._atril.getFichaByLetra(palabra[i]))

						#TENGO QUE COMPROBAR CASOS EN LOS QUE LA FICHA TENGA "RR" O "LL"

						self._atril.agregarCache(self._atril.getFichaByLetra(palabra[i]))




	def datosBuenos(self):
    letras = []
    for i in self._atril:
      letras.append(i.getLetra())
    return letras
  
  	def buscar(self):
	    pal = []
	    for x in pattern.es.lexicon.keys():
	      if x in pattern.es.spelling.keys():
	        regex="("+".*?".join(x) + ")"
	        lista1Cadena=" ".join(self.datosBuenos())
	        encontrados = re.finditer(regex, lista1Cadena, re.MULTILINE)
	        cantidad=len([matchNum for matchNum, match in enumerate(encontrados, start=1)])
	        if cantidad >= 1:
	          pal.append(x)
	    pal.sort(key = lambda s: len(s))
	    return(pal.pop())