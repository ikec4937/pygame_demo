import pygame, os, time

SIZE = DISP_W, DISP_H = 1280, 720
WIN = pygame.display.set_mode((SIZE), 0, 32)


def main():
    #Good box :)
    box_image = pygame.image.load(r"D:/Ikechukwu/Coding files/Python/Pygame stuffs/New Super Movement bros/Finished Product/start-assets/player.png")
    box_x = 50
    box_y = 50
    box_width = box_image.get_width()
    box_height = box_image.get_height()
    box_velocity = 2

    #Bad box >:(
    enemy_box_image = pygame.image.load(r"D:/Ikechukwu/Coding files/Python/Pygame stuffs/New Super Movement bros/Finished Product/start-assets/enemy.png")
    enemy_box_x = DISP_W-50
    enemy_box_y = 50
    enemy_box_width = enemy_box_image.get_width()
    enemy_box_height = enemy_box_image.get_height()
    enemy_box_velocity = 2

    
    def update_display():
        WIN.fill((255,255,255))
        WIN.blit(box_image, (box_x, box_y))
        WIN.blit(enemy_box_image, (enemy_box_x, enemy_box_y))
        pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        enemy_box_x -= enemy_box_velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and box_x > 0:
            box_x -= box_velocity
        if keys[pygame.K_RIGHT] and box_x < DISP_W - box_width:
            box_x += box_velocity
        if keys[pygame.K_UP] and box_y > 0:
            box_y -= box_velocity
        if keys[pygame.K_DOWN] and box_y < DISP_H - box_height:
            box_y += box_velocity
        
        update_display()
    
"""
if keys[pygame.K_LEFT] :
            box.move_left()
        if keys[pygame.K_RIGHT] and :
            box.move_right()
        if keys[pygame.K_UP] and :
            box.move_up()
        if keys[pygame.K_DOWN] and :
            box.move_down()
        if keys[pygame.K_SPACE]:
            box.attack()
"""

