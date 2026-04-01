nome = 'Diego Souza'
contador = 0
nova_string = '*'
while contador < len(nome):
    nova_string += nome[contador] + '*'
    print(f'{nome[contador]}')  
    contador += 1
    
print(nova_string)