import pygame, os
import colours as col

SIZE = DISP_W, DISP_H = 1280, 720
WIN = pygame.display.set_mode((SIZE), 0, 32)

class Player_Box:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.image = pygame.image.load("player.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.velocity = 4
    
    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

class Any_other_box:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        
    def draw(self, colour):
        pygame.draw.rect(WIN, colour, self.rect)        
    

def main():
    box = Player_Box()
    
    def update_display():
        WIN.fill(col.white)
        box.draw()
        pygame.display.update()
    
    #Main, main loop
    while True:
        update_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and box.x > 0:
            box.x -= box.velocity
        if keys[pygame.K_RIGHT] and box.x < DISP_W - box.width:
            box.x += box.velocity
        if keys[pygame.K_UP] and box.y > 0:
            box.y -= box.velocity
        if keys[pygame.K_DOWN] and box.y < DISP_H - box.height:
            box.y += box.velocity
        
def start_screen():
    starter_box = Any_other_box((DISP_W/2-200), 450, 400, 100)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

            WIN.fill(col.white)
            starter_box.draw(col.red)
            pygame.display.update()

start_screen()
