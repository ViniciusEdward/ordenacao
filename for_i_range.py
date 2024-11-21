import os
os.system("cls || clear")

lista_for = []
for i in range(5):
    nome = input("Digite seu nome: ")
    lista_for.append(nome)

lista_organizadadnv = sorted(lista_for)
print(f"Lista organizada for: {lista_organizadadnv}")

