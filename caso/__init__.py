#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Ejemplo de modulos en el curso de Python"""
import caso.altas as altas
import caso.listado as listado
import caso.datos as datos

def principal():
    while True:	#ciclo infinito
        try:
            alumnos = input("Número de alumnos:")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error)
            continue	# Vuelve a ejecutar el ciclo y pide el número de alumnos
        else:	# no se genera la excepción
            break	# Rompe el while y entra al for
    for contador in range(alumnos):	# 0 < alumnos
        print("\nAlumno nuevo", contador + 1)
        datos.alumnos.append(altas.alta())
    listado.despliega_todos()
