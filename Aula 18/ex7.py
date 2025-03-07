# 7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B com 200.000 habitantes e taxa de 1,5%.
# Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.

# Declaração de variáveis

paisA = 80000
paisB = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0

# Apresentação de resultados

while paisA < paisB:
    paisA += paisA * taxaA
    paisB += paisB * taxaB
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")
print(f"País A: {paisA:,.0f} habitantes.")
print(f"País B: {paisB:,.0f} habitantes.")