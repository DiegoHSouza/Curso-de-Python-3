''' while/else '''
string = input('Digite um nome com ou sem espaços: ')

i = 0
while i<len(string):
    letra = string[i]
    if letra == '':
        break
    
    print(letra)
    i += 1
else:
    print('Não encontrei espaços')
print('Encontrei um espaço aqui')