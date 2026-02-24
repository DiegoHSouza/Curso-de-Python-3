numero_usuario = input('Digite um número inteiro: ')

try:
    numero_convertido = float(numero_usuario)
    par = numero_convertido % 2 == 0
    inteiro = numero_convertido.is_integer()

    if inteiro:
        if par:
            print(f'O número {numero_convertido:.0f} é par')
        else:
            print(f'O número {numero_convertido:.0f} é impar')
    else:
        print('O número não é inteiro')
except:
    print(f' "{numero_usuario}" não é um número')