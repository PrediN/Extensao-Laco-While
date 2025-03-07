# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior.
# Em seguida, exiba quantos números foram inseridos.

# Declaração de variáveis

num = 0
anterior = -1
contador = 0

# Apresentação de resultados

while num != anterior:
    anterior = num
    num = int(input("Digite um número inteiro: "))
    contador += 1

print(f"Foram inseridos {contador-1} números.")