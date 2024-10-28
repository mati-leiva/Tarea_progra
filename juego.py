import pygame
import sys
import pygame.locals as pl
import numpy as np



class Player:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 2.
        self.vel_y = 2.
        self.rect = (self.pos_x,self.pos_y,20,20)
        
    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.pos_x ,self.pos_y,20,20))
    
    def movement(self):
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
        
    def velocity_limit(self):
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=4.:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 
        
    def update_position(self):
        
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

class Point:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0.
        self.vel_y = 0.
        self.color = GREEN
      
    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, self.color, (self.pos_x ,self.pos_y,20,20))    

    def direction_to_char(self,x,y):
            
        dir_x = (x - self.pos_x) 
        dir_y = (y - self.pos_y) 
        
        vec_pos = np.array([dir_x, dir_y])
        vel = np.array(vec_pos)/((vec_pos**2).sum()**0.5)
        
        Point.velocity_limit(self)
        
        self.vel_x += vel[0]
        self.vel_y += vel[1]
        
        Point.update_position(self)

    def velocity_limit(self):
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=2.5:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 

    def update_position(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
    
    def colide(self, x, y):
        player = [x,y]  
        rect = pygame.Rect((self.pos_x ,self.pos_y,25,25))
        self.color = GREEN if rect.collidepoint(player) else RED


def display_game():
    # We display a colection of points
    Point_1 = Point(200,200)
    Player_1 = Player(100,100)
    
    while True:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                    pygame.quit()
                    sys.exit()
                    
        DISPLAYSURF.fill(WHITE)   
        Point_1.draw_point()
        Player_1.draw_point()
            
        Player_1.movement()
        Point_1.direction_to_char(Player_1.pos_x,Player_1.pos_y)
        Point_1.colide(Player_1.pos_x,Player_1.pos_y)    
        
        pygame.display.update()
        clock.tick(60)
            
# Starting the colors
BLACK = (10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (31, 255,   10)
BLUE = (10,   10, 255)

# Seting up the display
width, height = 400, 400


DISPLAYSURF = pygame.display.set_mode((width,height),0, 32)
clock = pygame.time.Clock()  
pygame.display.set_caption("hello World")
# Starting the game

display_game()