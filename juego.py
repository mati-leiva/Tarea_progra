import pygame
import sys
import pygame.locals as pl
import numpy as np



class Player:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 1.
        self.vel_y = 1.
    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.pos_x ,self.pos_y,20,20))
    
    def movement(self):
        if pygame.key.get_pressed()[pl.K_a]:
            self.vel_x -= 0.1
        if pygame.key.get_pressed()[pl.K_d]:
            self.vel_x += 0.1
        if pygame.key.get_pressed()[pl.K_w]:
            self.vel_y -= 0.1
        if pygame.key.get_pressed()[pl.K_s]:
            self.vel_y += 0.1     
            
        self.velocity_limit()
        self.update_position() 
        
        
    def velocity_limit(self):
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=3.:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 
        
    def update_position(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        




class Point:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0.
        self.vel_y = 0.
      
    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, GREEN, (self.pos_x ,self.pos_y,20,20))

    def direction_to_mouse(self):
        [pos_x_mouse,pos_y_mouse]=pygame.mouse.get_pos()    
        dir_x = (pos_x_mouse - self.pos_x) 
        dir_y = (pos_y_mouse - self.pos_y) 
        
        vec_pos = np.array([dir_x, dir_y])
        vel = np.array(vec_pos)/((vec_pos**2).sum()**0.5)
        
        Point.velocity_limit(self)
        
        self.vel_x += vel[0]
        self.vel_y += vel[1]
        
        Point.update_position(self)

    
    def velocity_limit(self):
        if (np.array([self.vel_x,self.vel_y])**2).sum()**0.5>=5.:
            self.vel_x = self.vel_x * 0.5
            self.vel_y = self.vel_y * 0.5 

    def update_position(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

def display_game():
    # We display a colection of points
    Point_1 = Point(200,200)
    Point_2 = Point(190,190)
    Player_1 = Player(100,100)
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.fill(WHITE)   
        Point_1.draw_point()
        Point_2.draw_point()
        Player_1.draw_point()
        
        Player_1.movement()
        Point_1.direction_to_mouse()
        Point_2.direction_to_mouse()
        pygame.display.update()
        clock.tick(60)
        
# Starting the colors
BLACK = (10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (31, 255,   10)
BLUE = (10,   10, 255)

# Seting up the display
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
clock = pygame.time.Clock()  
pygame.display.set_caption("hello World")
# Starting the game

display_game()