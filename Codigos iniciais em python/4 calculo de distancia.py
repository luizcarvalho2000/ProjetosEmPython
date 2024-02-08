velocidade_carro = 110  # km/h
velocidade_caminhao = 80  # km/h
distancia_entre_cidades = 100  # km
distancia_pedagio = 10  # km
tempo_pedagio = 5  # minutos

# Ajusta a distância entre as cidades para levar em conta os pedágios
distancia_entre_cidades_ajustada = distancia_entre_cidades + (2 * distancia_pedagio)

# Calcula o tempo para o encontro
velocidade_relativa = velocidade_carro + velocidade_caminhao
tempo_para_encontro = distancia_entre_cidades_ajustada / velocidade_relativa

# Calcula a distância percorrida por cada veículo até o ponto de encontro
distancia_carro = velocidade_carro * tempo_para_encontro
distancia_caminhao = velocidade_caminhao * tempo_para_encontro

# Calcula a distância do carro até Ribeirão Preto
distancia_carro_rtp = distancia_entre_cidades - distancia_carro

# Verifica qual veículo está mais próximo de Ribeirão Preto
if distancia_carro_rtp < distancia_caminhao:
    print("O carro estará mais próximo de Ribeirão Preto.")
else:
    print("O caminhão estará mais próximo de Ribeirão Preto.")
