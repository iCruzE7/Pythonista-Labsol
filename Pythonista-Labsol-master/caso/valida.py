#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""script valida
valida se comunica con altas
altas vuelve a pedir el valor si se retorna false
una vez regrese true, pide el valor que sigue"""

import caso.datos as datos

def reglas(dato, campo):
    if campo == "Carrera" and dato not in datos.carreras:
        return False
    elif campo == "Semestre" and dato < 1:
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10):
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")):
        return False
    elif campo == "Segundo Apellido" and dato == "":
        while True:
            mensaje = "No ha ingresado el segundo apellido. ¿Es correcto? S/N: "
            confirma = input(mensaje)
            if confirma.upper() in ("S", "N"):
                respuesta = True
                if confirma.upper() == "N":
                    respuesta = False
                return respuesta
    else:
        return True
