"""Nombre: ProyectoSO1
    Autor: Jose Carlos Giron Solano
    Año: 2024
    """

import pygame
import sys
import time
import random as rd

from cola import PCB, cola

###---------------------    Declaracion de variables globales---------------------------------------
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
framesCentipede = []
Score = 0
Vidas = 4
estado = ''
respawn = False
n_spawn = 0
cant_misiles = 0
exp = 4

#Tipos
CENTIPEDE = 0
BALA = 1
OBSTACULO = 2
CANON = 3
MISIL = 4

# Inicializar Pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 32)
# Inicializar el módulo de sonido
pygame.mixer.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Cañón Sencillo")


# Crear un pool de objetos PCB
pool_size = 600  # Ajustar según sea necesario
pcb_pool = [PCB() for _ in range(pool_size)]
free_pcb_indices = list(range(pool_size))
obstaculos = [PCB() for _ in range(20)]
lvidas = [PCB() for _ in range(Vidas)]
bodys = [PCB() for _ in range(4)]

###-----------------------------------Carga de recursos------------------------------------------------------------##
#Imagenes
img_canon_org = pygame.image.load('img/cannon.png')
img_canon = pygame.transform.scale(img_canon_org, (30, 30))
img_vida = pygame.transform.scale(img_canon_org, (20, 20))
img_menu_org = pygame.image.load('img/main_menu_background.png')
img_menu = pygame.transform.scale(img_menu_org, (800, 600))

img_gameover_org = pygame.image.load('img/game_over_back.png')
img_gameover = pygame.transform.scale(img_gameover_org, (800, 600))


#Frames de animacion
img_canexp0_org = pygame.image.load('img/cannon_explosion0.png')
img_canexp0 = pygame.transform.scale(img_canexp0_org, (30, 30))

img_canexp01_org = pygame.image.load('img/cannon_explosion01.png')
img_canexp01 = pygame.transform.scale(img_canexp01_org, (30, 30))

img_canexp1_org = pygame.image.load('img/cannon_explosion1.png')
img_canexp1 = pygame.transform.scale(img_canexp1_org, (30, 30))

img_canexp2_org = pygame.image.load('img/cannon_explosion2.png')
img_canexp2 = pygame.transform.scale(img_canexp2_org, (30, 30))

img_canexp3_org = pygame.image.load('img/cannon_explosion3.png')
img_canexp3 = pygame.transform.scale(img_canexp3_org, (30, 30))

framesexp = [img_canexp0, img_canexp1, img_canexp01, img_canexp01 , img_canexp2, img_canexp3]

img_obs_org = pygame.image.load('img/obstaculo.png')
img_obs = pygame.transform.scale(img_obs_org, (20, 20))

img_obs1_org = pygame.image.load('img/obstaculo_1.png')
img_obs1 = pygame.transform.scale(img_obs1_org, (20, 20))

img_obs2_org = pygame.image.load('img/obstaculo_2.png')
img_obs2 = pygame.transform.scale(img_obs2_org, (20, 20))

img_obs3_org = pygame.image.load('img/obstaculo_3.png')
img_obs3 = pygame.transform.scale(img_obs3_org, (20, 20))

img_head0_org = pygame.image.load('img/head_0.png')
img_head0 = pygame.transform.scale(img_head0_org, (20, 20))
img_head0_inv = pygame.transform.flip(img_head0, True, False)

img_head2_org = pygame.image.load('img/head_2.png')
img_head2 = pygame.transform.scale(img_head2_org, (20, 20))
img_head2_inv = pygame.transform.flip(img_head2, True, False)

img_head3_org = pygame.image.load('img/head_3.png')
img_head3 = pygame.transform.scale(img_head3_org, (20, 20))
img_head3_inv = pygame.transform.flip(img_head3, True, False)

img_head4_org = pygame.image.load('img/head_4.png')
img_head4 = pygame.transform.scale(img_head4_org, (20, 20))
img_head4_inv = pygame.transform.flip(img_head4, True, False)
 
img_head6_org = pygame.image.load('img/head_6.png')
img_head6 = pygame.transform.scale(img_head6_org, (20, 20))
img_head6_inv = pygame.transform.flip(img_head6, True, False)

framehead = [img_head0, img_head2, img_head3, img_head4, img_head6, img_head4, img_head3, img_head2, img_head0]
frameheadInv = [img_head0_inv, img_head2_inv, img_head3_inv, img_head4_inv, img_head6_inv, img_head4_inv, 
                img_head3_inv, img_head2_inv, img_head0_inv]

#Cuerpo del gusano frames
img_body2_org = pygame.image.load('img/body_2.png')
img_body2 = pygame.transform.scale(img_body2_org, (20, 20))
img_body2_inv = pygame.transform.flip(img_body2, True, False)

img_body3_org = pygame.image.load('img/body_3.png')
img_body3 = pygame.transform.scale(img_body3_org, (20, 20))
img_body3_inv = pygame.transform.flip(img_body3, True, False)

img_body4_org = pygame.image.load('img/body_4.png')
img_body4 = pygame.transform.scale(img_body4_org, (20, 20))
img_body4_inv = pygame.transform.flip(img_body4, True, False)

img_body6_org = pygame.image.load('img/body_6.png')
img_body6 = pygame.transform.scale(img_body6_org, (20, 20))
img_body6_inv = pygame.transform.flip(img_body6, True, False)

img_body7_org = pygame.image.load('img/body_7.png')
img_body7 = pygame.transform.scale(img_body7_org, (20, 20))
img_body7_inv = pygame.transform.flip(img_body7, True, False)

framebody = [img_body2, img_body3, img_body4, img_body6, img_body7, img_body6, img_body4, img_body3, img_body2]
framebodyInv = [img_body2_inv, img_body3_inv, img_body4_inv, img_body6_inv, img_body7_inv
                , img_body6_inv, img_body4_inv, img_body3_inv, img_body2_inv]

# Misil frames
img_misil0_org = pygame.image.load('img/frame_0.png')
img_misil0 = pygame.transform.scale(img_misil0_org, (10, 30))

img_misil1_org = pygame.image.load('img/frame_1.png')
img_misil1 = pygame.transform.scale(img_misil1_org, (10, 30))

img_misil2_org = pygame.image.load('img/frame_2.png')
img_misil2 = pygame.transform.scale(img_misil2_org, (10, 30))

img_misil3_org = pygame.image.load('img/frame_3.png')
img_misil3 = pygame.transform.scale(img_misil3_org, (10, 30))

img_misil0_org = pygame.image.load('img/frame_4.png')
img_misil4 = pygame.transform.scale(img_misil0_org, (10, 30))

frameMisil = [img_misil0, img_misil1, img_misil2, img_misil3, img_misil4]

# Efectos de sonido
sonido_disparo = pygame.mixer.Sound('sound/laserSmall_002.ogg')
sonido_slime = pygame.mixer.Sound('sound/slime_000.ogg')
sonido_impact_obj = pygame.mixer.Sound('sound/impact_obj.wav')
sonido_explosion = pygame.mixer.Sound('sound/explosionCrunch_003.ogg')
sonido_game_over = pygame.mixer.Sound('sound/die.wav')
sonido_misil = pygame.mixer.Sound('sound/launch_rocket.wav')
sonido_misil.set_volume(0.2)
sonido_hit1 = pygame.mixer.Sound('sound/metal_hit_1.wav')
sonido_hit2 = pygame.mixer.Sound('sound/metal_hit_2.wav')
sonido_hit2.set_volume(0.2)

sonido_talk = pygame.mixer.Sound('sound/talk_insect.mp3')
sonido_walk = pygame.mixer.Sound('sound/walk.mp3')
main_menu_sound = pygame.mixer.Sound('sound/main_menu_sound.mp3')

# Tiempo de la última reproducción
ultimo_tiempo_reproduccion = 0

# Configuración del cañón   
ANCHO_CANON = 20
ALTO_CANON = 20
canon_color = (255, 0, 0)  # Rojo
canon_pos_x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
canon_pos_y = ALTO_PANTALLA - ALTO_CANON - 15
velocidad = 5



# Función de pantalla inicial
def pantalla_inicial():
    fuente = pygame.font.Font(None, 45)
    titulo = fuente.render("Pantalla Inicial", True, (255, 255, 255))
    iniciar = fuente.render("Comenzar", True, (255, 255, 255))
    iniciar_hover = fuente.render("Comenzar", True, (255, 0, 0))
    rect_titulo = titulo.get_rect(center=(400, 200))
    rect_iniciar = iniciar.get_rect(center=(570, 300))
    return titulo, iniciar, iniciar_hover, rect_titulo, rect_iniciar

# Función de pantalla de Game Over
def pantalla_game_over():
    global Score
    fuente = pygame.font.Font(None, 65)
    game_over = fuente.render(f"Puntuacion: {Score}", True, (255, 255, 255))
    reintentar = fuente.render("Reintentar", True, (255, 255, 255))
    reintentarhover = fuente.render("Reintentar", True, (255, 0, 0))
    rect_game_over = game_over.get_rect(center=(400, 200))
    rect_reintentar = reintentar.get_rect(center=(400, 400))
    return game_over, reintentar, reintentarhover, rect_game_over, rect_reintentar

def start():
    global head, body1, body2, body3, body4, n_spawn, exp, cant_misiles
    
    exp = 60
    n_spawn = 100
    cant_misiles = 0
    #Cañon
    canon.x = canon_pos_x
    canon.y = canon_pos_y
    canon.Alto = ALTO_CANON
    canon.Ancho = ANCHO_CANON
    canon.Color = canon_color 
    canon.Tipo = CANON
    canon.is_body = False
    canon.Salud = 1
    
    #head del gusano
    head.Tipo = CENTIPEDE
    head.Ancho= 20
    head.Alto  = 20
    head.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
    head.y = 10
    head.Color = canon_color
    head.Hora = pygame.time.get_ticks()
    head.Retardo = RetardoCentipede
    head.Dir = 0 
    head.Salud = 2
    Q.meter(head)

    #Cuerpo del gusano
    espacio = 20
    for body in bodys:
        body.Tipo = CENTIPEDE
        body.Ancho= 20
        body.Alto  = 20
        body.x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2 + espacio
        body.y = 10
        body.Color = canon_color
        body.Hora = pygame.time.get_ticks()
        body.Retardo = RetardoCentipede
        body.Dir = 0 
        body.Salud = 2
        body.is_body = True
        Q.meter(body)
        espacio += 20
    
    for obstaculo in obstaculos:
        obstaculo.Color = Clwhite
        obstaculo.Alto = head.Alto
        obstaculo.Ancho = head.Ancho
        obstaculo.x = rd.choice(range(30, 760 + 1, 20))
        obstaculo.y = rd.choice(range(30, 500 + 1, 20))
        obstaculo.Salud = 4
        obstaculo.Tipo = OBSTACULO
    
    f = 0 
    for vida in lvidas:
        vida.Tipo = CANON
        vida.Alto = canon.Alto
        vida.Ancho = canon.Ancho
        vida.x = 530 + f
        vida.y = 0
        vida.Color = Clwhite
        vida.is_body = True
        f += 20
        
        

    

start()


# Funciones
def CambiarColor(objeto):
    if objeto.Salud == 1:
        objeto.Color = Clgreen
        
def obtener_pcb_del_pool():
    if free_pcb_indices:
        return free_pcb_indices.pop()
    else:
        return None

def sonido_centipede():
    global ultimo_tiempo_reproduccion
    tiempo_actual = time.time()
    if tiempo_actual - ultimo_tiempo_reproduccion >= 0.5:
        sonido_walk.play()
        ultimo_tiempo_reproduccion = tiempo_actual

def devolver_pcb_al_pool(indice):
    free_pcb_indices.append(indice)
    
def crear_rect(objeto):
    return pygame.Rect(objeto.x, objeto.y, objeto.Ancho, objeto.Alto)

def dibujar(objeto):
    pygame.draw.rect(pantalla, objeto.Color, (objeto.x, objeto.y, objeto.Ancho, objeto.Alto))
    # Dibujar la imagen en la pantalla
    rect_obj = crear_rect(objeto)
    if objeto.Tipo == CANON:
        if objeto.is_body:
            pantalla.blit(img_vida, rect_obj)
        else:  
            if canon.Salud == 1: 
                pantalla.blit(img_canon, rect_obj)
            elif canon.Salud == 0:
                index = exp//10 -1
                cimg = framesexp[index]
                pantalla.blit(cimg, rect_obj)

    elif objeto.Tipo == MISIL:
        imgm = frameMisil.pop(0)
        pantalla.blit(imgm, rect_obj)
        frameMisil.append(imgm)
        
        
    elif objeto.Tipo == OBSTACULO:
        if objeto.Salud == 4:
            pantalla.blit(img_obs, rect_obj)
        if objeto.Salud == 3:
            pantalla.blit(img_obs1, rect_obj)
        if objeto.Salud == 2:
            pantalla.blit(img_obs2, rect_obj)
        if objeto.Salud == 1:
            pantalla.blit(img_obs3, rect_obj)
            
    elif objeto.Tipo == CENTIPEDE:
        if objeto.is_body:
            if objeto.Dir == 0:
                img = framebody.pop(0)
                pantalla.blit(img, rect_obj)
                framebody.append(img)
            else:
                img = framebodyInv.pop(0)
                pantalla.blit(img, rect_obj)
                framebodyInv.append(img)
        else:
            if objeto.Dir == 0:
                img = framehead.pop(0)
                pantalla.blit(img, rect_obj)
                framehead.append(img)
            else:
                img = frameheadInv.pop(0)
                pantalla.blit(img, rect_obj)
                frameheadInv.append(img)
            
    
# Función para renderizar texto
def render_text(text, font, color):
    return font.render(text, True, color)
    
def cambiarDir(objeto):
    if objeto.Dir == 0:
        objeto.Dir = 1
    elif objeto.Dir == 1:
        objeto.Dir = 0


def moverNave(prun):
    global Score, Vidas, estado, respawn
    
    if prun.x < 0:
        sonido_hit2.play()
        cambiarDir(prun)
        prun.y = prun.y + prun.Alto
    elif prun.x > ANCHO_PANTALLA - prun.Ancho:
        sonido_hit2.play()
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
            
    #detectar colision con jugador
    if rect_gus.colliderect(crear_rect(canon)):
        if Vidas > 0:
            sonido_explosion.play()
            Q.vaciar()
            Vidas -= 1  
            #lvidas.pop(0) 
            respawn = True      
            return
        else:
            Q.vaciar()
            estado = 'game_over'
            respawn = True
            return
    if prun.Dir == 0:
        vel = 10
    elif prun.Dir == 1:
        vel = -10 
    if not prun.is_body:
        sonido_centipede()  
    prun.x -= vel
    prun.Hora = pygame.time.get_ticks()
    if prun.Salud > 0:
        Q.meter(prun)
    else:
        nobstaculo = PCB()
        nobstaculo = prun
        nobstaculo.Salud = 4
        nobstaculo.Tipo = OBSTACULO
        obstaculos.append(nobstaculo)
        Score += 100
        i = 0
        while i <= Q.long():
            elem = Q.pos(i)
            if elem.Tipo == CENTIPEDE:   
                elem.is_body = False
                break
            i += 1    
        #Q.meter(camb)
        
        sonido_slime.play()
        

def moverBalaU(prun):
    global Score
    prun.y = prun.y -15
    
    # Detectar colision con el cienpies
    rect_bala = crear_rect(prun)
    for gusano in Q:
        if gusano.Tipo != BALA and gusano.Tipo != MISIL:
            rect_objeto = crear_rect(gusano)
            if rect_bala.colliderect(rect_objeto):
                sonido_talk.play()
                prun.y = 0
                gusano.Salud -= 1
                #CambiarColor(gusano)
                Score += 10
                
    # Detectar colision con obstaculos
    for obstaculo in obstaculos:
        rect_objeto = crear_rect(obstaculo)
        if rect_bala.colliderect(rect_objeto):
            prun.y = 0
            obstaculo.Salud -= 1
            sonido_impact_obj.play()
            Score += 5
                        
    if prun.y > 0:
        #dibujar(prun)
        prun.Hora = pygame.time.get_ticks()
        Q.meter(prun)

def moverBalaN(prun):
    global cant_misiles, respawn, estado, Vidas
    prun.y = prun.y + 20
    if prun.y < ALTO_PANTALLA:
        prun.Hora = pygame.time.get_ticks()
        Q.meter(prun)
    else:
        cant_misiles -= 1
    
    rect_misil = crear_rect(prun)
    #detectar colision con jugador
    if rect_misil.colliderect(crear_rect(canon)):
        if Vidas > 0:
            sonido_explosion.play()
            Q.vaciar()
            Vidas -= 1  
            canon.Salud = 0
            respawn = True      
            return
        else:
            sonido_game_over.play()
            Q.vaciar()
            estado = 'game_over'
            respawn = True
            return
    
def crearBala():
    global id
    indice_pcb = obtener_pcb_del_pool()
    if indice_pcb is None:
        print("No hay PCBs disponibles en el pool")
        return
    BalaUser = pcb_pool[indice_pcb]
    BalaUser.PID = id
    BalaUser.Tipo  = BALA
    BalaUser.Ancho = 2
    BalaUser.Alto  = 15
    BalaUser.Color = (255, 0, 0)  # Rojo
    BalaUser.x = (canon.Ancho - BalaUser.Ancho) // 2 + canon.x
    BalaUser.y = canon.y - BalaUser.Alto
    BalaUser.Retardo = 1
    BalaUser.Hora = pygame.time.get_ticks()
    dibujar(BalaUser)
    sonido_disparo.play()

    Q.meter(BalaUser)
    id += 1  
    
def crearMisil():
    global cant_misiles
    numero = rd.randint(0,150)
    if numero == 0 and cant_misiles < 3:
        Misil = PCB()
        Misil.Alto = 30
        Misil.Ancho = 15
        Misil.Color = (0, 0, 0)
        Misil.Retardo = 1
        Misil.Hora = pygame.time.get_ticks()
        Misil.x = rd.choice(range(20, 760 + 1, 20))
        Misil.y = 0
        Misil.Tipo = MISIL
        cant_misiles += 1
        sonido_misil.play()
        
        
        Q.meter(Misil)         
 #Planificador Basado en los FPS del juego            
def planificador():
    global obstaculos, exp
    PRUN = Q.sacar()
    if PRUN is None:
        if exp == 0:
            obstaculos = [PCB() for _ in range(20)]
            start()   
        exp -= 1    
        return
    else:  
        crearMisil()        
        if PRUN.Tipo == CENTIPEDE:
            moverNave(PRUN)
        elif PRUN.Tipo == BALA:
            moverBalaU(PRUN)
        elif PRUN.Tipo == MISIL:
            moverBalaN(PRUN)



#Planificador basado en el tiempo del sistema similar al ejemplo en delphi, NO ESTA SIENDO UTILIZADO   
def planificador2():
    global obstaculos, exp
    PRUN = Q.sacar()
    crearMisil()
    #print(PRUN)
    if PRUN is None:
        if exp == 0:
            obstaculos = [PCB() for _ in range(20)]
            start()   
        exp -= 1    
        return     
    current_time_ms = pygame.time.get_ticks()
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
        elif PRUN.Tipo == MISIL:
            moverBalaN(PRUN)

def menusound():
    if estado == 'inicio':
        main_menu_sound.play(-1)
    if estado == 'jugando':
        main_menu_sound.stop()

##--------------------------------------------Bucle principal del juego----------------------------------------------

estado = 'inicio'
main_menu_sound.play(-1)
corriendo = True
#n_spawn = 100
dibujarS = True
sw = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYUP and estado =='jugando':
            if evento.key == pygame.K_SPACE:
                crearBala()
        if estado == "inicio" and evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_iniciar.collidepoint(evento.pos):
                    estado = "jugando"
                    menusound()
        elif estado == "game_over" and evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_reintentar and rect_reintentar.collidepoint(evento.pos):
                    estado = "jugando" # Reinicia el juego
                    Score = 0
                    Vidas = 4
                    n_spawn = 100
    # Obtener la posición del mouse
    mouse_pos = pygame.mouse.get_pos()
    if estado == 'jugando':
        # Obtener las teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and canon.x > 0:
            canon.x -= velocidad
        if teclas[pygame.K_RIGHT] and canon.x < ANCHO_PANTALLA - ANCHO_CANON:
            canon.x += velocidad
        
        # Actualizar el texto dinámico continuamente
        elapsed_time = int(time.time() - time.time())
        ScoreText = f"Score: {Score} "    
        
        # Dibujar en la pantalla
        pantalla.fill((0, 0, 0))  # Limpiar la pantalla con color negro
        
        if respawn:
            if n_spawn > 0:
                if dibujarS:
                    dibujar(canon)
                    dibujarS = False
                else:
                    dibujarS = True
            else:
                respawn = False
            n_spawn -= 1       
        else:
            dibujar(canon)
        
        for i in range(Vidas):
            dibujar(lvidas[i])
        
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
        
            # Renderizar el texto dinámico
        texto_superficie = render_text(ScoreText, font, Clwhite)
        texto_rect = texto_superficie.get_rect(center=(680, 10))
        pantalla.blit(texto_superficie, texto_rect)
        
    elif estado =='inicio':
        pantalla.fill((0, 0, 0))
        titulo, iniciar, iniciarhover, rect_titulo, rect_iniciar = pantalla_inicial()
        pantalla.fill((0, 0, 0))
        pantalla.blit(img_menu, (0, 0))
        #pantalla.blit(titulo, rect_titulo)
        if rect_iniciar.collidepoint(mouse_pos):
            texto_surface = iniciarhover
        else:
            texto_surface = iniciar
        pantalla.blit(texto_surface, rect_iniciar)
    elif estado == 'game_over':
        pantalla.fill((0, 0, 0))
        pantalla.blit(img_gameover, (0, 0))
        game_over, reintentar, reintentarhover, rect_game_over, rect_reintentar = pantalla_game_over()
        pantalla.blit(game_over, rect_game_over)
        if rect_reintentar.collidepoint(mouse_pos):
            texto_surface = reintentarhover
        else:
            texto_surface = reintentar
        pantalla.blit(texto_surface, rect_reintentar)
        

    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    pygame.time.Clock().tick(50)

# Salir de Pygame
pygame.quit()
sys.exit()

