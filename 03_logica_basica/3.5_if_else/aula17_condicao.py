
senha = False



while senha != True:
    
    senha_digitada = input('Digite a senha de 4 dígitos: ')
    senha_digitada_int = int(senha_digitada)
    senha_real = 3580
    
    if senha_digitada_int == senha_real:
        print('Usuário logado com sucesso! ')
        senha = True
    else:
        print('Senha incorreta! ')    
    