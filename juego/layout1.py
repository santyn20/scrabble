import PySimpleGUI as sg
from chequear import Check
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from ficha import Ficha
from pozo import Pozo
from tablero1 import Tablero1

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
			#Se ejecuta cuando se hace click en una ficha
			if (not medio):
				#Me aseguro de que la primer ficha vaya en el medio
				window.FindElement("ayu").Update("La primer ficha debe ir en el medio!")
			if (f != None):
				#Si ya tengo una ficha seleccionada, hacer clic de nuevo sobre ella la devuelve al atril
				at.devolverFicha()
				f = None
				if ((not jugando) and (contCambio < 3)):#<---el 3 indica la cantidad de veces que puedo cambiar las fichas
					#Si no estoy armando una palabra, habilito el boton de cambiar fichas
					window.FindElement("cambiar fichas").Update(disabled=False)
			else:
				#Si no tengo ninguna ficha seleccionada, me la guardo
				f = event.getFicha()
				at.actualizarAtril(event)
				window.FindElement("cambiar fichas").Update(disabled=True)
		if ((type(event) == Boton0) or (type(event) == Boton1) or (type(event) == Boton2)):
			#Se ejecuta cuando hago click en cualquier boton del Tablero
			if ((event.getCoor() == (8,8)) and (f != None) and (not medio)):
				#Si selecciono el boton del medio del tablero y tengo una ficha seleccionada, la posiciono en el medio y habilito los demas botones
				medio = True
			if (medio):
				#Si ya hay una ficha en el medio entro al if

				if (ch.checkLugar(event.getCoor())):
					#Verifico que el lugar en el que quiero ingresar la ficha sea correcto

					if (event.getFicha() == None):
						#Compruebo que el boton en el que quiere ingresar la ficha, no tenga una
						if (f != None):
							#Verifico que se tenga una ficha seleccionada
							if (ch.getPosIni() == (0,0)):
								#Actualizo la posicion inicial de la primer letra de la palabra
								ch.setPosIni(event.getCoor())
							event.setFicha(f)
							ch.agregarLetra(event)
							jugando = True
							window.FindElement("cambiar fichas").Update(disabled=True)
							at.actualizarAtril(f,True)
							f = None



		if (event == "cambiar fichas"):
			#Se ejecuta cuando se hace click en "cambiar fichas. Habilito el boton para cancelar la accion y actualizo el mensaje de ayuda"
			
			window.FindElement("ayu").Update("Seleccione las fichas a cambiar!")
			window.FindElement("cancelar").Update(disabled=False)
			seleccionar = True
			while (seleccionar):
				#Mientras se esten seleccionando fichas, los unicos eventos habilitados son los de las fichas
				event,values = window.read()
				if (type(event) == Ficha):
					#Agrego la ficha a una lista para luego reemplazarlas
					at.seleccionarFicha(event)
				if (event == "cambiar fichas"):
					#Se confirma la accion y se cambian las fichas.
					contCambio += 1
					pozo.agregarFichas(at.getCache())
					at.renovarFichas()
					seleccionar = False
					window.FindElement("cancelar").Update(disabled=True)
					if (contCambio == 3):
						#Si ya gaste todos mis cambios, deshabilito el boton
						window.FindElement("cambiar fichas").Update(disabled=True)

					#TURNO DE LA IA <---------

				if (event == "cancelar"):
					#Cancelo el cambio de fichas
					at.deseleccionarFicha()
					seleccionar = False
					window.FindElement("cancelar").Update(disabled=True)




		if (event == "check"):
			#Se ejecuta si quiero verificar que la palabra ingresada es correcta mediante el boton "check"
			if (ch.buscar()):
				#Verifico que la palabra ingresada sea correcta, en caso de serlo calculo el puntaje y renuevo las fichas usadas
				miPuntaje = ch.calcularPuntaje(miPuntaje)
				window.FindElement("p").Update(miPuntaje)
				ch.reiniciarPalabra()
				ch.setPosIni((0,0))
				at.renovarFichas()
				jugando = False
				if (contCambio < 3):
					#Cuando termino de armar una palabra vuelvo a habilitar el boton para cambiar fichas, si es que aun tengo usos
					window.FindElement("cambiar fichas").Update(disabled=False)
				#TURNO DE LA IA <---------
			else:
				#Si la palabra no es correcta, devuelvo las letras
				at.limpiarCache()
				at.devolverFicha()
				ch.limpiar()
				if (ch.getPosIni() == (8,8)):
					#Si la palabra incorrecta era la primera de todas, el medio vuelve a ser requerido
					medio = False
				ch.setPosIni((0,0))
				ch.reiniciarPalabra()
				if (ch.getPalabra() == ''):
					#Actualizo el mensaje de ayuda si no se ingreso una palabra
					window.FindElement("ayu").Update("Ingrese una palabra!")
				else:
					#Si se ingreso una palabra, pero es incorrecta, actualizo mensaje de ayuda
					window.FindElement("ayu").Update("La palabra '"+ch.getPalabra()+"' es invalida!")
					jugando = False
					window.FindElement("cambiar fichas").Update(disabled=False)
			

		if (event == "cerrar"):
			#Cerrar el juego
			ok = False
	window.close()
