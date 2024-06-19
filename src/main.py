import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Cañón Sencillo")

# Configuración del cañón
ANCHO_CANON = 50
ALTO_CANON = 20
canon_color = (255, 0, 0)  # Rojo
canon_pos_x = ANCHO_PANTALLA // 2 - ANCHO_CANON // 2
canon_pos_y = ALTO_PANTALLA - ALTO_CANON - 10
velocidad = 5

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and canon_pos_x > 0:
        canon_pos_x -= velocidad
    if teclas[pygame.K_RIGHT] and canon_pos_x < ANCHO_PANTALLA - ANCHO_CANON:
        canon_pos_x += velocidad

    # Dibujar en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar la pantalla con color negro
    pygame.draw.rect(pantalla, canon_color, (canon_pos_x, canon_pos_y, ANCHO_CANON, ALTO_CANON))
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad del juego
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()

