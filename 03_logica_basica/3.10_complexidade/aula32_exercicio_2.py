horas = input('Que horas são?: ')

try:
    horas_numero = int(horas)
    manha = 0 <= horas_numero <= 11
    tarde = horas_numero >= 12 and horas_numero <=17
    noite = horas_numero >= 18 and horas_numero <=23

    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite')
    else:
        print('Digite um horario valido!')
except:
    print('Valor inserido invalido')
    