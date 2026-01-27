"""
Operadores de comparação (Relacionais)

OP      Significado         Exemplo

>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'

"""
from itertools import batched

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a',
diferente = 'a' != 'b'


lista = [
         'Maior', maior, 
         'maior_ou_igual', maior_ou_igual,
         'menor', menor, 
         'Menor ou igual', menor_ou_igual,
         'Igual', igual, 
         'Diferente', diferente
         ]

for i in batched(lista, 2): 
    print(i)
    