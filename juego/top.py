import PySimpleGUI as sg
class Top():
  def CrearTop(self,d):
    layout=[]
    x=1
    for i in range(10):
      n=[]
      linea=d.readline()
      l1,l2=linea.split(',')
      jg=sg.Text(x,size=(2,1))
      n.append(jg)
      jg=sg.Text(l1,size=(15,1))
      n.append(jg)
      jg=sg.Text(l2,size=(5,1))
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

      