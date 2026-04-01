"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

"""

pessoas = []
continuar = True

while continuar:
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    
    pessoa = nome, idade
    
    pessoas.append(pessoa)
    
    continuar = input('Deseja continuar? [S] ou [N]').lower()
    
    if continuar != 's':
        continuar = False
        
print(pessoas)
    
    
    