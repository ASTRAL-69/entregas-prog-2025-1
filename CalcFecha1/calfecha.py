#!/usr/bin/env python3

"""
Ejercicio: calculadora de fechas



Autor: Angel Rubio
Correo: angeluniversal69@gmail.com
Fecha: 19/05/2025
"""

from datetime import datetime, timedelta

def main():
    while True:
        fecha_actual = datetime.now()
        print(f"\n> La fecha actual es: {fecha_actual}")

        print("> Escriba 1 para ingresar segundos,\n"
              "        2 para ingresar días,\n"
              "        3 para salir.")
        
        opcion = input("< ")
        
        if opcion == "1":
            print("> Escriba la cantidad de segundos")
            try:
                segundos = float(input("< "))
                nueva_fecha = fecha_actual + timedelta(seconds=segundos)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor, escriba un número válido.")

        elif opcion == "2":
            print("> Escriba la cantidad de días")
            try:
                dias = float(input("< "))
                nueva_fecha = fecha_actual + timedelta(days=dias)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor, escriba un número válido.")

        elif opcion == "3":
            print("> Gracias!")
            break
        else:
            print("> Opción inválida. Intente de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    main()