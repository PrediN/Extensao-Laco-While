'''
4. Escreva um programa que leia um número inteiro positivo e determine se ele é um número
perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
mesmo) é igual ao próprio número.
Exemplo:
 Entrada: 28
 Cálculo: 1 + 2 + 4 + 7 + 14 = 28
 Saída: 28 é um número perfeito
'''

# Declaração de variáveis

num = int(input("Digite um número positivo: "))
soma = 0
listaNum = []
contador = 0

# Apresentação de resultados


while contador < num-1: # Cálculo dos divisores próprios
    contador += 1
    if num % contador == 0:
        listaNum.append(contador)

for i in listaNum: # Soma dos divisores próprios
    soma += i

for j in listaNum: # Imprimir a lista de divisores próprios
    print(j, end=' ')

print()

if soma == num: # Verificação se o número é perfeito
    print(f"O número {num} é perfeito!")

else:
    print("O número não é perfeito!")