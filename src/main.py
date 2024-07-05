"""Nombre: ProyectoSO1
    Autor: Jose Carlos Giron Solano
    Año: 2024
    """

import pygame
import sys
import time
import random as rd

from cola import PCB, cola

#Declaracion de variables globales
canon = PCB()
Q = cola()
head = PCB()
body1 = PCB()
body2 = PCB()
body3 = PCB()
body4 = PCB()
RetardoCentipede = 1
id = 0
Clred = (255, 0, 0)
Clyellow = (255, 255, 0)
Clgreen = (0, 255, 0)
Clwhite = (255, 255, 255)

#Tipos
CENTIPEDE = 0
BALA = 1
OBSTACULO = 2

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Cañón Sencillo")


# Crear un pool de objetos PCB
pool_size = 200  # Ajustar según sea necesario
pcb_pool = [PCB() for _ in range(pool_size)]
free_pcb_indices = list(range(pool_size))

   


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
head.Hora = pygame.time.get_ticks()
head.Retardo = RetardoCentipede
head.Dir = 0 
Q.meter(head)

#Cuerpo del cienpies
body1.Tipo = CENTIPEDE
body1.Ancho= 20
body1.Alto  = 20
body1.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 40
body1.y = 10
body1.Color = canon_color
body1.Hora = pygame.time.get_ticks()
body1.Retardo = RetardoCentipede
body1.Dir = 0 
Q.meter(body1)

body2.Tipo = CENTIPEDE
body2.Ancho= 20
body2.Alto  = 20
body2.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 80
body2.y = 10
body2.Color = canon_color
body2.Hora = pygame.time.get_ticks()
body2.Retardo = RetardoCentipede
body2.Dir = 0            
Q.meter(body2)

body3.Tipo = CENTIPEDE
body3.Ancho= 20
body3.Alto  = 20
body3.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 120
body3.y = 10
body3.Color = canon_color
body3.Hora = pygame.time.get_ticks()
body3.Retardo = RetardoCentipede
body3.Dir = 0 
Q.meter(body3)

body4.Tipo = CENTIPEDE
body4.Ancho= 20
body4.Alto  = 20
body4.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + 160
body4.y = 10
body4.Color = canon_color
body4.Hora = pygame.time.get_ticks()
body4.Retardo = RetardoCentipede
body4.Dir = 0            
Q.meter(body4)

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
obstaculos = [PCB() for _ in range(20)]
for obstaculo in obstaculos:
    obstaculo.Color = Clwhite
    obstaculo.Alto = head.Alto
    obstaculo.Ancho = head.Ancho
    obstaculo.x = rd.randint(0,500)
    obstaculo.y = rd.choice(range(10, 500 + 1, 20))
    obstaculo.Salud = 4
    obstaculo.Tipo = OBSTACULO
    #print(obstaculo)

# Funciones
def CambiarColor(objeto):
    if objeto.Salud == 1:
        objeto.Color = Clgreen
        
def obtener_pcb_del_pool():
    if free_pcb_indices:
        return free_pcb_indices.pop()
    else:
        return None

def devolver_pcb_al_pool(indice):
    free_pcb_indices.append(indice)
    
def crear_rect(objeto):
    return pygame.Rect(objeto.x, objeto.y, objeto.Ancho, objeto.Alto)

def dibujar(objeto):
    # Detección de colisión para la bala con cualquier otro objeto
    pygame.draw.rect(pantalla, objeto.Color, (objeto.x, objeto.y, objeto.Ancho, objeto.Alto))
    
def cambiarDir(objeto):
    if objeto.Dir == 0:
        objeto.Dir = 1
    elif objeto.Dir == 1:
        objeto.Dir = 0

def moverNave(prun):
    #print('centipede')
    if prun.x < 0:
        cambiarDir(prun)
        prun.y = prun.y + prun.Alto
    elif prun.x > ANCHO_PANTALLA - prun.Ancho:
        cambiarDir(prun)
        prun.y = prun.y + prun.Alto
    
    # Detectar choque con obstaculos
    rect_gus = crear_rect(prun)
    for obstaculo in obstaculos:
        rect_objeto = crear_rect(obstaculo)
        if rect_gus.colliderect(rect_objeto):
            #print("¡Colisión detectada con un objeto!")
            cambiarDir(prun)
            prun.y = prun.y + prun.Alto
    
    if prun.Dir == 0:
        vel = 10
    elif prun.Dir == 1:
        vel = -10
    
    prun.x -= vel
    prun.Hora = pygame.time.get_ticks()
    #print(prun.Hora)
    if prun.Salud > 0:
        Q.meter(prun)
    else:
        nobstaculo = PCB()
        nobstaculo = prun
        nobstaculo.Salud = 4
        nobstaculo.Tipo = OBSTACULO
        obstaculos.append(nobstaculo)
        

def moverBalaU(prun):
    #print('bala')
    #print(f'Moviendo bala U: {prun}')
    prun.y = prun.y -15
    # Detectar colision con el cienpies
    rect_bala = crear_rect(prun)
    for gusano in Q:
        if gusano.Tipo != BALA:
            rect_objeto = crear_rect(gusano)
            if rect_bala.colliderect(rect_objeto):
                print("¡Colisión detectada con un objeto!")
                prun.y = 0
                gusano.Salud -= 1
                CambiarColor(gusano)
                
    # Detectar colision con obstaculos
    for obstaculo in obstaculos:
        rect_objeto = crear_rect(obstaculo)
        if rect_bala.colliderect(rect_objeto):
            #print("¡Colisión detectada con un objeto!")
            prun.y = 0
            obstaculo.Salud -= 1
                        
    if prun.y > 0:
        #dibujar(prun)
        prun.Hora = pygame.time.get_ticks()
        Q.meter(prun)

def moverBalaN(prun):
    print(f'Moviendo bala N: {prun}')
    
def crearBala():
    global id
    indice_pcb = obtener_pcb_del_pool()
    if indice_pcb is None:
        print("No hay PCBs disponibles en el pool")
        return
    BalaUser = pcb_pool[indice_pcb]
    BalaUser.PID = id
    BalaUser.Tipo  = BALA
    BalaUser.Ancho = 5
    BalaUser.Alto  = 10
    BalaUser.Color = (255, 0, 0)  # Rojo
    BalaUser.x = (canon.Ancho - BalaUser.Ancho) // 2 + canon.x
    BalaUser.y = canon.y - BalaUser.Alto
    BalaUser.Retardo = 1
    #BalaUser.Hora = HoraAbs
    BalaUser.Hora = pygame.time.get_ticks()
    dibujar(BalaUser)

    Q.meter(BalaUser)
    id += 1             

    
    
def planificador():
    PRUN = Q.sacar()
    #print(PRUN)
    if PRUN is None:
        return

    current_time_ms = pygame.time.get_ticks()
    #current_time_ms = int(time.time() * 1000)  # Convertir tiempo a milisegundos

    if PRUN.Hora + PRUN.Retardo > current_time_ms:
        Q.meter(PRUN)
        #moverNave(PRUN)
        print(current_time_ms)
        print(PRUN.Hora + PRUN.Retardo)
    else:
        #print('----')
        
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
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                crearBala()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and canon.x > 0:
        canon.x -= velocidad
    if teclas[pygame.K_RIGHT] and canon.x < ANCHO_PANTALLA - ANCHO_CANON:
        canon.x += velocidad
        
    
    # Dibujar en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar la pantalla con color negro
    dibujar(canon)
    
    for dibujo in Q:
        dibujar(dibujo)
    
    #dibujar(Q.first())
    for obstaculo in obstaculos:
        if obstaculo.Salud > 0:
            dibujar(obstaculo)
        else:
            obstaculos.remove(obstaculo)

    
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

