import os
os.system("cls || clear")

lista_nomes = []

# Entrada.
print("=== Solicitando dados para o usuário ===")
while True:
    nome = input("Digite seu nome: ")
    if nome.lower() == "sair":
        break
    else:
        lista_nomes.append(nome)
    
# Processamento.
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_nomes)

# Saída.
print("\n=== Resultado ===")
print(f"Lista original: {lista_nomes}")
print(f"\nLista ordenada: {lista_ordenada}")