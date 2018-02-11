#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""agrega_uno hace append al txt, agrega el registro
despliega_todos hace read del .txt
para después mostrartodo"""

import caso_nuevo.datos as datos


def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))

        
def despliega_todos(ruta=datos.ruta):
    with open(ruta, 'r') as archivo:
        contador = 0
        for alumno in archivo:
            alumno = eval(alumno)
            contador += 1
            print("\nAlumno: ", contador)
            despliega_uno(alumno)
        
        
def agrega_uno(elemento, ruta=datos.ruta):
    with open(ruta, 'a') as archivo:
        archivo.write(str(elemento) + '\n')