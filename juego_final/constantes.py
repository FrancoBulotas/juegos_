import pygame
import pyautogui

ANCHO_PANTALLA, ALTO_PANTALLA = pyautogui.size()

# ANCHO_PANTALLA = 1200
# ALTO_PANTALLA = 885

ANCHO_PERSONAJE = 100
ALTO_PERSONAJE = 50
ANCHO_MUNICION = 50
ALTO_MUNICION = 20

ALTURA_MENU_SUPERIOR = 80

VELOCIDAD_PERSONAJE = 8
VELOCIDAD_MISIL = 5
VELOCIDAD_NAVE_ALIEN = 4
VIDAS_PERSONAJE = 3
VIDA_MISIL = 2
VIDAS_NAVE_ALIEN_VIOLETA = 10
VIDAS_ALIEN = 1
MUNICION_PERSONAJE = 15
MUNICION_POR_BALAS_EXTRA = 5
MUNICION_POR_BALAS_EXTRA_MEJORADA = 3

TIEMPO_NIVEL = 60
CANTIDAD_MISILES_NIVEL_UN0 = 10
CANTIDAD_BALAS_EXTRA = 3
CANTIDAD_BALAS_EXTRA_MEJORADAS = 2
CANTIDAD_VIDAS_EXTRA = 1

PANTALLA_JUEGO = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
RECURSOS = "recursos\\"

# Puntuaciones
PUNTOS_POR_MISIL = 50
PUNTOS_POR_ALIEN = 25
PUNTOS_POR_NAVE_ALIEN = 300


