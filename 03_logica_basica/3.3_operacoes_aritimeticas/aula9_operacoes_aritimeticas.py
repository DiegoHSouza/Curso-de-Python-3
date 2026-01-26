adicao = 10 + 10
print(adicao)


subtracao = 10 - 10
print(subtracao)

multiplicacao = 10 * 10
print(multiplicacao)


divisao = 10 / 2.2 
print(divisao)


divisao_inteira = 10 // 2.2
print(divisao_inteira)

exponenciacao = 2 ** 10
print(exponenciacao)

modulo = 55 % 2 # resto da divisão
print(modulo)


numero = int(input('Digite um número inteiro e descubra se ele é par ou ímpar : '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')