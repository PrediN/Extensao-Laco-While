'''
1. Escreva um programa que leia um número N e imprima todos os termos da sequência de
Fibonacci até que o maior termo seja menor ou igual a N.
Exemplo:
 Entrada: 20
 Saída: 0 1 1 2 3 5 8 13
'''

# Declaração de variáveis

n = 0
a = 0
b = 1
c = 0

# Apresentação de resultados
n = int(input("Digite um número: "))

while c <= n:
    print(c, end=', ')
    c = a + b
    a = b
    b = c