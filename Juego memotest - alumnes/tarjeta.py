import pygame
from constantes import *


def crear_tarjeta(nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int) -> dict:
    tarjeta = { }

    tarjeta["ruta_imagen"] = CARPETA_RECURSOS + nombre_imagen
    tarjeta["imagen_cargada"] = pygame.image.load(tarjeta["ruta_imagen"])
    tarjeta["imagen_cargada"] = pygame.transform.scale(tarjeta["imagen_cargada"], (ANCHO_TARJETA, ALTO_TARJETA))
    tarjeta["superficie"] = pygame.Surface((ANCHO_TARJETA, ALTO_TARJETA))
    tarjeta["imagen_escondida"] = pygame.image.load(CARPETA_RECURSOS + nombre_imagen_escondida)
    tarjeta["identificador"] = identificador
    tarjeta["visible"] = False
    tarjeta["descubierto"] = False
    tarjeta["rectangulo"] = tarjeta["imagen_cargada"].get_rect(x, y)

    return tarjeta


def obtener_cantidad_tarjetas_por_estado(lista_tarjetas: list[dict], estado: bool) -> int:
    '''
        Obtiene la cantidad de tarjetas que esten visibles y que esten o no cubiertas
        Recibe la lista de tarjetas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
        Retorna dicha cantidad
    '''
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if (tarjeta["descubierto"] == estado and tarjeta["visible"]):
            cantidad += 1
    return cantidad


def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarme la bandera a las tarjetas a las que el usuario haya acertado en el memotest
        recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
        Uso una variable contador para evitar que el bucle se ejecute completo y ahorrar recursos si ya reemplazo a dos tarjetas no tiene sentido seguir iterando
    '''
    contador = 0
    for tarjeta in lista_tarjetas:
        if tarjeta["identificador"] == identificador and tarjeta["descubierto"] == False:
            tarjeta["descubierto"] = True
            contador += 1
        elif contador == 2:
            break
            