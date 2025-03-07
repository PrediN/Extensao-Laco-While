'''
2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
palíndromo (ou seja, se lido de trás para frente continua igual).
Exemplo:
 Entrada: 1221
 Saída: 1221 é um número palíndromo
'''

# Declaração de variáveis

num = str(input("Digite um número: "))
num1 = num[::-1]

# Apresentação de resultados

if num == num1:
    print(f"{num} é um número palíndromo")

else:
    print(f"{num} não é um número palíndromo")