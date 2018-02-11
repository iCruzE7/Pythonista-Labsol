#! /usr/bin/python3
# -*-coding: utf-8 -*-
"""El primer condicional nos dice si
el espacio donde vamos a insertar el campo es
diferente de string, y si lo es
va a evaluar qué tipo de dato (además de str) va a ser guardado
Se va a asegurar de que los datos sean guardados
en los campos correctos"""

import caso.datos as datos
import caso.valida as valida



def alta():
    """Realiza las altas."""
    
    
    def ingresa(campo):
        while True:
            mensaje = "Ingrese " + campo.lower() + ": " 
            dato = input(mensaje)
            print("Este es el campo: " + campo.lower())
            if datos.campos[campo] != str:
                try:
                    if eval(dato) == datos.campos[campo](dato):
                        print("Este es el dato: " + dato)
                        """Imrpime todo lo que no sea str"""
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:
                    continue
            if valida.reglas(dato, campo):
                return dato
                  
    return {campo: ingresa(campo) for campo in datos.orden}
