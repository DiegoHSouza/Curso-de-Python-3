'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if(ruim)

       <-  Contagem de complexidade (ruim)

'''


velocidade = 61 # velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local radar
RADAR_RANGE = 1 # distancia de detecção

above_speed_in_radar_1 = velocidade > RADAR_1
car_pass_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_RANGE) 
car_fined = car_pass_radar_1 and above_speed_in_radar_1

if above_speed_in_radar_1:
    print('Velocidade carro passou no radar 1')

if car_pass_radar_1:
    print('Carro passou no radar 1')
if car_fined:
    print('Carro multado')