'''

documentação python: https://docs.python.org/pt-br/3/
Imutáveis que vimos: str, int, float, bool
todos são objetos, e por isso existem métodos que podem ser utilizados
cada tipo de objeto, tem seus métodos
'''

string = 'diego Souza'
outra_variavel = f'{string[:3]}'
# string[3] = 'ABC' <- não funciona pois a string é uma variavél imutável
print(outra_variavel)
print(string.capitalize())