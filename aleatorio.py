import os, random
os.system("cls || clear")

lista = []
for i in range(10):
    numero_aleatorio = random.randrange(1, 100)
    lista.append(numero_aleatorio)

lista_organizada = sorted(lista)

print(f"Lista original: {lista}")

print(f"\nLista ordenada: {lista_organizada}")