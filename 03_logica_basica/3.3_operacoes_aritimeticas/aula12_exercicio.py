nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc =  peso / (altura * altura)  # pode ser altura ** 2

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f} ')

# ... chama Ellipsis e permite compilar um codigo imcompleto sem que ele de erro