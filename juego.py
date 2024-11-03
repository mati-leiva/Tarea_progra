import pygame
import sys
import pygame.locals as pl
import numpy as np
import math


##T¿ODO FUNCINOA GRADKS
class Player:  # Se genera un objeto para funcionar como avatar del jugador
    def __init__(self, pos_x, pos_y):  # Define los atributos iniciales del jugador
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 2.0
        self.vel_y = 2.0
        self.rect = (self.pos_x, self.pos_y, 20, 20)
        self.bullets = 100

    def draw_point(self, ship):
        DISPLAYSURF.blit(ship, (self.pos_x - 10, self.pos_y - 10))

    def movement(
        self,
    ):  # Cambia el atributo de velocidad del jugador según las teclas presionadas
        if pygame.key.get_pressed()[pl.K_a]:
            self.vel_x -= 0.2
        if pygame.key.get_pressed()[pl.K_d]:
            self.vel_x += 0.2
        if pygame.key.get_pressed()[pl.K_w]:
            self.vel_y -= 0.2
        if pygame.key.get_pressed()[pl.K_s]:
            self.vel_y += 0.2
        self.velocity_limit()
        self.update_position()

    def velocity_limit(self):  # Define un limite del atributo velocidad
        if (np.array([self.vel_x, self.vel_y]) ** 2).sum() ** 0.5 >= 4.0:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5

    def show_bullets(self):  # Muestra la cantidad de balas restantes
        font = pygame.font.Font("Andika-Bold.ttf", 10)
        text = font.render(str(self.bullets), True, BLUE, WHITE)
        textRect = text.get_rect()
        textRect.center = (self.pos_x + 10, self.pos_y + 30)
        DISPLAYSURF.blit(text, textRect)

    def shoot(self, lista):  # Metodo para disparar un lasser
        if self.bullets > 0:
            self.bullets -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            lista.append(
                LASSER(
                    self.pos_x, self.pos_y, mouse_x - self.pos_x, mouse_y - self.pos_y
                )
            )

    def update_position(
        self,
    ):  # Cambia el atributo de posición según el atributo de velocidad, con un maximo y minimo

        if 8 < self.pos_x < width - 8:
            self.pos_x += self.vel_x
        elif self.pos_x <= 11:
            self.vel_x = 0
            self.pos_x = 10
        elif self.pos_x >= width - 11:
            self.vel_x = 0
            self.pos_x = width - 10

        if 8 < self.pos_y < height - 8:
            self.pos_y += self.vel_y
        elif self.pos_y <= 11:
            self.vel_y = 0
            self.pos_y = 9
        elif self.pos_y >= height - 11:
            self.vel_y = 0
            self.pos_y = height - 10


############################################################################################################


class Point:  # Se define el objeto a usar como enemigo/objetivo del juego

    def __init__(self, pos_x, pos_y):  # Define atributos de condiciones iniciales
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.color = GREEN

    def draw_point(self):
        DISPLAYSURF.blit(asteroid, (self.pos_x - 15, self.pos_y - 15))

    def direction_to_char(
        self, x, y
    ):  # Metodo con entrada que incluira la posición del jugador para dirigirse a este

        dir_x = x + 10 - self.pos_x
        dir_y = y + 10 - self.pos_y

        vec_pos = np.array([dir_x, dir_y])
        vel = np.array(vec_pos) / ((vec_pos**2).sum() ** 0.5)

        Point.velocity_limit(self)

        self.vel_x += vel[0]
        self.vel_y += vel[1]

        Point.update_position(self)

    def velocity_limit(self):  # Limita el atributo de velocidad
        if (np.array([self.vel_x, self.vel_y]) ** 2).sum() ** 0.5 >= 4.1:
            self.vel_x = self.vel_x * 0.2
            self.vel_y = self.vel_y * 0.2

    def update_position(self):  # Cambia atributo posición según atributo velocidad
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def colide(
        self, x, y
    ):  # Metodo a usar para verificar si los puntos chocan contra jugador
        player = [x + 10, y + 10]
        rect = pygame.Rect((self.pos_x, self.pos_y, 13, 13))
        self.color = GREEN if rect.collidepoint(player) else RED


############################################################################################################


class Consumable:  # Se define un objeto consumible
    def __init__(self, pos_x, pos_y):  # constructor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = BLUE

    def draw_point(self):  # dibujo
        DISPLAYSURF.blit(bullet, (self.pos_x - 10, self.pos_y - 10))

    def colide(self, x, y):  # verifica si el jugador colisiona con el objeto
        player = [x + 11, y + 11]
        rect = pygame.Rect((self.pos_x, self.pos_y, 30, 30))
        if rect.collidepoint(player):
            return True
        return False


############################################################################################################


class LASSER:  # Se define una clase con objeto los laseres disparados por la nave
    def __init__(self, pos_x, pos_y, velp_x, velp_y):  # constructor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = math.cos(math.atan2(velp_y, velp_x)) * 10
        self.vel_y = math.sin(math.atan2(velp_y, velp_x)) * 10

    def draw_lasser(self):  # dibujo
        DISPLAYSURF.blit(fire, (self.pos_x, self.pos_y))

    def update_position_LASSER(self):  # mover a siguiente posicion
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def out_of_bound(self):  # verifica si se encuentra dentro de la pantalla
        if -11 < self.pos_x < 11 or -11 < self.pos_y < 11:
            return False
        return True

    def colide(self, x, y):  # verifica si ha colisionado con un objeto punto
        enemy = [x + 5, y + 5]
        rect = pygame.Rect((self.pos_x, self.pos_y, 25, 25))
        if rect.collidepoint(enemy):
            return True
        return False


############################################################################################################


def display_game():
    # We display a colection of points
    time_interval = 500
    next_step_time = 0

    # Inicializa los objetos de jugador, punto y se genera una lista para contener objetos lasser
    Player_1 = Player(100, 100)
    killed_enemies = 0
    Lista_LASSER = []
    List_Enemies = []
    List_Consumables = []
    continue_game = True
    menu_game = True
    
    
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    pygame.time.set_timer(pygame.USEREVENT + 1, 8000)

    while menu_game:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pl.KEYDOWN:
                if event.key == pl.K_SPACE:
                    menu_game = False
        DISPLAYSURF.blit(background, (0, 0))
        font = pygame.font.Font("Andika-Bold.ttf", 25)
        text = font.render("TAREA DE PROGRAMACION", True, BLUE)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        text2 = font.render("Presiona espacio para jugar", True, BLUE)
        DISPLAYSURF.blit(text, textRect)
        textRect.center = (width // 2, height // 2 + 50)
        DISPLAYSURF.blit(text2, textRect)
        pygame.display.update()
        clock.tick(60)

    while continue_game:
        while True:
            random_angle = np.random.uniform(0, 3.1415 * 2)
            for event in pygame.event.get():
                if event.type == pl.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pl.MOUSEBUTTONDOWN:
                    Player_1.shoot(Lista_LASSER)
                    laser.play()
                if event.type == pygame.USEREVENT:
                    List_Enemies.append(
                        Point(
                            math.cos(random_angle) * 400 + 10,
                            math.sin(random_angle) * 400 + 10,
                        )
                    )
                if event.type == pygame.USEREVENT + 1:
                    List_Consumables.append(
                        Consumable(
                            np.random.randint(0, width), np.random.randint(0, height)
                        )
                    )

            current_time = pygame.time.get_ticks()
            if current_time > next_step_time:
                next_step_time += time_interval

            mx, my = pygame.mouse.get_pos()
            dx, dy = mx - Player_1.pos_x, my - Player_1.pos_y
            angle = math.degrees(math.atan2(-dy, dx)) - 90
            rot_image = pygame.transform.rotate(ship, angle)

            DISPLAYSURF.blit(background, (0, 0))

            Player_1.draw_point(rot_image)
            Player_1.show_bullets()

            # Actualización de posiciones de los objetos
            Player_1.movement()
            for i in List_Consumables:
                i.draw_point()
                if i.colide(Player_1.pos_x, Player_1.pos_y) == True:
                    Player_1.bullets += 10
                    if Player_1.bullets >= 100:
                        Player_1.bullets = 100
                    List_Consumables.remove(i)

            for i in Lista_LASSER:
                i.update_position_LASSER()
                i.draw_lasser()
                if i.out_of_bound == True:
                    Lista_LASSER.remove(i)

            for i in List_Enemies:
                i.draw_point()
                i.direction_to_char(Player_1.pos_x, Player_1.pos_y)
                i.colide(Player_1.pos_x, Player_1.pos_y)
                if i.color == GREEN:
                    Player_1.bullets //= 2
                    List_Enemies.remove(i)
                    hurt.play()
                    continue  # elimina el objeto de la lista y continua con el siguiente

                for j in Lista_LASSER:
                    if j.colide(i.pos_x, i.pos_y):
                        killed_enemies += 1
                        List_Enemies.remove(i)
                        Lista_LASSER.remove(j)
                        break  # Rompe el ciclo for para hacer menos iteraciones

            if Player_1.bullets == 0:
                continue_game = False
                break
                       
            font = pygame.font.Font("Andika-Bold.ttf", 25)
            text = font.render(str(killed_enemies), True, BLUE)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            DISPLAYSURF.blit(text, textRect)
            pygame.display.update()
            clock.tick(60)
            
    while True:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(background, (0, 0))
        font = pygame.font.Font("Andika-Bold.ttf", 50)
        text = font.render("GAME OVER", True, RED)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        DISPLAYSURF.blit(text, textRect)
        pygame.display.update()
        clock.tick(60)


############################################################################################################

pygame.init()

original_ship = pygame.image.load("images/playerShip1_red.png")
ship = pygame.transform.scale(original_ship, (40, 30))

original_asteroid = pygame.image.load("images/meteorBrown_big1.png")
asteroid = pygame.transform.scale(original_asteroid, (25, 25))

original_bullet = pygame.image.load("images/powerupYellow_bolt.png")
bullet = pygame.transform.scale(original_bullet, (20, 20))

original_lasser = pygame.image.load("images/star_silver.png")
fire = pygame.transform.scale(original_lasser, (15, 15))

bg = pygame.image.load("blue.png")
background = pygame.transform.scale(bg, (400, 400))

laser = pygame.mixer.Sound("images/laser.wav")
hurt = pygame.mixer.Sound("images/hurt.wav")

# Comenzando los colores
BLACK = (10, 10, 10)
WHITE = (240, 240, 240)
RED = (255, 10, 10)
GREEN = (31, 255, 10)
BLUE = (10, 10, 255)

# Preparando el display
width, height = 400, 400

DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption("hello World")
# Inicializando el juego

display_game()
