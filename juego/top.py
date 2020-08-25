import PySimpleGUI as sg
import json
class Top():
  def CrearTop(self,arch):
    datos = json.load(arch)
    layout=[]
    x=1
    for i in datos:
      if (x > 10):
        break
      n=[]

      jg=sg.Text(x,size=(4,1))
      n.append(jg)
      
      if (datos[i]["nombre"] == ""):
        jg=sg.Text("Anonimo",size=(10,1))
      else:
        jg=sg.Text(datos[i]["nombre"],size=(10,1))
      n.append(jg)
      jg=sg.Text(datos[i]["puntaje"],size=(4,1))
      n.append(jg)
      jg=sg.Text(datos[i]["nivel"],size=(10,1))
      n.append(jg)
      jg=sg.Text(i,size=(15,1))
      n.append(jg)
      x+=1
      layout.append(n)
    b=[sg.Button("Salir")]
    layout.append(b)
    window=sg.Window("Top 10 jugadores",layout)
    while True:
      event,values=window.read()
      if event=='Salir':
        break
    window.close()

      