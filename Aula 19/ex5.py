'''
5. Escreva um programa que leia um número inteiro positivo e determine se ele é um
quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).
Exemplo:
 Entrada: 49
 Cálculo: 7 × 7 = 49
 Saída: 49 é um quadrado perfeito
'''

# Declaração de variáveis

num = int(input("Digite um número inteiro positivo: "))
contador = 0

# Apresentação de resultados

while contador**2 < num: # Cálculo do quadrado perfeito
    contador += 1

if contador**2 == num: # Verificação se o número é um quadrado perfeito
    print(f"O número {num} é um quadrado perfeito! Sua raiz quadrada é {contador}.")

else:
    print(f"O número {num} não é um quadrado perfeito!")