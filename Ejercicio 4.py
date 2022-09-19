# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:14:11 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def calcularBinario(numero):
    numBinario = ""  # La variable 'numBinario' es inicializada como un string vacío, en esta variable se guardará el valor ingresado en binario
    while numero >= 1:  # Mientras 'numero' sea mayor o igual que 1, el ciclo continua
        if (numero % 2 == 0):  # Si el resto (%) de 'numero' entre 2  es igual a 0
            numBinario += "0"  # Se agrega un 0 al string y se guarda en 'numBinario'
            # Continúa la conversión, dividiendo 'numero' entre 2 y obteniendo la parte entera
            numero = numero // 2
        else:  # Si el resto (%) de 'numero' entre 2 NO es igual a 0 (distinto)
            numBinario += "1"  # Se agrega un 1 al string y se guarda en 'numBinario'
            # Continúa la conversión, diviendo 'numero' entre 2 y obteniendo la parte entera
            numero = numero // 2
    # Entregamos el valor convertido a binario.
    return "".join(reversed(numBinario))


# Programa principal, se pide al usuario un número para convertir
numero = int(input("Ingrese un número para calcular en binario: "))
# Se le entrega a la función el valor ingresado anteriormente y se guarda en 'binario'
binario = calcularBinario(numero)

# Se entrega el resultado en pantalla
print(f"El número {numero} en binario es '{binario}'")
