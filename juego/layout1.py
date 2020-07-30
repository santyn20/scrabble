import PySimpleGUI as sg
from chequear import Check
from boton0 import Boton0
from boton1 import Boton1
from boton2 import Boton2
from atril import Atril
from ficha import Ficha
from tablero1 import Tablero1
from IA import InteligenciaArtificial

def main():


	miPuntaje = 0

	iaPuntaje = 0

	sg.theme('Dark Brown')
	tab = Tablero1()
	at = Atril()
	ch = Check()
	layout = tab.crearTablero()
	layout.append(at.mostrarAtril())
	layout.append([sg.Button("cerrar"),sg.Button("check"),sg.Text("Puntaje", size=(7,1)),sg.Text(miPuntaje, size=(4,1),key="p")])
	layout.append([sg.Text("Ayuda:", size=(7,1)),sg.Text("", size=(30,1),key="ayu")])
	window = sg.Window('Tablero', layout, finalize = True)
	ok = True
	f = None
	medio = False
	inicio = (0,0)



	while ok:
		event,values = window.read()

		
    if (type(event) == Ficha):
      if (f != None):
        at.devolverFicha()
        f = None
      else:
        f = event.getFicha()
        at.actualizarAtril(event)
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
              at.actualizarAtril(f,True)
              f = None


		if (event == "check"):
			if (ch.buscar()):
				miPuntaje = ch.calcularPuntaje(miPuntaje)
				window.FindElement("p").Update(miPuntaje)
				ch.reiniciarPalabra()
				ch.setPosIni((0,0))
				at.renovarFichas()
			else:
				at.limpiarCache()
				at.devolverFicha()
				ch.limpiar()
				if (ch.getPosIni() == (8,8)):
					medio = False
				ch.setPosIni((0,0))
				if (ch.getPalabra() == ''):
					window.FindElement("ayu").Update("Ingrese una palabra!")
				else:
					window.FindElement("ayu").Update("La palabra '"+ch.getPalabra()+"' es invalida!")
			

		if (event == "cerrar"):
			ok = False
	window.close()

