import json
import time
class GuardarDatos():
	def __init__(self):
		self._datos = {}
		
	def guardar(self, nom, punt, niv):
		fecha = time.strftime("%c")
		nombre = nom
		puntaje = int(punt)


		dato_nuevo = {'nombre':nombre,'puntaje': punt, 'nivel':niv}
		self._datos.setdefault(fecha,dato_nuevo)
		print(self._datos)
		try:
			with open("datos_juego.json") as f:
				data = json.load(f)
				data[fecha]=dato_nuevo
				datos_or = dict(sorted(data.items(), key=lambda dato: dato[1]['puntaje'], reverse=True))
      
				with open("datos_juego.json", "w") as f:
					json.dump(datos_or, f,indent=2)
		except FileNotFoundError:
    
    
			f = open('datos_juego.json', 'w')
      
			json.dump(self._datos, f,indent=2)
			f.close()
