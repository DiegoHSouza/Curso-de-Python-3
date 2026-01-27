from time import sleep

entrada = 0
while entrada != 'entrar' and entrada != 'sair':
    entrada = input('Você quer "entrar" ou "sair" ')

    if entrada == 'entrar':
        sleep: 2
        print('Usuário logado com sucesso')
    elif entrada == 'sair':
        sleep: 2
        print('Usuário deslogado com sucesso')
    else:
        sleep: 2
        print('Digite um comando correto')
if entrada == 'sair':
    sleep: 2
    print('Obrigado por usar nosso sistema')
else:
    sleep: 2
    print('Bem vindo')