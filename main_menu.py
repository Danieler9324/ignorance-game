import principals_controllers.game_canoa
import principals_controllers.game_formula1
from moviepy.editor import VideoFileClip
from classes.class_button import Button
import principals_controllers
import pygame
import sys

import principals_controllers.game_savana

# Inicialización de Pygame
pygame.init()
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
pygame.display.set_caption("Game Menu")

# Colores y fondo
BG_COLOR = (30, 30, 30)
FONT_COLOR = (255, 255, 255)
HOVER_COLOR = (100, 255, 100)

# Función para obtener la fuente personalizada
def get_font(size):
    return pygame.font.Font("visual/font/PressStart2P-Regular.ttf", size)

# Definir fuentes
TITLE_FONT = get_font(90)
BUTTON_FONT = get_font(70)
SMALL_BUTTON_FONT = get_font(70)
ROUNDS_BUTTON_FONT = get_font(40)

# Cargar el sonido de clic
click_sound = pygame.mixer.Sound("music/click.mp3")
click_sound.set_volume(1.0)

# Cargar las imágenes de vista previa para los botones
image_canoas = pygame.image.load("visual/images/backgrounds_game/fondo_canoas_previ.png")
image_formula1 = pygame.image.load("visual/images/tracks_images/formula1.png")
image_savana = pygame.image.load("visual/images/tracks_images/savana.png")

# Escalar las imágenes (dimensiones más grandes)
image_canoas = pygame.transform.scale(image_canoas, (300, 200))
image_formula1 = pygame.transform.scale(image_formula1, (250, 200))
image_savana = pygame.transform.scale(image_savana, (300, 200))

# Cargar el GIF
clip = VideoFileClip("visual/gifs/background_gifs/el_menu.gif")

# Función para obtener los cuadros del GIF
def get_gif_frames(clip):
    for frame in clip.iter_frames(fps=clip.fps, dtype="uint8"):
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frame_surface = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        yield frame_surface

# Cargar la imagen de fondo del menú de selección de mapas
background_map_menu = pygame.image.load("visual/images/board_backgrounds/background_select_maps.png")
background_map_menu = pygame.transform.scale(background_map_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Submenú de mapas
def map_menu():
    clock = pygame.time.Clock()

    # Tamaños de fuente ajustados
    MAP_TITLE_FONT = get_font(60)  # Tamaño reducido para el título del submenú
    MAP_BUTTON_FONT = get_font(25)  # Tamaño reducido para los botones
    BACK_BUTTON_FONT = get_font(40)

    # Posiciones de los botones de mapas
    map1_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.3)
    map2_pos = (SCREEN_WIDTH // 3 - 150, SCREEN_HEIGHT * 3 // 4)
    map3_pos = (SCREEN_WIDTH * 3 // 4 + 150, SCREEN_HEIGHT * 3 // 4)
    back_button_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    while True:
        # Dibuja el fondo
        SCREEN.blit(background_map_menu, (0, 0))

        # Dibujar el título del submenú
        title_text = MAP_TITLE_FONT.render("Selecciona un mapa", True, FONT_COLOR)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        SCREEN.blit(title_text, title_rect)

        # Dibujar las imágenes encima de los botones
        SCREEN.blit(image_canoas, (SCREEN_WIDTH // 2.1 - 100, SCREEN_HEIGHT // 3.7 - 120))
        SCREEN.blit(image_formula1, (SCREEN_WIDTH // 3.2 - 150 - 100, SCREEN_HEIGHT * 2.4 // 4 - 120))
        SCREEN.blit(image_savana, (SCREEN_WIDTH * 2.9 // 4 + 150 - 100, SCREEN_HEIGHT * 2.4 // 4 - 120))

        # Crear los botones de los mapas
        map1_button = Button("Pista Canoas", map1_pos, MAP_BUTTON_FONT, FONT_COLOR, HOVER_COLOR)
        map2_button = Button("Pista Formula 1", map2_pos, MAP_BUTTON_FONT, FONT_COLOR, HOVER_COLOR)
        map3_button = Button("Pista Savana", map3_pos, MAP_BUTTON_FONT, FONT_COLOR, HOVER_COLOR)
        back_button = Button("Volver", back_button_pos, BACK_BUTTON_FONT, FONT_COLOR, HOVER_COLOR)

        # Dibujar los botones
        for button in [map1_button, map2_button, map3_button, back_button]:
            button.change_color(pygame.mouse.get_pos())
            button.update(SCREEN)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Si se hace click entonces ejecutar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    return  # Volver al menú principal
                if map1_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    pygame.quit()
                    principals_controllers.game_canoa.game_canoas()
                if map2_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    pygame.quit()
                    principals_controllers.game_formula1.game_formula1()
                if map3_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    pygame.quit()
                    principals_controllers.game_savana.game_savana()

        # Actualiza la pantalla
        pygame.display.update()
        clock.tick(60)

# Define la funcion del menu principal
def main_menu():
    clock = pygame.time.Clock()
    # Define el color del texto
    text_color = FONT_COLOR
    title_pos_y = -100
    target_title_y = SCREEN_HEIGHT // 7
    fall_speed = 5.2
    color_switch_time = 0

    # Define las posiciones de los botones
    play_button_pos = -100
    quit_button_pos = -30
    distance_between_buttons = 105

    stop_music_button = Button("Musica", (SCREEN_WIDTH - 185, SCREEN_HEIGHT - 50), SMALL_BUTTON_FONT, FONT_COLOR, HOVER_COLOR)

    # Genera la musica con el mixer de pygame
    pygame.mixer.music.load("music/music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0)
    is_music_playing = True

    gif_frames = get_gif_frames(clip)
    current_frame = next(gif_frames)

    # mientras sea verdadero ejecutar las letras y el fondo
    while True:
        SCREEN.blit(current_frame, (0, 0))
        try:
            current_frame = next(gif_frames)
        except StopIteration:
            gif_frames = get_gif_frames(clip)
            current_frame = next(gif_frames)

        color_switch_time += 0.5
        if color_switch_time > 30:
            text_color = (255, 0, 0) if text_color == FONT_COLOR else FONT_COLOR
            color_switch_time = 0

        title_text = TITLE_FONT.render("IGNORANCIA", True, text_color)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, title_pos_y))
        SCREEN.blit(title_text, title_rect)

        if title_pos_y < target_title_y:
            title_pos_y += fall_speed

        if play_button_pos < target_title_y + 150:
            play_button_pos += fall_speed
        if quit_button_pos < target_title_y + 150 + (distance_between_buttons * 2):
            quit_button_pos += fall_speed

        play_button = Button("Jugar", (SCREEN_WIDTH // 2, play_button_pos), BUTTON_FONT, FONT_COLOR, HOVER_COLOR)
        quit_button = Button("Salir", (SCREEN_WIDTH // 2, quit_button_pos), BUTTON_FONT, FONT_COLOR, HOVER_COLOR)

        for button in [play_button, quit_button, stop_music_button]:
            button.change_color(pygame.mouse.get_pos())
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Si hace click el cursor ejecutar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    map_menu()  # Ir al submenú de mapas
                if quit_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()
                if stop_music_button.check_for_input(pygame.mouse.get_pos()):
                    click_sound.play()
                    if is_music_playing:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    is_music_playing = not is_music_playing

        # Actualiza la pantalla
        pygame.display.update()
        clock.tick(clip.fps)

# Iniciar el menú principal
main_menu()