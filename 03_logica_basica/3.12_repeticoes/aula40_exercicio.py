while True:
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite o operador (+-/*): ')
        
    numeros_validos = None 
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Digitos invalidos')
        continue
    
    
    operadores_permitidos = '+-/*'
    
    if operador  not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    elif len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    if operador == '+':
        resultado = num_1_float + num_2_float
    
    elif operador == '-':
        resultado = num_1_float - num_2_float
    
    elif operador == '/':
        resultado = num_1_float / num_2_float
    
    elif operador == '*':
        resultado = num_1_float * num_2_float
    
    print(f'o resultado de {num_1_float} {operador} {num_2_float} = {resultado}')    
    
    
    sair = input('Quer sair? [S]IM:  ').lower().startswith('s')
    if sair:
        break