#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso.datos as datos
import caso.valida as valida
"""Módulo que contiene la funcion de altas."""

def alta():
    """Realiza las altas."""
        
    def ingresa(campo):
        """Recibe como argumento el identificador de datos.orden"""
        while True:
            mensaje = "Ingrese " + campo.lower() + ": " 
            dato = input(mensaje)
            if datos.campos[campo] != str:  #Si no se está solicitando un String
                try:
                    #Si el dato ingresado es del tipo esperado
                    if eval(dato) == datos.campos[campo](dato): 
                        dato = datos.campos[campo](dato)
                    else:
                        continue    #Vuelve al while a solicitar el dato
                except:
                    continue    #Vuelve al while a solicitar el dato
            if valida.reglas(dato, campo):  #si la info ingresada es válida
                return dato
	#(Completado de Elementos) Solicita los 7 campos (llama la función "ingresa") 
	#uno por vez que debe contener cada alumno y los Retorna para que se haga el #append                  
    return {campo: ingresa(campo) for campo in datos.orden} 
