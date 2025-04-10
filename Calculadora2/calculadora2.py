#!/usr/bin/env python3

"""
taller: calculadora 2

aqui se cumplio con los requisitos necesarios

#autor: Angel Rubio
#correo: angeluniversal69@gmail.com
#fecha: 31/03/25
"""

def mostrar_menu():
    """Muestra el menú de operaciones disponibles."""
    print("> Escriba 1 para suma,")
    print(">         2 para resta,")
    print(">         3 para multiplicación")
    print(">         4 para división.")
    print(">         5 para potenciación.")
    print(">         6 para división entera.")
    print(">         7 para módulo.")
    print(">         8 para salir.")

def leer_operando(nombre):
    """Lee un operando desde la entrada del usuario, con validación.

    Args:
        nombre (str): El nombre del operando a mostrar ("A" o "B").

    Returns:
        float | None: El valor del operando o None si se cancela la operación.
    """
    while True:
        entrada = input(f"> Ingrese el operando {nombre} (vacío para cancelar):\n< ").strip()
        if entrada == "":
            print("> Operación cancelada")
            return None
        try:
            return float(entrada)
        except ValueError:
            print("> Dato inválido, por favor ingrese el operando", nombre + ":")

def calcular(opcion, a, b):
    """Realiza el cálculo según la opción seleccionada.

    Args:
        opcion (int): Código de la operación.
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        tuple: Resultado de la operación y descripción de la operación.
    """
    if opcion == 1:
        return a + b, "suma"
    if opcion == 2:
        return a - b, "resta"
    if opcion == 3:
        return a * b, "multiplicación"
    if opcion == 4:
        if b == 0:
            return None, "Error: División por cero"
        return a / b, "división"
    if opcion == 5:
        return a ** b, "potenciación"
    if opcion == 6:
        if b == 0:
            return None, "Error: División por cero"
        return a // b, "división entera"
    if opcion == 7:
        if b == 0:
            return None, "Error: División por cero"
        return a % b, "módulo"

def run():
    """Punto de entrada del script que ejecuta la calculadora."""
    while True:
        mostrar_menu()
        try:
            opcion = int(input("< "))
        except ValueError:
            print("> Opción inválida. Intente de nuevo.")
            continue

        if opcion == 8:
            print("> Gracias!")
            break
        if opcion < 1 or opcion > 8:
            print("> Opción inválida. Intente de nuevo.")
            continue

        a = leer_operando("A")
        if a is None:
            continue
        b = leer_operando("B")
        if b is None:
            continue

        resultado, descripcion = calcular(opcion, a, b)
        if resultado is None:
            print(">", descripcion)
        else:
            print(f"> El resultado de la {descripcion} es: {resultado}")

if __name__ == "__main__":
    run()
