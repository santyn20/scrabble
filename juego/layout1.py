import PySimpleGUI as sg
from chequear import Check
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from ficha import Ficha
from pozo import Pozo
from tablero1 import Tablero1

#Deberia iniciar pozo aqui??????????<<<<<<<<<<<<<<<----------

def main():

	pozo = Pozo()

	miPuntaje = 0

	iaPuntaje = 0

	sg.theme('Dark Brown')
	tab = Tablero1()
	at = Atril(pozo)
	ch = Check()
	layout = tab.crearTablero()
	layout.append(at.mostrarAtril())
	layout.append([sg.Button("cerrar"),sg.Button("check"),sg.Button("cambiar fichas"),sg.Button("cancelar",disabled=True),sg.Text("Puntaje", size=(7,1)),sg.Text(miPuntaje, size=(4,1),key="p")])
	layout.append([sg.Text("Ayuda:", size=(7,1)),sg.Text("", size=(30,1),key="ayu")])
	window = sg.Window('Tablero', layout, finalize = True)
	ok = True
	f = None
	jugando = False
	medio = False
	inicio = (0,0)

	contCambio = 0



	while ok:
		event,values = window.read()
	

		if (type(event) == Ficha):
			if (not medio):
				window.FindElement("ayu").Update("La primer ficha debe ir en el medio!")
			if (f != None):
				at.devolverFicha()
				f = None
				if ((not jugando) and (contCambio < 3)):
					window.FindElement("cambiar fichas").Update(disabled=False)
			else:
				f = event.getFicha()
				at.actualizarAtril(event)
				window.FindElement("cambiar fichas").Update(disabled=True)
		if ((type(event) == Boton0) or (type(event) == Boton1) or (type(event) == Boton2)):
			if ((event.getCoor() == (8,8)) and (f != None) and (not medio)):
				medio = True
			if (medio):

				if (ch.checkLugar(event.getCoor())):

					if (event.getFicha() == None):
						if (f != None):
							if (ch.getPosIni() == (0,0)):
								ch.setPosIni(event.getCoor())
							event.setFicha(f)
							ch.agregarLetra(event)
							jugando = True
							window.FindElement("cambiar fichas").Update(disabled=True)
							at.actualizarAtril(f,True)
							f = None



		if (event == "cambiar fichas"):
			contCambio += 1
			window.FindElement("ayu").Update("Seleccione las fichas a cambiar!")
			window.FindElement("cancelar").Update(disabled=False)
			seleccionar = True
			while (seleccionar):
				event,values = window.read()
				if (type(event) == Ficha):
					at.seleccionarFicha(event)
				if (event == "cambiar fichas"):
					pozo.agregarFichas(at.getCache())
					at.renovarFichas()
					seleccionar = False
					window.FindElement("cancelar").Update(disabled=True)
					if (contCambio == 3):
						window.FindElement("cambiar fichas").Update(disabled=True)

					#TURNO DE LA IA <---------

				if (event == "cancelar"):
					at.deseleccionarFicha()
					seleccionar = False
					window.FindElement("cancelar").Update(disabled=True)




		if (event == "check"):
			if (ch.buscar()):
				miPuntaje = ch.calcularPuntaje(miPuntaje)
				window.FindElement("p").Update(miPuntaje)
				ch.reiniciarPalabra()
				ch.setPosIni((0,0))
				at.renovarFichas()
				jugando = False
				if (contCambio < 3):
					window.FindElement("cambiar fichas").Update(disabled=False)
				#TURNO DE LA IA <---------
			else:
				at.limpiarCache()
				at.devolverFicha()
				ch.limpiar()
				if (ch.getPosIni() == (8,8)):
					medio = False
				ch.setPosIni((0,0))
				ch.reiniciarPalabra()
				if (ch.getPalabra() == ''):
					window.FindElement("ayu").Update("Ingrese una palabra!")
				else:
					window.FindElement("ayu").Update("La palabra '"+ch.getPalabra()+"' es invalida!")
					jugando = False
					window.FindElement("cambiar fichas").Update(disabled=False)
			

		if (event == "cerrar"):
			ok = False
	window.close()
