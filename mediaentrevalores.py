#Exercício 1. Escreva um programa que pede cinco números ao usuário e imprime o valor máximo, o valor mínimo e a média desses números.

#Interação com o usuário

n1, n2, n3, n4, n5 = input("Digite 5 números separados por espaço: ").split()

#Organizando a lista

lista = [n1, n2, n3, n4, n5]
print(f"\nOs números fornecidos foram: [{n1}, {n2}, {n3}, {n4}, {n5}]")

#Menor valor da lista
print(f"O menor valor é {min(lista)}")

#Maior valor da lista
print(f"O maior valor é {max(lista)}")

#Média
soma = float(n1) + float(n2) + float(n3) + float(n4) + float(n5)
media = soma/5
print(f"A média é {media}")
