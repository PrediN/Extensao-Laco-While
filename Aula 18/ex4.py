# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido.
# No final, exiba o maior número informado.

# Declaração de variáveis

num = 0
maior = 0

# Apresentação de resultados

while num >= 0:
    num = int(input("Digite um número inteiro(-1 para sair): "))

    if num > maior:
        maior = num

print(f"O maior número informado foi {maior}.")