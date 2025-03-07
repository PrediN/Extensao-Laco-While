# 6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.

# Declaração de variáveis

nota = -1

# Apresentação de resultados

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

print(f"A nota digitada foi {nota}.")