#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Imprime lso registro ya seatodo o de uno en uno"""

import caso.datos as datos


def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))


def despliega_todos():
    contador = 0
    for alumno in datos.alumnos:
        contador += 1
        print("\nAlumno: ", contador)
        despliega_uno(alumno)