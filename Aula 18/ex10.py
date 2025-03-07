# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo (5) ou branco (6).
# O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. A entrada 0 encerra a votação.

# Declaração de variáveis

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
voto = -1
total = 0
porcBrancos = 0
porcNulos = 0

# Apresentação de resultados

while voto != 0:
    print()
    print("1 - Candidato 1.")
    print("2 - Candidato 2.")
    print("3 - Candidato 3.")
    print("4 - Candidato 4.")
    print("5 - Nulo.")
    print("6 - Branco.")
    print("0 - Encerrar votação.")
    print()
    voto = int(input("Digite o número do candidato (0 para encerrar): "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    elif voto == 0:
        break
    else:
        print("Voto inválido.")

    total += 1

porcNulos = (nulo / total) * 100
porcBrancos = (branco / total) * 100

print()
print("Resultado da votação:")
print(f"Candidato 1: {candidato1} votos.")
print(f"Candidato 2: {candidato2} votos.")
print(f"Candidato 3: {candidato3} votos.")
print(f"Candidato 4: {candidato4} votos.")
print(f"Votos nulos: {nulo} votos ({porcNulos:.2f}%).")
print(f"Votos brancos: {branco} votos ({porcBrancos:.2f}%).")
print(f"Total de votos: {total} votos.")