#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""La Función Principal es buscar()"""
import caso.datos as datos

campos = ("Nombre", "Primer Apellido", "Segundo Apellido")


def despliega_uno(elemento):
    listaResultados = []
    for campo in datos.orden:
        #print(campo + ": " + str(elemento[campo]))
        listaResultados.append(campo + ": " + str(elemento[campo]))
    print(tuple(listaResultados)) #Mostrar todos los datos de ese alumno en forma de tupla


def buscaEspec(elemento, cadena):
    for campo in campos:    #Buscar en los campos Nombre y Primer y Segundo Apellido
        if cadena.lower() in elemento[campo].lower():   #Si se encuentra la cadena deseada           
            despliega_uno(elemento)     #Mostrar todos los datos de ese alumno


def buscar(cadena):
    """Esta es la función Principal a llamar """
    for alumno in datos.alumnos:    #Para cada alumno registrado        
        buscaEspec(alumno, cadena)
