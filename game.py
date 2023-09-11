import pygame
from sys import exit

pygame.init()  # needs to start pygame

screen = pygame.display.set_mode((1500, 1003))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surface = pygame.image.load("bg_homepage.jpg").convert()
text_surface = test_font.render("Avantha Fonseka FTW", False, "White")
snail_surface = pygame.Surface((100, 100))
snail_surface.fill("White")

x_pos = 100

while True:  # We need to keep the file running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # closes the pygame
            exit()

    screen.blit(test_surface, (0, 0))
    screen.blit(text_surface, (300, 400))
    screen.blit(snail_surface, (x_pos, 100))
    x_pos += 1

    if x_pos > 1500:
        x_pos = 0

    pygame.display.update()
    clock.tick(600)
