# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados.
# O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

# Declaração de variáveis

qtd = 1
codigo = 0
total = 0
valor = 0

# Definição de produtos

produtos = {1: 4.5, 2: 5.0, 3: 3.5, 4: 2.0, 5: 5.5}

# Apresentação de resultados

print()
while qtd != 0:
    print()
    print("Produtos disponíveis:")
    print("1 - Cachorro-quente: R$ 4,50.")
    print("2 - X-Salada: R$ 5,00.")
    print("3 - Refrigerante: R$ 3,50.")
    print("4 - Batata frita: R$ 2,00.")
    print("5 - Milkshake: R$ 5,50.")
    print("0 - Finalizar pedido.")
    print()
    qtd = int(input("Digite a quantidade do produto (0 para sair): "))

    if qtd != 0:
        codigo = int(input("Digite o código do produto: "))
        valor = produtos[codigo] * qtd
        total += valor
        print(f"Valor parcial: R$ {valor:.2f}.")

print(f"Total do pedido: R$ {total:.2f}.")