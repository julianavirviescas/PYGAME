import pygame

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primer Juego")

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

x = 100
y = 100

ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, VERDE, (x, y, 50, 50))
    pygame.display.update()

pygame.quit()