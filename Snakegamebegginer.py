# Required Modules.
import pygame
import sys
import random
from pygame.locals import*
from pygame.math import Vector2 

# Creating The Snake Class.      
class Snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10), Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False
    def draw_snake(self):
        for index,block in enumerate(self.body):
            x_pos=int(block.x*BLOCKSIZE)
            y_pos=int(block.y*BLOCKSIZE)
            block_rect=pygame.Rect(x_pos,y_pos, BLOCKSIZE,BLOCKSIZE)
            SCREEN.blit(SNAKE,block_rect)
            #pygame.draw.rect(SCREEN,(180,110,120), block_rect)
    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            
    def add_block(self):
        self.new_block=True
            
# Creating The Food Class.          
class Food:
    def __init__(self):
        self.randomize()
    def draw_food(self):
        food_rect=((int(self.pos.x*BLOCKSIZE),int(self.pos.y*BLOCKSIZE),BLOCKSIZE,BLOCKSIZE))
        SCREEN.blit(APPLE,food_rect)
        #pygame.draw.rect(SCREEN,(126,166,114),food_rect)
    def randomize(self):
        self.x=random.randint(0,BLOCKSIZE-1)
        self.y=random.randint(0,BLOCKSIZE-1)
        self.pos=Vector2(self.x,self.y)
        
# Creating The Main Class.
class Main:
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_border()
    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()
    def check_collision(self):
        if self.food.pos==self.snake.body[0]:
            ATE_SOUND.play()
            
            self.food.randomize()
            self.snake.add_block()
    def check_border(self):
        if not 0<=self.snake.body[0].x<BLOCKNUMBER or not 0<=self.snake.body[0].y<BLOCKNUMBER:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
    def draw_score(self):
        score_text=str(len(self.snake.body)-3)
        score_surface=GAME_FONT.render(score_text,True,(56,74,12))
        score_x=int(BLOCKNUMBER*BLOCKSIZE-60)
        score_y=int(BLOCKNUMBER*BLOCKSIZE-60)
        score_rect==score_surface.get_rect(center=(score_x,scorey))
        SCREEN.blit(score_surface,score_rect)
# Initlizing The Pygame Module.                        
pygame.init()
# Creating The Main Background Screen.
BLOCKNUMBER=30
BLOCKSIZE=20
SCREEN=pygame.display.set_mode((BLOCKNUMBER*BLOCKSIZE,BLOCKNUMBER*BLOCKSIZE),pygame.SCALED|pygame.FULLSCREEN)
CLOCK=pygame.time.Clock()
GAME_FONT=pygame.font.Font("Raleway-Regular.ttf",20)
#Image Surfaces.
SNAKE=pygame.image.load("Block.png")
SNAKE=pygame.transform.scale(SNAKE,(25,25))
APPLE=pygame.image.load("apple.png").convert_alpha()

ATE_SOUND=pygame.mixer.Sound("crunch.wav")

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game=Main()

# Main Game Loop.
while True:
    for event in pygame.event.get():
        if event.type==QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        if event.type==SCREEN_UPDATE:
                main_game.update()
        if event.type==KEYDOWN and (event.key== K_2 or event.key==K_UP) or event.type == MOUSEBUTTONDOWN:
            if main_game.snake.direction.y!=1:
                main_game.snake.direction=Vector2(0,-1)
                
        if event.type==KEYDOWN and (event.key==K_4 or event.key==K_RIGHT) or event.type==MOUSEBUTTONDOWN:
            if main_game.snake.direction.x!=1:
                main_game.snake.direction=Vector2(1,0)
                
        if event.type==KEYDOWN and (event.key==K_6 or event.key==K_DOWN) or event.type== MOUSEBUTTONDOWN:
            if main_game.snake.direction.y!=-1:
                main_game.snake.direction=Vector2(0,1)
                
        if event.type==KEYDOWN and (event.key==K_8 or event.key==K_LEFT) or event.type==MOUSEBUTTONDOWN:
            if main_game.snake.direction.x!=1:
                main_game.snake.direction=Vector2(-1,0)
                
    SCREEN.fill((128,128,128))    
    main_game.draw_elements()
    pygame.display.update()
    CLOCK.tick(30)