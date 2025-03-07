'''
3. Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.
Exemplo:
 Entrada: 98765
 Saída: O número 98765 tem 5 dígitos
'''

# Declaração de variáveis

num = str(input("Digite um número: "))
cont = 0

# Apresentação de resultados

for i in num:
    cont += 1

print(f"O número {num} tem {cont} dígitos")