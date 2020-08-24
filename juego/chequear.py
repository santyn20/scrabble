import pattern.es
from config import Configuracion
import random
class Check():


  def __init__(self,conf):
    self._posIni = (0,0)
    self._posAct = (0,0)
    self._derecha = False
    self._abajo = False
    self._casillas = [] #<---Lista con los botones donde se esta ingresando una palabra
    self._palabra = '' #<---La palabra en si
    self._conf=conf.Nivel()
    self._tipo=random.choice(["VB","NN","JJ"])



  def checkLugar(self,pos):
    '''Este metodo verifica que la posicion en la que se esta poninendo una ficha sea correcto'''
    if ((pos[0] > 15) or (pos[1] > 15)):
      return False

    if (self._posIni == (0,0)):
      #Entra si es la primer ficha para una palabra
      return True

    if (self._derecha):
      #La palbra esta siendo escrita para la derecha
      if ( (pos[1] - self._posAct[1] == 1) and (pos[0] == self._posAct[0]) ):
        #Tiene que ser adyacente a derecha para ser valida
        self._posAct = pos
        return self._derecha
      else:
        return False


    if (self._abajo):
      #La palabra esta siendo escrita para abajo
      if ( (pos[0] - self._posAct[0] == 1) and (pos[1] == self._posAct[1]) ):
        #Tiene que ser adyacente para abajo para ser valida
        self._posAct = pos
        return self._abajo
      else:
        return False


    if ( (pos[0] - self._posAct[0] == 1) and (pos[1] == self._posAct[1]) ):
      #Si la letra se ingresa justo abajo de la primera, actualizo la variable "abajo"
      self._posAct = pos
      self._abajo = True
      return self._abajo
    if ( (pos[1] - self._posAct[1] == 1) and (pos[0] == self._posAct[0]) ):
      #Si la letra se ingresa justo a la derecha de la primera, actualizo la variable "derecha"
      self._posAct = pos
      self._derecha = True
      return self._derecha
    else:
      #Si la letra no se ingresa en una posicion valida (derecha o abajo) devuelvo false
      return False

#INICIO GETTERS Y SETTERS

  def getPosIni(self):
    return self._posIni

  def getPalabra(self):
    return self._palabra

  def setPosIni(self,pos):
    self._posAct = pos
    self._posIni = pos

#FIN GETTERS Y SETTERS

  def reiniciar(self):
    self._derecha = False
    self._abajo = False

  def calcularPuntaje(self,p):
    '''Calculo el puntaje de la palabra ingresada'''
    for i in self._casillas:
      p += i.getPuntaje()
    return p

  def reiniciarPalabra(self):
    '''Limpio la lista que guarda la palabra que se esta armando'''
    self._casillas.clear()

  def agregarLetra(self,let):
    '''Agrego una letra(boton donde esta la ficha) a la palabra que se esta armando'''
    self._casillas.append(let)

  def limpiar(self):
    '''Se quita la palabra del tablero'''
    for i in self._casillas:
      i.limpiarFicha()
    self.reiniciarPalabra()

  
  def buscar(self):
    '''Verifico que la palabra ingresada sea correcta'''
    self._palabra = ''
    for i in self._casillas:
      self._palabra += i.getFicha().getLetra()
    if (len(self._palabra) < 2):
      return False
    encuentro = False
    if ( (self._palabra in pattern.es.spelling.keys()) and (self._palabra != '')):
      encuentro = self.buscarPorNivel(pattern.es.parse(self._palabra).split())
      self._derecha = False
      self._abajo = False
    return encuentro


  def buscarPorNivel(self,p):
    if self._conf=="Facil":
      for cada in p:
        for c in cada:
          if ((c[1] == 'VB') or (c[1] ==  "NNS" or c[1] ==  "NN") or (c[1] ==  "JJ")):
            return True
    elif self._conf=="Normal":
      for cada in p:
        for c in cada:
          if ((c[1] == 'VB')or(c[1] ==  "NNS") or (c[1] ==  "NN")):
            return True
    else:
      for cada in p:
        for c in cada:
          if (c[1] == self._tipo):
            return True
  
