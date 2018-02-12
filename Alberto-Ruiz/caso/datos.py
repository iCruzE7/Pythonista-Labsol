#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""No son más que los registros
    ya establecidos en el código
    carrera y oden son tuplas
    campos en su dict
    alumnos es una lista"""
carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")

orden = ("Nombre", "Primer Apellido", "Segundo Apellido", "Carrera", "Semestre",
         "Promedio", "Al Corriente")

campos = {"Nombre": str, "Primer Apellido": str, "Segundo Apellido": str,
         "Carrera": str, "Semestre": int, "Promedio": float,
         "Al Corriente": bool}

alumnos = [{"Nombre":"Eduardo", "Primer Apellido": "Sánchez",
          "Segundo Apellido": "Ramos", "Carrera": "Sistemas",
          "Semestre": 6, "Promedio": 7.5, "Al Corriente": True},
          {"Nombre": "Alberto", "Primer Apellido": "Durán",
          "Segundo Apellido": "Montellano", "Carrera": "Derecho",
          "Semestre": 2, "Promedio": 6.3, "Al Corriente": True},
          {"Nombre": "Joaquín", "Primer Apellido": "Ausencio",
          "Segundo Apellido": "Olvera", "Carrera": "Actuaría",
          "Semestre": 2, "Promedio": 5.2, "Al Corriente": False},
          {"Nombre": "Emiliano", "Primer Apellido": "Rentería",
          "Segundo Apellido": "", "Carrera": "Administración",
          "Semestre": 4, "Promedio": 8.7, "Al Corriente": True},
          {"Nombre": "Patricio", "Primer Apellido": "Ayala",
          "Segundo Apellido": "Arriaga", "Carrera": "Sistemas",
          "Semestre": 5, "Promedio": 8.0, "Al Corriente": True}]
