import random
import time


def mudar_para_maiuscula(texto_entrada):
    return texto_entrada.upper()


def mudar_para_minuscula(texto_entrada):
    return texto_entrada.lower()


def gerar_numero_aleatorio():
    n = random.random()
    result = "X" + str(n) + "Y"
    return result


def calcular_idade(ano_nascimento):
    year, month, day, hour, min = map(
        int, time.strftime("%Y %m %d %H %M").split())
    idade = year - ano_nascimento
    return idade
