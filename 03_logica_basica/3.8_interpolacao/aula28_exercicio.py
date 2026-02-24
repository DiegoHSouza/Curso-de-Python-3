nome = input('Digite seu nome: ' )
idade  = input('Digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome} e você tem {int(idade)} anos')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')    
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A Ultima letra do nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')