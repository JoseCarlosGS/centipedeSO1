"""Nombre: ProyectoSO1
    Autor: Jose Carlos Giron Solano
    Año: 2024
    """

import pygame
import sys
import time

from cola import PCB, cola

canon = PCB()
Q = cola()
head = PCB()

#Tipos
CENTIPEDE = 0
BALA = 1

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Cañón Sencillo")

#inicialiar variables
    # Configuración del cañón
ANCHO_CANON = 50
ALTO_CANON = 20
canon_color = (255, 0, 0)  # Rojo
canon_pos_x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
canon_pos_y = ALTO_PANTALLA - ALTO_CANON - 10
velocidad = 5

canon.x = canon_pos_x
canon.y = canon_pos_y
canon.Alto = ALTO_CANON
canon.Ancho = ANCHO_CANON
canon.Color = canon_color 

#head del cienpies
head.Tipo = CENTIPEDE
head.Ancho= 50
head.Alto  = 20
head.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
head.y = 10
head.Color = canon_color
head.Hora = int(time.time() * 1000);
head.Retardo = 50;  

Q.meter(head)

# Funciones
def dibujar(objeto):
    pygame.draw.rect(pantalla, objeto.Color, (objeto.x, objeto.y, objeto.Ancho, objeto.Alto))

def moverNave(prun):
    #print(f'Moviendo nave: {prun}')
    prun.x -= 5
    prun.Hora = int(time.time() * 1000);
    Q.meter(prun)

def moverBalaU(prun):
    print(f'Moviendo bala U: {prun}')

def moverBalaN(prun):
    print(f'Moviendo bala N: {prun}')
    
def planificador():
    PRUN = Q.sacar()
    #print(PRUN)
    if PRUN is None:
        return

    current_time_ms = int(time.time() * 1000)  # Convertir tiempo a milisegundos

    if PRUN.Hora + PRUN.Retardo > current_time_ms:
        Q.meter(PRUN)
    else:
        if PRUN.Tipo == CENTIPEDE:
            moverNave(PRUN)
        elif PRUN.Tipo == "BALAU":
            moverBalaU(PRUN)
        elif PRUN.Tipo == "BALAN":
            moverBalaN(PRUN)

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and canon_pos_x > 0:
        canon.x -= velocidad
    if teclas[pygame.K_RIGHT] and canon_pos_x < ANCHO_PANTALLA - ANCHO_CANON:
        canon.x += velocidad

    # Dibujar en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar la pantalla con color negro
    dibujar(canon)
    dibujar(head)
    
    #Ejecutar planificador
    planificador()
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()

