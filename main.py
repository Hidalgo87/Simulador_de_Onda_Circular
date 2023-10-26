import math
import pygame
import sys

# Colores RGB
BLACK = (0, 0, 0)
PINK = (255, 204, 187)
BLUE_LIGHT = (110, 181, 192)
BLUE_DARK = (0, 108, 132)
LIGHT_GRAY = (226, 232, 228)
GREEN_DARK = (51, 82, 82)
GRAY_DARK = (45, 48, 51)


def calcularIntensidad(distancia):
    num = 0.1 /(4 * math.pi * distancia ** 2)
    # Formatear el número para mostrar 3 dígitos y la notación científica
    formatted_num = "{:.4e}".format(num)
    # O usando una f-string (disponible en Python 3.6+)
    formatted_num = f"{num:.4e}"
    return formatted_num


# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulador de Onda Esférica")


# Parámetros de la onda
wave_radius_right = 1
# Establece el centro de la onda en el lado izquierdo de la pantalla
wave_center_right = (3 * screen_width // 4, screen_height // 2)
wave_color_right = BLUE_LIGHT
max_radius = 155

wave_radius_left = 90
wave_center_left = (screen_width // 4, screen_height // 2)
wave_color_left = BLUE_DARK

#label_color = GRAY_DARK
label_color = GREEN_DARK

# Fuente para el texto
font = pygame.font.SysFont("comicsans", 30)

clock = pygame.time.Clock()

running = True
circle_opening = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill(LIGHT_GRAY)
    rec = pygame.Rect(-20, -20, screen_width // 2 + 20, screen_height + 30)
    pygame.draw.rect(screen, BLACK, rec, 1)

    # ESFERA DERECHA
    if circle_opening:
        wave_radius_right += 1
        if wave_radius_right == max_radius:
            circle_opening = False
    else:
        wave_radius_right = 1
        circle_opening = True

    # Ajusta el grosor de la línea en función del radio (inversamente proporcional)
    line_thickness_right = max(1, max_radius - wave_radius_right)

    # Dibuja la onda esférica

    pygame.draw.circle(screen, wave_color_right, wave_center_right, wave_radius_right, line_thickness_right)

    # Muestra el radio actual en un label
    text = font.render(f"Radio: {wave_radius_right}", True, label_color)
    screen.blit(text, (3*screen_width // 4 - text.get_width()//2, 40))

    text = font.render(f"Intensidad: {calcularIntensidad(wave_radius_right)}", True, label_color)
    screen.blit(text, (3*screen_width // 4 - text.get_width()//2, 70))

    # TODO: ESFERA IZQUIERDA

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_RIGHT]:
        if wave_radius_left < max_radius:
            wave_radius_left += 1
    if keys[pygame.K_DOWN] or keys[pygame.K_LEFT]:
        if wave_radius_left > 1:
            wave_radius_left -= 1

    line_thickness_left = max(1, max_radius - wave_radius_left)

    # Dibuja la onda esférica

    pygame.draw.circle(screen, wave_color_left, wave_center_left, wave_radius_left, line_thickness_left)

    # Muestra el radio actual en un label
    text = font.render(f"Radio: {wave_radius_left}", True, label_color)
    screen.blit(text, (screen_width // 4 - text.get_width()//2, 40))

    # Muestra la intensidad en el punto
    text = font.render(f"Intensidad: {calcularIntensidad(wave_radius_left)}", True, label_color)
    screen.blit(text, (screen_width // 4 - text.get_width()//2, 70))

    # MOSTRAR PANTALLA
    pygame.display.flip()
    clock.tick(60)

# Cierra Pygame
pygame.quit()
sys.exit()
