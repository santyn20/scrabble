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

      jg=sg.Text(x,size=(2,1))
      n.append(jg)
      
      if (datos[i]["nombre"] == ""):
        jg=sg.Text("Anonimo")
      else:
        jg=sg.Text(datos[i]["nombre"])
      n.append(jg)
      jg=sg.Text(datos[i]["puntaje"])
      n.append(jg)
      jg=sg.Text(datos[i]["nivel"])
      n.append(jg)
      jg=sg.Text(i)
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

      