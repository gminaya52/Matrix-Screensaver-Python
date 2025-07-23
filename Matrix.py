import pygame
import random
import os
import ctypes # Necesario para hablar con la API de Windows

# --- Configuración Inicial para Múltiples Monitores ---

# 1. Obtenemos el tamaño total del escritorio virtual (todos los monitores)
user32 = ctypes.windll.user32
WIDTH = user32.GetSystemMetrics(78)  # Ancho total
HEIGHT = user32.GetSystemMetrics(79) # Alto total

# 2. Posicionamos la ventana en la esquina superior izquierda del escritorio
#    Esto es por si el monitor principal no es el de más a la izquierda.
LEFT = user32.GetSystemMetrics(76)
TOP = user32.GetSystemMetrics(77)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{LEFT},{TOP}"

# 3. Inicializamos Pygame y creamos la ventana
pygame.init()
# Usamos pygame.NOFRAME para crear una ventana sin bordes que llenará todo.
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Matrix Screensaver - Multi-Monitor")

# --- Colores y Fuentes (esto se queda igual) ---
GREEN = (0, 255, 0)
WHITE = (200, 255, 200) 
FONT_SIZE = 20

try:
    font = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", FONT_SIZE)
except FileNotFoundError:
    font = pygame.font.SysFont('courier new', FONT_SIZE, bold=True)

# --- Caracteres ---
# Usamos Katakana de ancho medio, que es lo más parecido al original
katakana = [chr(i) for i in range(0xFF61, 0xFF9F)]
characters = katakana + [str(i) for i in range(10)] # Añadimos números
columns = WIDTH // FONT_SIZE

# --- Clase para la Línea de Lluvia (Stream) ---
class Stream:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(1, 5)
        self.length = random.randint(15, 40)
        self.chars = []
        self.generate_chars()

    def generate_chars(self):
        # Crea la lista de caracteres para esta línea
        self.chars = [random.choice(characters) for _ in range(self.length)]

    def draw(self):
        # Dibuja la cabeza brillante y la cola verde
        for i, char in enumerate(self.chars):
            y_pos = self.y - (i * FONT_SIZE)
            # Solo dibuja si está dentro de la pantalla
            if 0 <= y_pos < HEIGHT:
                color = WHITE if i == 0 else GREEN
                text_surface = font.render(char, True, color)
                screen.blit(text_surface, (self.x, y_pos))
    
    def update(self):
        self.y += self.speed

        # AJUSTE PRINCIPAL AQUÍ
        # Si la cabeza de la línea (self.y) pasa el final de la pantalla...
        if self.y > HEIGHT:
            # ...la reiniciamos en una posición aleatoria por encima de la pantalla.
            self.y = random.randint(-HEIGHT, 0)
            self.speed = random.uniform(1, 5)
            # Opcional: puedes hacer que la longitud también cambie al reiniciar
            # self.length = random.randint(15, 40)
            # self.generate_chars()

        # Cambiamos un símbolo de la cola de vez en cuando para el parpadeo
        if random.randint(1, 25) == 1:
            index_to_change = random.randint(0, self.length - 1)
            self.chars[index_to_change] = random.choice(characters)

# --- Creación de los Streams ---
streams = [Stream(x=i * FONT_SIZE, y=random.randint(-HEIGHT, 0)) for i in range(columns)]

# --- Bucle Principal ---
running = True
clock = pygame.time.Clock()
# Esta superficie es la clave para el efecto de estela
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill((0, 0, 0)) # Rellena de negro
fade_surface.set_alpha(50)   # Ponle una transparencia media

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # El truco mágico: dibuja la superficie semi-transparente sobre todo
    # Esto hace que lo del fotograma anterior se oscurezca, creando la estela
    screen.blit(fade_surface, (0, 0))

    # Actualiza y dibuja cada línea
    for stream in streams:
        stream.update()
        stream.draw()

    pygame.display.flip()
    # Corre a 60 FPS para un movimiento fluido
    clock.tick(60)

pygame.quit()
