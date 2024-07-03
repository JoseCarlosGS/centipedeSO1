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
body1 = PCB()
body2 = PCB()
body3 = PCB()
body4 = PCB()
HoraAbs = int(time.time() * 1000)
id = 0

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
head.Ancho= 20
head.Alto  = 20
head.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
head.y = 10
head.Color = canon_color
head.Hora = int(time.time() * 1000)
head.Retardo = 30
head.Dir = 0 

Q.meter(head)
#Cuerpo del cienpiez
body1.Tipo = CENTIPEDE
body1.Ancho= 20
body1.Alto  = 20
body1.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 20
body1.y = 10
body1.Color = canon_color
body1.Hora = int(time.time() * 1000)
body1.Retardo = 30
body1.Dir = 0 
Q.meter(body1)

body2.Tipo = CENTIPEDE
body2.Ancho= 20
body2.Alto  = 20
body2.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 40
body2.y = 10
body2.Color = canon_color
body2.Hora = int(time.time() * 1000)
body2.Retardo = 30
body2.Dir = 0 
Q.meter(body2)

# body3.Tipo = CENTIPEDE
# body3.Ancho= 20
# body3.Alto  = 20
# body3.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 60
# body3.y = 10
# body3.Color = canon_color
# body3.Hora = int(time.time() * 1000)
# body3.Retardo = 30
# body3.Dir = 0 
# Q.meter(body3)


# Funciones
def dibujar(objeto):
    pygame.draw.rect(pantalla, objeto.Color, (objeto.x, objeto.y, objeto.Ancho, objeto.Alto))
    
def cambiarDir(objeto):
    if objeto.Dir == 0:
        objeto.Dir = 1
    elif objeto.Dir == 1:
        objeto.Dir = 0

def moverNave(prun):
    if prun.x < 0:
        cambiarDir(prun)
        prun.y = prun.y + prun.Alto
    elif prun.x > ANCHO_PANTALLA - prun.Ancho:
        cambiarDir(prun)
        prun.y = prun.y + prun.Alto
    if prun.Dir == 0:
        vel = 5
    elif prun.Dir == 1:
        vel = -5
    
    prun.x -= vel
    prun.Hora = int(time.time() * 1000);
    Q.meter(prun)

def moverBalaU(prun):
    #print(f'Moviendo bala U: {prun}')
    prun.y = prun.y -5
    if prun.y > 0:
        #dibujar(prun)
        prun.Hora = int(time.time() * 1000)
        Q.meter(prun)

def moverBalaN(prun):
    print(f'Moviendo bala N: {prun}')
    
def crearBala():
    global id
    BalaUser = PCB()
    BalaUser.PID = id
    BalaUser.Tipo  = BALA
    BalaUser.Ancho = 5
    BalaUser.Alto  = 10
    BalaUser.Color = (255, 0, 0)  # Rojo
    BalaUser.x = (canon.Ancho - BalaUser.Ancho) // 2 + canon.x
    BalaUser.y = canon.y - BalaUser.Alto
    BalaUser.Retardo = 5
    BalaUser.Hora = HoraAbs
    #BalaUser.Hora = int(time.time() * 1000)
    dibujar(BalaUser)

    Q.meter(BalaUser)
    id += 1             

    
    
def planificador():
    PRUN = Q.sacar()
    #print(PRUN)
    if PRUN is None:
        return

    current_time_ms = int(time.time() * 1000)  # Convertir tiempo a milisegundos

    if PRUN.Hora + PRUN.Retardo > current_time_ms:
        Q.meter(PRUN)
        #print('aun hay quamtum')
    else:
        #print('se acabo quantum')
        if PRUN.Tipo == CENTIPEDE:
            moverNave(PRUN)
        elif PRUN.Tipo == BALA:
            moverBalaU(PRUN)
        elif PRUN.Tipo == "BALAN":
            moverBalaN(PRUN)

# Bucle principal del juego
corriendo = True
sw = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and canon.x > 0:
        canon.x -= velocidad
    if teclas[pygame.K_RIGHT] and canon.x < ANCHO_PANTALLA - ANCHO_CANON:
        canon.x += velocidad
    if teclas[pygame.K_SPACE]:
        #print('detectado tab')
        crearBala()

    # Dibujar en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar la pantalla con color negro
    dibujar(canon)
    
    for dibujo in Q:
        dibujar(dibujo)
    
    #dibujar(Q.first())

    
    #Ejecutar planificador
    planificador()
    # print(Q.last())
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    pygame.time.Clock().tick(100)

# Salir de Pygame
pygame.quit()
sys.exit()

