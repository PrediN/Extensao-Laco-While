'''
8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba
o troco. Após isso, o programa deve reiniciar para um novo cliente.
'''

# Declaração de variáveis

total = 0
itens = 0
valor = -1
troco = 0
pagamento = 0

# Apresentação de resultados

while valor != 0:
    valor = float(input("Digite o valor do produto (0 para sair): "))
    
    if valor != 0:
        total += valor
        itens += 1
        print(f"Soma parcial: R$ {total:.2f}.")

pagamento = float(input("Digite o valor pago: "))
troco = pagamento - total

print(f"Total da compra: R$ {total:.2f}.")
print(f"Valor pago: R$ {pagamento:.2f}.")
print(f"Troco: R$ {troco:.2f}.")