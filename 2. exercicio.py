"""
Dada uma lista de palavra, escreva um programa que receba um lista de frutas e mostra:
- a lista original
- a lista ordenada
- a lista na ordem inversa

caso o usuario digite sair, pare de solicitar dados.

refatorando codigo:
crie uma função para:
- ordenação
- ordenação na ordem inversa
"""

import os
os.system("cls || clear")

# Solicitando dados.
lista_frutas = []

def ordenação(n1):
    lista_ordenada = sorted(n1)
    print(f"\nLista ordenada: {lista_ordenada}")

def ordenação_inversa(n1):
    lista_ordenada = sorted(n1)
    lista_ordenada.reverse()
    print(f"\nLista ordenada inversa: {lista_ordenada}")

while True:
    frutas = input("Digite nome de frutas: ")
    if frutas == "sair":
        break
    else:
        lista_frutas.append(frutas)

os.system("cls || clear")
# Lista original.
print(f"Lista original: {lista_frutas}")

# Ordenação.
ordenação(lista_frutas)

# Ordenação inversa.
ordenação_inversa(lista_frutas)

# Lista inversa.
lista_inversa = lista_frutas[::-1]
print(f"\nLista inversa: {lista_inversa}")