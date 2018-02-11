#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Ejemplo de modulos en el curso de Python
Ejemplo de modulos en el curso de Python

importamos algunos .py de la carpeta casos
que son: altas.py, listado.py y datos.py

El ciclo while se repite hasta que demos un dato entero
el dato (int) se guarda en "alumnos"

Después hacemos un ciclo for que se itera de 0 a el valor int dado
en este for se van agregando elementos a el listado de alumnos
el listado se encuentra en datos.py

Nota que en al momento de hacer el append
llamamos a una función que se encuentra en altas.py
"""
import caso_nuevo.altas as altas
import caso_nuevo.archivos as archivos
import caso_nuevo.buscar as buscar

buscar.readFile("Alberto")

def principal():
    while True:
        try:
            alumnos = input("Número de alumnos:")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error)
            continue
        else:
            break
    for contador in range(alumnos):
        print("\nAlumno nuevo", contador + 1)
        archivos.agrega_uno(altas.alta())
    archivos.despliega_todos()

