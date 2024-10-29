import pygame
import sys
import pygame.locals as pl
import numpy as np


class Player: #Se genera un objeto para funcionar como avatar del jugador
    def __init__(self, pos_x, pos_y): #Define los atributos iniciales del jugador
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 2.
        self.vel_y = 2.
        self.rect = (self.pos_x,self.pos_y,20,20)
        
    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.pos_x ,self.pos_y,20,20))
    
    def movement(self): #Cambia el atributo de velocidad del jugador según las teclas presionadas
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
        
    def velocity_limit(self): #Define un limite del atributo velocidad
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=4.:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 
        
    def update_position(self): #Cambia el atributo de posición según el atributo de velocidad, con un maximo y minimo
        
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


class Point: #Se define el objeto a usar como enemigo/objetivo del juego
    def __init__(self, pos_x, pos_y): #Define atributos de condiciones iniciales
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0.
        self.vel_y = 0.
        self.color = GREEN
      
    def draw_point(self): 
        pygame.draw.circle(DISPLAYSURF, self.color, (self.pos_x ,self.pos_y),10)    

    def direction_to_char(self,x,y): #Metodo con entrada que incluira la posición del jugador para dirigirse a este
            
        dir_x = (x +10- self.pos_x) 
        dir_y = (y +10- self.pos_y) 
        
        vec_pos = np.array([dir_x, dir_y])
        vel = np.array(vec_pos)/((vec_pos**2).sum()**0.5)
        
        Point.velocity_limit(self)
        
        self.vel_x += vel[0]
        self.vel_y += vel[1]
        
        Point.update_position(self)

    def velocity_limit(self): #Limita el atributo de velocidad
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=2.5:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 

    def update_position(self): #Cambia atributo posición según atributo velocidad
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
    
    def colide(self, x, y): #Metodo a usar para verificar si los puntos chocan contra jugador
        player = [x+10,y+10]  
        rect = pygame.Rect((self.pos_x,self.pos_y,11,11)) 
        self.color = GREEN if rect.collidepoint(player) else RED


def display_game():
    # We display a colection of points
    time_interval = 500 # 500 milliseconds == 0.1 seconds
    next_step_time = 0
    
    font = pygame.font.Font('Andika-Bold.ttf', 32)
    text = font.render("hola", True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)

    #Inicializa los objetos de jugador y punto
    Point_1 = Point(200,200)
    Player_1 = Player(100,100)
    
    while True:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                    pygame.quit()
                    sys.exit()
        current_time = pygame.time.get_ticks()
        if current_time > next_step_time:
            next_step_time += time_interval
                                
        DISPLAYSURF.fill(WHITE)   
        Point_1.draw_point()
        Player_1.draw_point()
        
        DISPLAYSURF.blit(text, textRect)
        
        Player_1.movement()
        Point_1.direction_to_char(Player_1.pos_x,Player_1.pos_y)
        Point_1.colide(Player_1.pos_x,Player_1.pos_y)    
        
        pygame.display.update()
        clock.tick(60)
        
        
        
pygame.init()
            
#Comenzando los colores
BLACK = (10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (31, 255,   10)
BLUE = (10,   10, 255)

#Preparando el display
width, height = 400, 400



DISPLAYSURF = pygame.display.set_mode((width,height),0, 32)
clock = pygame.time.Clock()  
pygame.display.set_caption("hello World")
# Inicializando el juego

display_game()
