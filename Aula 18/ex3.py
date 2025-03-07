# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o usuário digite -1.
# Em seguida, exiba a média das notas.

# Declaração de variáveis

contador = 0
soma = 0
nota = 0

# Apresentação de resultados

while nota != -1:
    nota = float(input("Digite uma nota (-1 para sair): "))
    
    if nota != -1:
        soma += nota
        contador += 1

media = soma / contador
print(f"A média das {contador} notas é {media:.2f}.")