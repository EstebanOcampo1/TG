import pygame
import sys

from tkinter import *
from tkinter import messagebox

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Novela Visual en Pygame')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 102, 204)
SEMI_TRANSPARENT = (0, 0, 0, 180)

# Carga de imágenes (debes tener las imágenes en el mismo directorio o ajustar las rutas)
background_image = pygame.image.load('Imagenes/Lilac solid colour.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Redimensiona el fondo

character_image = pygame.image.load('Imagenes/Capibara-removebg.png')

# Fuentes para texto
font = pygame.font.Font(None, 36)

# Variable para almacenar el nombre del usuario
user_name = ''
input_active = True  # Indica si la caja de texto está activa o no

# Diálogos del juego
dialogues = [
    "Hola, ¿cómo te llamas?",
    "Yo soy el personaje principal de esta historia.",
    "¡Vamos a vivir una gran aventura!",
]

# Variables del juego
current_dialogue = 0
clock = pygame.time.Clock()

def get_username():
    # Crear una ventana emergente
    popup = Toplevel()
    popup.title("Nombre de usuario")
    popup.geometry("300x150")
    
    # Etiqueta
    label = Label(popup, text="Ingresa tu nombre:", font=("Arial", 12))
    label.pack(pady=10)
    
    # Entrada de texto
    entry = Entry(popup, font=("Arial", 12))
    entry.pack(pady=10)
    
    def on_submit():
        user_name = entry.get()  # Obtener el nombre ingresado
        if user_name:
            popup.destroy()  # Cerrar el cuadro de diálogo
            print(f'Nombre ingresado: {user_name}')
        else:
            print("El campo de nombre está vacío")

    # Botón para enviar el nombre
    submit_button = Button(popup, text="Aceptar", command=on_submit, font=("Arial", 12))
    submit_button.pack(pady=10)

    popup.mainloop()


def draw_text(text, font, color, x, y):
    """Función para dibujar texto en la pantalla."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_rounded_rect(surface, color, rect, radius=0.4):
    """Dibuja un rectángulo con bordes redondeados."""
    rect = pygame.Rect(rect)
    corner_radius = int(min(rect.width, rect.height) * radius)
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

def input_name_popup():
    global user_name, input_active

    input_box = pygame.Rect(300, 250, 200, 50)  # Caja de entrada

    while input_active:  # Mostrar hasta que el usuario presione Enter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Entrada de texto cuando la caja está activa
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter para confirmar el nombre
                    if user_name != '':
                        input_active = False  # Desaparece el pop-up
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]  # Borrar último caracter
                else:
                    user_name += event.unicode  # Añadir caracteres al nombre

        # Fondo semitransparente para el pop-up
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill(SEMI_TRANSPARENT)
        screen.blit(overlay, (0, 0))

        # Dibuja el fondo del pop-up con bordes redondeados
        popup_rect = pygame.Rect(250, 150, 300, 200)  # Rectángulo para el pop-up
        draw_rounded_rect(screen, LIGHT_BLUE, popup_rect)  # Fondo del pop-up
        draw_rounded_rect(screen, DARK_BLUE, popup_rect, 0.1)  # Borde del pop-up

        # Dibuja la caja de entrada de texto
        pygame.draw.rect(screen, GRAY, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)  # Borde de la caja de entrada

        # Muestra el nombre ingresado en la caja de texto
        draw_text(user_name, font, BLACK, input_box.x + 10, input_box.y + 10)

        # Muestra instrucciones al jugador
        draw_text("Ingresa tu nombre y presiona Enter:", font, BLACK, 230, 200)

        # Actualiza la pantalla
        pygame.display.flip()

        # Controla la velocidad del bucle
        clock.tick(30)

def game_loop():
    global current_dialogue

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Avanza al siguiente diálogo al hacer clic
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_dialogue < len(dialogues) - 1:
                    current_dialogue += 1

        # Dibuja el fondo
        screen.blit(background_image, (0, 0))

        # Dibuja al personaje
        screen.blit(character_image, (200, 100))

        # Dibuja el cuadro de diálogo
        pygame.draw.rect(screen, BLACK, (50, 465, 720, 190))
        pygame.draw.rect(screen, WHITE, (60, 475, 700, 130))

        # Muestra el diálogo actual
        if current_dialogue < len(dialogues):
            draw_text(dialogues[current_dialogue], font, BLACK, 80, 500)

        # Muestra el nombre del usuario si ya fue ingresado
        if user_name and current_dialogue > 0:  # Mostrar solo después del primer diálogo
            draw_text(f"¡Hola, {user_name}!", font, BLACK, 300, 400)

        # Actualiza la pantalla
        pygame.display.flip()

        # Controla la velocidad del bucle
        clock.tick(60)

# Iniciar el juego
game_loop()
