"""
Dada uma lista de palavra, escreva um programa que receba um lista de frutas e mostra:
- a lista original
- a lista ordenada
- a lista na ordem inversa

caso o usuario digite sair, pare de solicitar dados.
"""

import os
os.system("cls || clear")

# Solicitando dados.
lista_frutas = []

while True:
    frutas = input("Digite nome de frutas: ")
    if frutas == "sair":
        break
    else:
        lista_frutas.append(frutas)

os.system("cls || clear")
# Lista original.
print(f"Lista original: {lista_frutas}")

# Modificando a lista.
lista_ordenada = sorted(lista_frutas)
print(f"\nLista ordenada: {lista_ordenada}")

# Lista inversa.
lista_inversa = lista_frutas[::-1]
print(f"\nLista inversa: {lista_inversa}")