#! /usr/bin/python3
# -*-coding: utf-8 -*-
"""El primer condicional nos dice si
el espacio donde vamos a insertar el campo es
diferente de string, y si lo es
va a evaluar qué tipo de dato (además de str) va a ser guardado
Se va a asegurar de que los datos sean guardados
en los campos correctos"""
import caso_nuevo.datos as datos
import caso_nuevo.valida as valida

def alta():
    """Realiza las altas."""
    
    
    def ingresa(campo):
        while True:
            mensaje = "Ingrese " + campo.lower() + ": " 
            dato = input(mensaje)
            if datos.campos[campo] != str:
                try:
                    if eval(dato) == datos.campos[campo](dato):
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:
                    continue
            if valida.reglas(dato, campo):
                return dato
                  
    return {campo: ingresa(campo) for campo in datos.orden}
