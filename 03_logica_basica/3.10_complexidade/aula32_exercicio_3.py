nome = input('Digite seu primeiro nome: ')
try:
    curto = len(nome) <= 4
    normal = len(nome) >= 5 and len(nome) <= 6
    grande = len(nome) > 6
    
    if curto:
        print('Seu nome é curto')
    if normal:
        print('Seu nome é normal')
    if grande:
        print('Seu nome é grande')
except:
    print('Nome digitado invalido')