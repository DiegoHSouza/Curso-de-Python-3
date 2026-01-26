
usuarios = []
novo_usuario = True


while novo_usuario == True :
    
    nome =  str(input('Qual é o seu nome?: '))
    sobrenome = str(input('Qual é o seu Sobrenome?: '))
    idade = int(input('Qual é a sua idade?: '))
    ano_nascimento = int(input('Qual ano você nasceu?: '))
    altura_metros = float(input('Qual sua altura em metros?: '))
    if idade >= 18:
        maior_de_idade = 'é'
    else:
        maior_de_idade = 'não é'
    print(f'O Usuario se chama {nome} {sobrenome}, tem {idade} anos e mede {altura_metros}, ele {maior_de_idade} maior de idade.')
    
    usuario = {'nome': nome, 'idade': idade, 'altura': altura_metros}
    usuarios.append(usuario)
    
    continuar = int(input('digite:\n [1] para novo Usuario\n [2] Para encerrar e exibir todos: \n'))
    if continuar == 2:
        novo_usuario = False
        
print(usuarios)