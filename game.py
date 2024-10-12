import random

import pygame
import_pygame.freetype


pygame.init()
clock = pygame.time.Clocl()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Flappy Bird')

bird_image = pygame.image.load('images/bird.png')
wall_image = pygame.image.load('images/wall.png')
bird_image = pygame.transform.scale(bird_image, (80,60))
bird_image = pygame.transform.scale(wall_image, (100,00))
wall_rect = bird_image.get.rect()
bird_rect.center = (300, 300)
font = pygame_freetype.Font(None, 30)

bird_speed = 15
gravity = 0.5
jump = 1

wall_group = pygame.sprite.Group()
spawn_wall_event = pygame.USEREVENT
pygame.time.set_timer(spawn_wall_event, 1000)

game_status = "game"


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        global game_status
        self.rect.x -= 10
        if self.rect.colliderect(bird_rect):
            game_status = 'menu'

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_wall_event:
            wall = Wall((1050, random, choice([-50,-100,-150])), wall_image)
            wall_group.add(wall)
            wall = Wall((1050, random, choice([650,700,750])), wall_image)
            wall_group.add(wall)
    screen.fill((100,100,100))        
    is game_status == 'game':
        keys = pygame.key.get.pressed()
        if keys[pygame.K_SPACE]:
            bird_speed -=jump
        bird_speed += gravity
        bird_rect.centery += int(bird_speed)
        screen.blit(bird_image, bird_rect)
        wall_group.update()
        wall_group.draw(screen)
    else:
        font.render_to(screen, (300, 300), 'Game over', (200, 0, 0))

pygame.display.flip()
clock.tick(60)
 

