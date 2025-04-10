#!/usr/bin/env python3

"""
taller: calculadora 1 basica

aqui ta

#autor: Angel Rubio
#correo: angeluniversal69@gmail.com
#fecha: 31/03/25
"""

def mostrar_menu():
    """Muestra el menú de operaciones disponibles."""
    print("> Cual operación se va a realizar?")
    print("> Escriba 1 para suma,")
    print(">         2 para resta,")
    print(">         3 para multiplicación")
    print(">         4 para división.")

def leer_operando(nombre):
    """Lee un operando desde la entrada del usuario, con validación.

    Args:
        nombre (str): El nombre del operando a mostrar ("A" o "B").

    Returns:
        float: El valor del operando.
    """
    while True:
        entrada = input(f"> Ingrese el operando {nombre}:<").strip()
        try:
            return float(entrada)
        except ValueError:
            print(f"> Dato inválido, por favor ingrese el operando {nombre}:")

def calcular(opcion, a, b):
    """Realiza el cálculo según la opción seleccionada.

    Args:
        opcion (int): Código de la operación.
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        float | str: Resultado de la operación o mensaje de error.
    """
    if opcion == 1:
        return a + b
    if opcion == 2:
        return a - b
    if opcion == 3:
        return a * b
    if opcion == 4:
        if b == 0:
            return "Error: División por cero"
        return a / b

def run():
    """Punto de entrada del script que ejecuta la calculadora básica."""
    a = leer_operando("A")
    b = leer_operando("B")

    mostrar_menu()
    try:
        opcion = int(input("< "))
    except ValueError:
        print("> Opción inválida")
        return

    if opcion < 1 or opcion > 4:
        print("> Opción inválida")
        return

    resultado = calcular(opcion, a, b)
    print(f"> El resultado es: {resultado}")

if __name__ == "__main__":
    run()
