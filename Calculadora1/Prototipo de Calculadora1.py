#!/usr/bin/env python3

"""
#ejercicio 1= calculadora basica

este es un ejemplo de como usar las instrucciones basicas para usar python

#autor: Angel Rubio
#correo: angeluniversal69@gmail.com
#fecha: 20/02/25
"""

def run():
    """script entrypoint"""

#recopilar operandos
primerTermino = int(input("escriba un  numero entero: "))
segundoTermino = int(input("escriba otro  numero entero: "))

#hacer la operacion suma
resultadoSuma = primerTermino + segundoTermino

#hacer la operacion resta
resultadoResta = primerTermino - segundoTermino

#hacer la operacion multiplicacion
resultadoMultiplicacion = primerTermino * segundoTermino

#hacer la operacion division
resultadoDivision = primerTermino / segundoTermino

#hacer la operacion potenciacion
resultadoPotenciacionPrimerTermino = primerTermino **2

#hacer la operacion potenciacion
resultadoPotenciacionSegundoTermino = segundoTermino **2
#mostrar numero en pantalla
print (f"la suma de {primerTermino} y {segundoTermino} es {resultadoSuma}")

print (f"la resta de {primerTermino} y {segundoTermino} es {resultadoResta}")

print (f"la multiplicacion de {primerTermino} y {segundoTermino} es {resultadoMultiplicacion}")

print (f"la division de {primerTermino} y {segundoTermino} es {resultadoDivision}")

print (f"el cuadrado del primer termino {primerTermino}  {resultadoPotenciacionPrimerTermino}")

print (f"el cuadrado del segundo termino  {segundoTermino} es {resultadoPotenciacionSegundoTermino}")

if __name__ == "__main__":
    run()
