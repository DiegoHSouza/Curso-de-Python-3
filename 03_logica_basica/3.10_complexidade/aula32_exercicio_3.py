nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)


if nome.isalpha():
    
    if tamanho_nome <=4:
        print('Seu nome é curto!')
    elif 5 <= tamanho_nome <=6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é grande!')

else:
    print('Digite apenas letras!')