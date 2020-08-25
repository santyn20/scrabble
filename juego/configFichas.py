import PySimpleGUI as sg
import json

class ConfigFichas:

	def __init__(self):
		pass

	def main(self):

		alph = ["A","B","C","D","E","F","G","H","I","J","K","L","LL","M","N","Ñ","O","P","Q","R","RR","S","T","U","V","W","X","Y","Z"]

		try:
			archivo = open("fichas.json", "r")
			datos = json.load(archivo)
		except FileNotFoundError:
			col1 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("A"),sg.InputText("11",size=(8,3),key="cantA"),sg.InputText("1",size=(8,3),key="puntA")],
					[sg.Text("B"),sg.InputText("3",size=(8,3),key="cantB"),sg.InputText("3",size=(8,3),key="puntB")],
					[sg.Text("C"),sg.InputText("4",size=(8,3),key="cantC"),sg.InputText("2",size=(8,3),key="puntC")],
					[sg.Text("D"),sg.InputText("4",size=(8,3),key="cantD"),sg.InputText("2",size=(8,3),key="puntD")],
					[sg.Text("E"),sg.InputText("11",size=(8,3),key="cantE"),sg.InputText("1",size=(8,3),key="puntE")],
					[sg.Text("F"),sg.InputText("2",size=(8,3),key="cantF"),sg.InputText("4",size=(8,3),key="puntF")],
					[sg.Text("G"),sg.InputText("2",size=(8,3),key="cantG"),sg.InputText("2",size=(8,3),key="puntG")],
					[sg.Text("H"),sg.InputText("2",size=(8,3),key="cantH"),sg.InputText("4",size=(8,3),key="puntH")],
					

			]
			col2 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("I"),sg.InputText("6",size=(8,3),key="cantI"),sg.InputText("1",size=(8,3),key="puntI")],
					[sg.Text("J"),sg.InputText("2",size=(8,3),key="cantJ"),sg.InputText("6",size=(8,3),key="puntJ")],
					[sg.Text("K"),sg.InputText("1",size=(8,3),key="cantK"),sg.InputText("7",size=(8,3),key="puntK")],
					[sg.Text("L"),sg.InputText("4",size=(8,3),key="cantL"),sg.InputText("1",size=(8,3),key="puntL")],
					[sg.Text("LL"),sg.InputText("1",size=(8,3),key="cantLL"),sg.InputText("7",size=(8,3),key="puntLL")],
					[sg.Text("M"),sg.InputText("3",size=(8,3),key="cantM"),sg.InputText("3",size=(8,3),key="puntM")],
					[sg.Text("N"),sg.InputText("5",size=(8,3),key="cantN"),sg.InputText("1",size=(8,3),key="puntN")],
					[sg.Text("Ñ"),sg.InputText("1",size=(8,3),key="cantÑ"),sg.InputText("7",size=(8,3),key="puntÑ")],
					

			]
			col3 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("O"),sg.InputText("8",size=(8,3),key="cantO"),sg.InputText("1",size=(8,3),key="puntO")],
					[sg.Text("P"),sg.InputText("2",size=(8,3),key="cantP"),sg.InputText("3",size=(8,3),key="puntP")],
					[sg.Text("Q"),sg.InputText("1",size=(8,3),key="cantQ"),sg.InputText("7",size=(8,3),key="puntQ")],
					[sg.Text("R"),sg.InputText("4",size=(8,3),key="cantR"),sg.InputText("1",size=(8,3),key="puntR")],
					[sg.Text("RR"),sg.InputText("1",size=(8,3),key="cantRR"),sg.InputText("7",size=(8,3),key="puntRR")],
					[sg.Text("S"),sg.InputText("7",size=(8,3),key="cantS"),sg.InputText("1",size=(8,3),key="puntS")],
					[sg.Text("T"),sg.InputText("4",size=(8,3),key="cantT"),sg.InputText("1",size=(8,3),key="puntT")],
					[sg.Text("U"),sg.InputText("6",size=(8,3),key="cantU"),sg.InputText("1",size=(8,3),key="puntU")],
					

			]
			col4 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("V"),sg.InputText("2",size=(8,3),key="cantV"),sg.InputText("4",size=(8,3),key="puntV")],
					[sg.Text("W"),sg.InputText("1",size=(8,3),key="cantW"),sg.InputText("7",size=(8,3),key="puntW")],
					[sg.Text("X"),sg.InputText("1",size=(8,3),key="cantX"),sg.InputText("7",size=(8,3),key="puntX")],
					[sg.Text("Y"),sg.InputText("1",size=(8,3),key="cantY"),sg.InputText("4",size=(8,3),key="puntY")],
					[sg.Text("Z"),sg.InputText("1",size=(8,3),key="cantZ"),sg.InputText("10",size=(8,3),key="puntZ")],

			]

		else:

			col1 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("A"),sg.InputText(datos["A"]["cant"],size=(8,3),key="cantA"),sg.InputText(datos["A"]["punt"],size=(8,3),key="puntA")],
					[sg.Text("B"),sg.InputText(datos["B"]["cant"],size=(8,3),key="cantB"),sg.InputText(datos["B"]["punt"],size=(8,3),key="puntB")],
					[sg.Text("C"),sg.InputText(datos["C"]["cant"],size=(8,3),key="cantC"),sg.InputText(datos["C"]["punt"],size=(8,3),key="puntC")],
					[sg.Text("D"),sg.InputText(datos["D"]["cant"],size=(8,3),key="cantD"),sg.InputText(datos["D"]["punt"],size=(8,3),key="puntD")],
					[sg.Text("E"),sg.InputText(datos["E"]["cant"],size=(8,3),key="cantE"),sg.InputText(datos["E"]["punt"],size=(8,3),key="puntE")],
					[sg.Text("F"),sg.InputText(datos["F"]["cant"],size=(8,3),key="cantF"),sg.InputText(datos["F"]["punt"],size=(8,3),key="puntF")],
					[sg.Text("G"),sg.InputText(datos["G"]["cant"],size=(8,3),key="cantG"),sg.InputText(datos["G"]["punt"],size=(8,3),key="puntG")],
					[sg.Text("H"),sg.InputText(datos["H"]["cant"],size=(8,3),key="cantH"),sg.InputText(datos["H"]["punt"],size=(8,3),key="puntH")],
					

			]
			col2 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("I"),sg.InputText(datos["I"]["cant"],size=(8,3),key="cantI"),sg.InputText(datos["I"]["punt"],size=(8,3),key="puntI")],
					[sg.Text("J"),sg.InputText(datos["J"]["cant"],size=(8,3),key="cantJ"),sg.InputText(datos["J"]["punt"],size=(8,3),key="puntJ")],
					[sg.Text("K"),sg.InputText(datos["K"]["cant"],size=(8,3),key="cantK"),sg.InputText(datos["K"]["punt"],size=(8,3),key="puntK")],
					[sg.Text("L"),sg.InputText(datos["L"]["cant"],size=(8,3),key="cantL"),sg.InputText(datos["L"]["punt"],size=(8,3),key="puntL")],
					[sg.Text("LL"),sg.InputText(datos["LL"]["cant"],size=(8,3),key="cantLL"),sg.InputText(datos["LL"]["punt"],size=(8,3),key="puntLL")],
					[sg.Text("M"),sg.InputText(datos["M"]["cant"],size=(8,3),key="cantM"),sg.InputText(datos["M"]["punt"],size=(8,3),key="puntM")],
					[sg.Text("N"),sg.InputText(datos["N"]["cant"],size=(8,3),key="cantN"),sg.InputText(datos["N"]["punt"],size=(8,3),key="puntN")],
					[sg.Text("Ñ"),sg.InputText(datos["Ñ"]["cant"],size=(8,3),key="cantÑ"),sg.InputText(datos["Ñ"]["punt"],size=(8,3),key="puntÑ")],
					

			]
			col3 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("O"),sg.InputText(datos["O"]["cant"],size=(8,3),key="cantO"),sg.InputText(datos["O"]["punt"],size=(8,3),key="puntO")],
					[sg.Text("P"),sg.InputText(datos["P"]["cant"],size=(8,3),key="cantP"),sg.InputText(datos["P"]["punt"],size=(8,3),key="puntP")],
					[sg.Text("Q"),sg.InputText(datos["Q"]["cant"],size=(8,3),key="cantQ"),sg.InputText(datos["Q"]["punt"],size=(8,3),key="puntQ")],
					[sg.Text("R"),sg.InputText(datos["R"]["cant"],size=(8,3),key="cantR"),sg.InputText(datos["R"]["punt"],size=(8,3),key="puntR")],
					[sg.Text("RR"),sg.InputText(datos["RR"]["cant"],size=(8,3),key="cantRR"),sg.InputText(datos["RR"]["punt"],size=(8,3),key="puntRR")],
					[sg.Text("S"),sg.InputText(datos["S"]["cant"],size=(8,3),key="cantS"),sg.InputText(datos["S"]["punt"],size=(8,3),key="puntS")],
					[sg.Text("T"),sg.InputText(datos["T"]["cant"],size=(8,3),key="cantT"),sg.InputText(datos["T"]["punt"],size=(8,3),key="puntT")],
					[sg.Text("U"),sg.InputText(datos["U"]["cant"],size=(8,3),key="cantU"),sg.InputText(datos["U"]["punt"],size=(8,3),key="puntU")],
					

			]
			col4 = [[sg.Text("	cantidad"),sg.Text("puntaje")],
					[sg.Text("V"),sg.InputText(datos["V"]["cant"],size=(8,3),key="cantV"),sg.InputText(datos["V"]["punt"],size=(8,3),key="puntV")],
					[sg.Text("W"),sg.InputText(datos["W"]["cant"],size=(8,3),key="cantW"),sg.InputText(datos["W"]["punt"],size=(8,3),key="puntW")],
					[sg.Text("X"),sg.InputText(datos["X"]["cant"],size=(8,3),key="cantX"),sg.InputText(datos["X"]["punt"],size=(8,3),key="puntX")],
					[sg.Text("Y"),sg.InputText(datos["Y"]["cant"],size=(8,3),key="cantY"),sg.InputText(datos["Y"]["punt"],size=(8,3),key="puntY")],
					[sg.Text("Z"),sg.InputText(datos["Z"]["cant"],size=(8,3),key="cantZ"),sg.InputText(datos["Z"]["punt"],size=(8,3),key="puntZ")],

			]
			archivo.close()


		layout = [[sg.Column(col1),sg.Column(col2),sg.Column(col3),sg.Column(col4)],[sg.Button("guardar")]]

		window = sg.Window("Config fichas",layout)
		ok = True
		error = False
		while ok:
			event,values = window.read()
			if (event == "guardar"):
				archivo = open("fichas.json","w")
				datos = {}
				for i in alph:
					indx = "cant"+i
					indx2 = "punt"+i
					if (values[indx] == "0"):
						error = True
						break
					try:
						datos[i] = {"cant":int(values[indx]), "punt":int(values[indx2])}
					except ValueError:
						error = True
				if (error):
					sg.Popup("DATOS INCORRECTOS, POR FAVOR INGRESE NUMEROS > 0")
					archivo.close()
					error = False
				else:
					json.dump(datos,archivo,indent=2)
					sg.Popup("Guardado con exito!")
					archivo.close()
					ok = False
					
		window.close()
