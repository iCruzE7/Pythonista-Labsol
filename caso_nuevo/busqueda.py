#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""La Función Principal es buscar()"""
import caso_nuevo.datos as datos

campos = ("Nombre", "Primer Apellido", "Segundo Apellido")


def despliega_uno(elemento):
    listaResultados = []
    for campo in datos.orden:
        #print(campo + ": " + str(elemento[campo]))
        listaResultados.append(campo + ": " + str(elemento[campo]))
    print(tuple(listaResultados)) #Mostrar todos los datos de ese alumno en forma de tupla



def buscaEspec(elemento, cadena):
    for campo in campos:
        if cadena.lower() in elemento[campo].lower():   #Si se encuentra la cadena deseada
            #print(campo + ": " + str(elemento[campo]))
            despliega_uno(elemento)     #Mostrar todos los datos de ese alumno


def buscar(cadena, ruta=datos.ruta):
	"""Esta es la función Principal a llamar """
    with open(ruta, 'r') as archivo:    #'r' para modo lectura y cierre automáticamente al archivo        
        for alumno in archivo:  	#Para cada alumno registrado en el archivo
            alumno = eval(alumno)                       
            buscaEspec(alumno, cadena)
	