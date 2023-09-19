import pygame
from sys import exit

pygame.init()  # needs to start pygame

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surface = pygame.image.load("bg_homepage.jpg").convert()
text_surface = test_font.render("Avantha Fonseka FTW", False, "White")
snail_surface = pygame.Surface((100, 100))
snail_surface.fill("White")

player_surface = pygame.Surface((100, 100))
player_surface.fill("Blue")

x_pos = 0

while True:  # We need to keep the file running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # closes the pygame
            exit()

    screen.blit(test_surface, (0, 0))
    screen.blit(text_surface, (300, 400))
    screen.blit(snail_surface, (x_pos, 100))
    screen.blit(player_surface, (300, 100))

    x_pos += 1

    if x_pos > 1600:
        x_pos = 0

    pygame.display.update()
    clock.tick(300)

    mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

        # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Jump")

    # if player_rect.colliderect(ball_rect):
    #     print("Collision")

    # mouse_pos = pygame.mouse.get_pos()

    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
