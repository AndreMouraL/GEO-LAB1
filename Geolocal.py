import random
import phonenumbers
from opencage.geocoder import OpenCageGeocode
import ipyleaflet
from IPython.display import display
from ipywidgets import Button

# Substitua 'SUA_CHAVE_AQUI' pela chave de API fornecida pelo OpenCage.
SUA_CHAVE_AQUI = 'SUA_CHAVE_AQUI'

geocoder = OpenCageGeocode(SUA_CHAVE_AQUI)

def autorizacao_operadora(numero):
    # Em uma aplicação real, você pode realizar verificações de autorização reais aqui.
    return True

def consultar_localizacao(numero):
    if autorizacao_operadora(numero):
        # Simulando uma localização aleatória para fins de demonstração.
        latitude = random.uniform(-35, 5)  # Faixa de latitude para o Brasil
        longitude = random.uniform(-75, -35)  # Faixa de longitude para o Brasil
        return latitude, longitude
    else:
        return None

def obter_detalhes_localizacao(latitude, longitude):
    try:
        result = geocoder.reverse((latitude, longitude), language="pt-BR")
        address = result[0]['formatted']
        return address
    except:
        return None

def criar_mapa(coordenadas):
    mapa = ipyleaflet.Map(center=coordenadas, zoom=10)
    return mapa

def exibir_mapa(mapa):
    display(mapa)

def localizar_por_numero(numero):
    coordenadas = consultar_localizacao(numero)

    if coordenadas:
        endereco = obter_detalhes_localizacao(*coordenadas)

        if endereco:
            print(f"Localização encontrada: {coordenadas}")
            print(f"Endereço: {endereco}")

            mapa = criar_mapa(coordenadas)
            exibir_mapa(mapa)

            print("Clique no botão 'Atualizar' para obter a localização em tempo real.")
            botao_atualizar = Button(description="Atualizar")
            botao_atualizar.on_click(lambda btn: atualizar_localizacao(mapa, numero))
            display(botao_atualizar)
        else:
            print("Não foi possível obter detalhes de endereço.")
    else:
        print("Não foi possível determinar a localização")

def atualizar_localizacao(mapa, numero):
    coordenadas = consultar_localizacao(numero)

    if coordenadas:
        endereco = obter_detalhes_localizacao(*coordenadas)

        if endereco:
            print(f"Localização atualizada: {coordenadas}")
            print(f"Endereço: {endereco}")

            mapa.center = coordenadas
        else:
            print("Não foi possível obter detalhes de endereço.")
    else:
        print("Não foi possível determinar a localização")

numero_alvo = '+55 66 996591926'
localizar_por_numero(numero_alvo)
