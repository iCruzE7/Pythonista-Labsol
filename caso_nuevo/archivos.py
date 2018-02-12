#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso_nuevo.datos as datos


def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))

        
def despliega_todos(ruta=datos.ruta):
    with open(ruta, 'r') as archivo:    #'r' para modo lectura y cierre automáticamente al archivo
        contador = 0
        for alumno in archivo:
            alumno = eval(alumno)
            contador += 1
            print("\nAlumno: ", contador)
            despliega_uno(alumno)
        
        
def agrega_uno(elemento, ruta=datos.ruta):
    with open(ruta, 'a') as archivo:        #'a' para escribir al final del archivo y cierre automáticamente al archivo
        archivo.write(str(elemento) + '\n')
