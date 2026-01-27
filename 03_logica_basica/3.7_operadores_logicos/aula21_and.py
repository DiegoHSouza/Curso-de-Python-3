"""
    Operadores lógicos
    and (e)
    or  (ou)
    not (não)
    
    
    and -  Todas as condições precisam ser verdadeiras
    
    se qualquer valor for considerado, falso a expressão inteira será avaliada naquele valor
    São consideradas falsy 
    
    0 0.0 '' False
    
    Também existe o ripo None que é usado para representar um não valor 

"""


entrada = input('Login: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
login_permitido = 'poldefacer'


if entrada == login_permitido and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
    
    
