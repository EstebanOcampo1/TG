import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Vocabulario con Subrayado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)

# Fuente
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 35)

# Lista de palabras
words = ["Apple", "Banana", "Cherry", "Grape", "Orange", "Pineapple", "Strawberry", "Watermelon"]

# Asegurarse de que haya el mismo número de palabras que posiciones
word_positions = [(screen_width // 4, 100), (screen_width // 4, 150), (screen_width // 4, 200), (screen_width // 4, 250)]

# Recortar la lista de palabras si es necesario para que coincida con el número de posiciones
words = words[:len(word_positions)]

# Índice de la palabra actual subrayada
current_word_index = random.randint(0, len(words) - 1)

# Puntaje
score = 0

# Botón
button_pos = (screen_width // 2 - 75, screen_height // 2 + 100)
button_size = (150, 50)

# Función para dibujar el botón
def draw_button(text, pos, size, color):
    pygame.draw.rect(screen, color, (*pos, *size))
    button_text = small_font.render(text, True, WHITE)
    text_rect = button_text.get_rect(center=(pos[0] + size[0] // 2, pos[1] + size[1] // 2))
    screen.blit(button_text, text_rect)

# Función para seleccionar una nueva palabra subrayada que sea distinta a la actual
def new_word():
    global current_word_index
    previous_word_index = current_word_index
    while current_word_index == previous_word_index:
        current_word_index = random.randint(0, len(words) - 1)

# Bucle principal del juego
running = True
while running:
    screen.fill(WHITE)

    # Mostrar todas las palabras, subrayando la actual
    for i, word in enumerate(words):
        word_surface = font.render(word, True, BLACK)
        word_rect = word_surface.get_rect(topleft=word_positions[i])
        screen.blit(word_surface, word_rect)

        # Subrayar la palabra actual
        if i == current_word_index:
            pygame.draw.line(screen, BLACK, (word_rect.left, word_rect.bottom + 5), (word_rect.right, word_rect.bottom + 5), 3)

    # Dibujar el botón
    draw_button("Said it!", button_pos, button_size, BLUE)

    # Evento de cierre y detección de clics
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Verificar si el botón fue presionado
            button_rect = pygame.Rect(*button_pos, *button_size)
            if button_rect.collidepoint(mouse_pos):
                score += 1  # Incrementar el puntaje
                new_word()  # Cambiar la palabra subrayada cuando se haga clic

    # Mostrar el puntaje
    score_text = small_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
