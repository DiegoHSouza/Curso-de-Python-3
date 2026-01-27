primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é menor que o segundo valor {segundo_valor} ')
else:
    print(f'O primeiro valor {primeiro_valor} e o segundo valor {segundo_valor} são iguais')