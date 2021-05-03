import pygame, os, time
SIZE = DISP_W, DISP_H = 1280, 720
WIN = pygame.display.set_mode((SIZE), 0, 32)

#Colours
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

box_image = pygame.image.load(os.path.join("player.png"))
enemy_box_image = pygame.image.load(os.path.join("enemy.png"))

class Player_Box:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.velocity = 2
    
    def draw(self):
        WIN.blit(self.image, (self.x, self.y))
    
    def move_left(self):
        self.x -= self.velocity
    
    def move_right(self):
        self.x += self.velocity
    
    def move_up(self):
        self.y -= self.velocity
    
    def move_down(self):
        self.y += self.velocity
    
    def attack(self):
        print("I'm attacking trust me bro")


def main():
    box = Player_Box(50, 50, box_image)
    enemy_box = Player_Box(DISP_W-50, 50, enemy_box_image)
    
    def update_display():
        WIN.fill(white)
        box.draw()
        enemy_box.draw()
        pygame.display.update()
    
    def check_key_input():
        enemy_box.move_left()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and box.x > 0:
            box.move_left()
        if keys[pygame.K_RIGHT] and box.x < DISP_W - box.width:
            box.move_right()
        if keys[pygame.K_UP] and box.y > 0:
            box.move_up()
        if keys[pygame.K_DOWN] and box.y < DISP_H - box.height:
            box.move_down()
        if keys[pygame.K_SPACE]:
            box.attack()

    #Main, main loop
    while True:
        update_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        check_key_input()
