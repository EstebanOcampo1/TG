import pygame
import sys

# Inicializa Pygame
pygame.init()

# Constantes de pantalla
ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Crear la pantalla
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con Menú")

# Fuentes
font = pygame.font.SysFont(None, 50)


# Función para dibujar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Funciones de minijuegos
def minijuego1():
    running = True
    while running:
        screen.fill(BLANCO)
        draw_text("Minijuego 1", font, NEGRO, screen, ANCHO//2, ALTO//2)

        arrow_img = pygame.image.load('arrow.png')  # Asegúrate de tener un archivo 'arrow.png'
        arrow_img = pygame.transform.scale(arrow_img, (50, 50)) 
        arrow_rect = arrow_img.get_rect()
        arrow_rect.topleft = (10, 10)  # Posición de la flecha en la pantallaç

        # Dibujar la flecha de regreso
        screen.blit(arrow_img, arrow_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    running = False

        pygame.display.update()

def minijuego2():
    running = True
    while running:
        screen.fill(BLANCO)
        draw_text("Minijuego 2", font, NEGRO, screen, ANCHO//2, ALTO//2)

        arrow_img = pygame.image.load('arrow.png')  # Asegúrate de tener un archivo 'arrow.png'
        arrow_img = pygame.transform.scale(arrow_img, (50, 50)) 
        arrow_rect = arrow_img.get_rect()
        arrow_rect.topleft = (10, 10)  # Posición de la flecha en la pantallaç

        # Dibujar la flecha de regreso
        screen.blit(arrow_img, arrow_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    running = False

        pygame.display.update()

def minijuego3():
    running = True
    while running:
        screen.fill(BLANCO)
        draw_text("Minijuego 3", font, NEGRO, screen, ANCHO//2, ALTO//2)

        arrow_img = pygame.image.load('arrow.png')  # Asegúrate de tener un archivo 'arrow.png'
        arrow_img = pygame.transform.scale(arrow_img, (50, 50)) 
        arrow_rect = arrow_img.get_rect()
        arrow_rect.topleft = (10, 10)  # Posición de la flecha en la pantalla
        # Dibujar la flecha de regreso
        screen.blit(arrow_img, arrow_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    running = False

        pygame.display.update()

# Función para mostrar el menú de minijuegos de un nivel
def mostrar_minijuegos():
    while True:
        screen.fill(BLANCO)
        draw_text("Seleccione un Minijuego", font, NEGRO, screen, ANCHO//2, ALTO//4)

        # Botones para los minijuegos
        minijuego1_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 - 60, 200, 50)
        minijuego2_button = pygame.Rect(ANCHO//2 - 100, ALTO//2, 200, 50)
        minijuego3_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 + 60, 200, 50)

        pygame.draw.rect(screen, NEGRO, minijuego1_button)
        pygame.draw.rect(screen, NEGRO, minijuego2_button)
        pygame.draw.rect(screen, NEGRO, minijuego3_button)

        draw_text("Minijuego 1", font, BLANCO, screen, minijuego1_button.centerx, minijuego1_button.centery)
        draw_text("Minijuego 2", font, BLANCO, screen, minijuego2_button.centerx, minijuego2_button.centery)
        draw_text("Minijuego 3", font, BLANCO, screen, minijuego3_button.centerx, minijuego3_button.centery)

        # Cargar la imagen de la flecha
        arrow_img = pygame.image.load('arrow.png')  # Asegúrate de tener un archivo 'arrow.png'
        arrow_img = pygame.transform.scale(arrow_img, (50, 50)) 
        arrow_rect = arrow_img.get_rect()
        arrow_rect.topleft = (10, 10)  # Posición de la flecha en la pantallaç

        # Dibujar la flecha de regreso
        screen.blit(arrow_img, arrow_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if minijuego1_button.collidepoint(event.pos):
                    minijuego1()
                if minijuego2_button.collidepoint(event.pos):
                    minijuego2()
                if minijuego3_button.collidepoint(event.pos):
                    minijuego3()
                if arrow_rect.collidepoint(event.pos):
                    return  # Regresa al menú de niveles

        pygame.display.update()

# Funciones de niveles que contienen el menú de minijuegos
def nivel1():
    mostrar_minijuegos()

def nivel2():
    mostrar_minijuegos()

def nivel3():
    mostrar_minijuegos()

# Función del menú de niveles
def level_menu():
    while True:
        screen.fill(BLANCO)
        draw_text("Seleccione un Nivel", font, NEGRO, screen, ANCHO//2, ALTO//4)

        # Botones para los niveles
        nivel1_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 - 60, 200, 50)
        nivel2_button = pygame.Rect(ANCHO//2 - 100, ALTO//2, 200, 50)
        nivel3_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 + 60, 200, 50)

        pygame.draw.rect(screen, NEGRO, nivel1_button)
        pygame.draw.rect(screen, NEGRO, nivel2_button)
        pygame.draw.rect(screen, NEGRO, nivel3_button)

        draw_text("Nivel 1", font, BLANCO, screen, nivel1_button.centerx, nivel1_button.centery)
        draw_text("Nivel 2", font, BLANCO, screen, nivel2_button.centerx, nivel2_button.centery)
        draw_text("Nivel 3", font, BLANCO, screen, nivel3_button.centerx, nivel3_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nivel1_button.collidepoint(event.pos):
                    nivel1()
                if nivel2_button.collidepoint(event.pos):
                    nivel2()
                if nivel3_button.collidepoint(event.pos):
                    nivel3()

        pygame.display.update()

# Función del menú principal
def main_menu():
    while True:
        screen.fill(BLANCO)
        draw_text("Menú Principal", font, NEGRO, screen, ANCHO//2, ALTO//4)

        # Botones para Start y Quit
        start_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 - 60, 200, 50)
        quit_button = pygame.Rect(ANCHO//2 - 100, ALTO//2 + 60, 200, 50)

        pygame.draw.rect(screen, NEGRO, start_button)
        pygame.draw.rect(screen, NEGRO, quit_button)

        draw_text("Start", font, BLANCO, screen, start_button.centerx, start_button.centery)
        draw_text("Quit", font, BLANCO, screen, quit_button.centerx, quit_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    level_menu()  # Lleva al menú de niveles
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Ejecutar el menú principal
main_menu()
