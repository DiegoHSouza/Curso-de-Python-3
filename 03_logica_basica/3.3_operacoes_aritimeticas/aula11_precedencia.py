
# Ordem de precedencia

# 1. (n + n)
# 2. **
# 3. */ // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # esperado 1024, real resultado 7
print(conta_1)

conta_1_correta = (1 + 1) ** (5 + 5)
print(conta_1_correta)