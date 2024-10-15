import pygame
import sys
import speech_recognition as sr
from difflib import SequenceMatcher

def speech_game():
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

    # Carga de imágenes
    background_image = pygame.image.load('imgs/Barkley_house.jpg')
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    character_image = pygame.image.load('imgs/Barkley-removebg.png')
    microphone_image = pygame.image.load('imgs/microphone.png')
    microphone_image = pygame.transform.scale(microphone_image, (50, 50))
    arrow_image = pygame.image.load('imgs/arrow2.png')
    arrow_image = pygame.transform.scale(arrow_image, (50, 50))

    # Fuentes
    font = pygame.font.Font(None, 36)

    # Variables del juego
    current_quest = 0
    result_message = ""
    question_answered = False
    button_pressed = False

    recognizer = sr.Recognizer()

    def draw_text(text, font, color, x, y):
        """Dibuja texto con fondo."""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(topleft=(x, y))
        box_surface = pygame.Surface((text_rect.width + 10, text_rect.height + 10))
        box_surface.set_alpha(200)
        box_surface.fill(WHITE)
        screen.blit(box_surface, text_rect.topleft)
        screen.blit(text_surface, (x + 5, y + 5))

    def draw_rounded_rect(surface, color, rect, radius):
        """Dibuja un rectángulo con esquinas redondeadas."""
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def draw_button_background(x, y):
        """Dibuja un recuadro detrás de los botones con esquinas redondeadas."""
        button_box_rect = pygame.Rect(x - 10, y - 10, 70, 70)  # +10 para margen
        draw_rounded_rect(screen, (98, 132, 245, 200), button_box_rect, radius=10)  # Ajusta el radio según sea necesario

    def listen_to_user():
        with sr.Microphone(device_index=2) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                print("Escuchando...")
                audio_data = recognizer.listen(source, timeout=5)
                recognized_text = recognizer.recognize_google(audio_data)
                print(f"Texto reconocido: {recognized_text}")
                return recognized_text.lower()
            except sr.UnknownValueError:
                print("No se pudo entender el audio.")
                return ""
            except sr.RequestError:
                print("No se pudo realizar la solicitud.")
                return ""

    def is_pronunciation_correct(expected_word, user_word):
        similarity = SequenceMatcher(None, expected_word, user_word).ratio()
        print(f"Comparando: '{expected_word}' con '{user_word}' - Similitud: {similarity}")
        return similarity >= 0.65

    questions = [
        {"question": "What did Lola lose?", "answer": "Lola lose her necklace"},
        {"question": "What is Lola’s brother?", "answer": "Lola’s brother is a cat"},
        {"question": "What does Barkley do?", "answer": "He is a detective"},
        {"question": "Where does Barkley go to investigate?", "answer": "to lola’s house"},
        {"question": "What did Barkley find?", "answer": "Barkley find a feather and a footprint"},
        {"question": "Who gave the necklace to Lola?", "answer": "her grandmother"},
        {"question": "Who tells Lola to ask Barkley for help?", "answer": "her brother"},
        {"question": "What kind of animal is Lola?", "answer": "Lola is a dog"},
        {"question": "Where did Barkley find the footprint?", "answer": "In the bedroom window"},
        {"question": "Who took the necklace?", "answer": "the raven took the necklace"},
        {"question": "Why did the raven take the necklace?", "answer": "it liked shiny things"}
    ]

    def ask_voice_question(question_data):
        """Resetea mensaje y escucha la respuesta."""
        nonlocal result_message, question_answered
        result_message = ""
        recognized_text = listen_to_user()
        if recognized_text:
            if is_pronunciation_correct(question_data["answer"].lower(), recognized_text):
                result_message = f"Correct! La respuesta es: {question_data['answer']}"
                question_answered = True
            else:
                result_message = f"Incorrect! Correct answer: {question_data['answer']}"
        else:
            result_message = "No answer detected."

    def next_dialogue():
        """Avanza al siguiente diálogo si hay más preguntas."""
        nonlocal current_quest, question_answered, result_message
        if current_quest < len(questions) - 1:
            current_quest += 1
            question_answered = False
            result_message = ""

    def game_loop():
        nonlocal button_pressed
        running = True
        while running:
            screen.blit(background_image, (0, 0))
            screen.blit(character_image, (50, 150))

            if current_quest < len(questions):
                question_data = questions[current_quest]
                draw_text(question_data["question"], font, BLACK, 50, 50)

                mic_rect = pygame.Rect(350, 500, 50, 50)
                arrow_rect = pygame.Rect(700, 250, 50, 50)

                draw_button_background(350, 500)
                draw_button_background(700, 250)

                screen.blit(microphone_image, mic_rect.topleft)
                screen.blit(arrow_image, arrow_rect.topleft)
            else:
                draw_text("Fin del juego", font, BLACK, 50, 50)

            if result_message:
                draw_text(result_message, font, BLACK, 50, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not button_pressed:
                    if mic_rect.collidepoint(event.pos):
                        ask_voice_question(questions[current_quest])
                        button_pressed = True
                    elif arrow_rect.collidepoint(event.pos) and question_answered:
                        next_dialogue()
                        button_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    button_pressed = False

            pygame.display.update()
            pygame.time.Clock().tick(60)

    game_loop()

speech_game()
