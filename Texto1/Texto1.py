#!/usr/bin/env python3

"""
Ejercicio 1: Texto1

nos ayuda a cambiar el estilo de cualquier oracion que escribamos en la terminal

Autor: Angel Rubio
Correo: angeluniversal69@gmail.com
Fecha: 04/05/2025
"""

def mostrar_menu():
    print("> Escriba 1 para pasar a minúsculas, ")
    print("          2 para pasar a mayúsculas, ")
    print("          3 para invertir mayúsculas y minúsculas ")
    print("          4 para pasar a capitalización.")
    print("          5 para pasar a titulación.")
    print("          6 para reemplazar espacios por guiones bajos.")
    print("          7 para salir.")

def transformar_texto(texto, opcion):
    if opcion == "1":
        return texto.lower()
    elif opcion == "2":
        return texto.upper()
    elif opcion == "3":
        return texto.swapcase()
    elif opcion == "4":
        return texto.capitalize()
    elif opcion == "5":
        return texto.title()
    elif opcion == "6":
        return texto.replace(" ", "_")
    else:
        return texto

def main():
    texto = input("> Ingrese la línea de texto:\n< ")

    while True:
        mostrar_menu()
        opcion = input("< ")

        if opcion == "7":
            print("> ¡Gracias!")
            break
        elif opcion in {"1", "2", "3", "4", "5", "6"}:
            texto = transformar_texto(texto, opcion)
            print(f"> Resultado: {texto}")
        else:
            print("> Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()