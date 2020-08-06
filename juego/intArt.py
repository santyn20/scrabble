import random
import PySimpleGUI as sg
import pattern.es
import re
import random
from chequear import Check
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from ficha import Ficha
from tablero1 import Tablero1



class IntArt():

	def __init__(self,tab,p,conf):
		self._atril = Atril(p)
		self._tablero = tab
		self._ch = Check(conf)


	def selecPos(self):
		palabra = self.buscar()
		lugares = [] #<--botones
		seguir = True
		while (seguir):
			lugar = random.choice(self._tablero.getBotones())
			if (lugar.getFicha() == None):
				orientacion = random.randint(1,2)

				if (orientacion == 1):
					for i in range(len(palabra)):
						if (self._ch.checkLugar( (lugar.getCoor()[0],lugar.getCoor()[1]+i) )):
							if (self._tablero.getBotonByPos((lugar.getCoor()[0], lugar.getCoor()[1]+i) ).getFicha() == None ):
								lugares.append(self._tablero.getBotonByPos( (lugar.getCoor()[0], lugar.getCoor()[1]+i) ))
							else:
								lugares.clear()
								break
						else:
							lugares.clear()
							break
				else:
					for i in range(len(palabra)):
						if (self._ch.checkLugar( (lugar.getCoor()[0]+i,lugar.getCoor()[1]) )):
							if (self._tablero.getBotonByPos((lugar.getCoor()[0]+i, lugar.getCoor()[1]) ).getFicha() == None ):
								lugares.append(self._tablero.getBotonByPos( (lugar.getCoor()[0]+i, lugar.getCoor()[1]) ))
							else:
								lugares.clear()
								break
						else:
							lugares.clear()
							break
				if ((len(lugares) > 0)):
					seguir = False

		cant = 0
		p = 0
		for i in lugares:
			i.setFicha( self._atril.getFichaByLetra(palabra[cant]) )
			self._atril.agregarCache( self._atril.getFichaByLetra(palabra[cant]) )
			self._ch.agregarLetra(i)
			p += self._ch.calcularPuntaje(0)
			self._ch.reiniciarPalabra()
			self._atril.renovarFichasIA()
			cant += 1
		return p







	def datosBuenos(self):
		letras = []
		for i in self._atril.getAtril():
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
				if (cantidad >= 1):
					pal.append(x)
		pal.sort(key = lambda s: len(s))
		return(pal.pop())