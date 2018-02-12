#! /usr/bin/python3
# -*- coding: utf-8 -*-

#El valor de ruta es la ruta donde se encuentra el archivo datos.txt
#Ejemplo en Windows: "C:\Users\Josech\Documentos\Python\datos.txt"

"la lista de alumnos se encuentra en el .txt"

ruta = "caso_nuevo/alumnos.txt"

orden = ("Nombre", "Primer Apellido", "Segundo Apellido", "Carrera",
"Semestre", "Promedio", "Al Corriente")

campos = {"Nombre": str, "Primer Apellido": str, "Segundo Apellido": str,
         "Carrera": str, "Semestre": int, "Promedio": float,
         "Al Corriente": bool}

carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura",
    "Administración")