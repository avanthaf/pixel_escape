import pygame
from random import randint
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = font.render(f'Score : {current_time}', False, "Black")
    score_rect = score_surf.get_rect(center=(620, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rec in obstacle_list:
            obstacle_rec.x -= 5

            if obstacle_rec.topleft == 480:
                screen.blit(ball_surface, obstacle_rec)
            else:
                screen.blit(fire_surface, obstacle_rec)

        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list

    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rec in obstacles:
            if player.colliderect(obstacle_rec):
                return False
    return True


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pixel Escape")
clock = pygame.time.Clock()
font = pygame.font.Font('font/DigitalDisco.ttf', 50)
game_active = False
start_time = 0
score = 0

game_surface = pygame.image.load("images/bg_homepage.jpg").convert()

cloud1_surface = pygame.image.load("images/cloud1.png").convert_alpha()
cloud1_rec = cloud1_surface.get_rect(topleft=(0, 50))

cloud2_surface = pygame.image.load("images/cloud1.png").convert_alpha()
cloud2_rec = cloud2_surface.get_rect(topleft=(640, 200))

# Obstacles
ball_surface = pygame.image.load('images/ice_ball.png').convert_alpha()
ball_mask = pygame.mask.from_surface(ball_surface)

fire_surface = pygame.image.load('images/flame.png').convert_alpha()
fire_mask = pygame.mask.from_surface(fire_surface)

obstacle_rest_lits = []


# Player
player_surface = pygame.image.load("images/character_run.png").convert_alpha()
player_rect = player_surface.get_rect(topleft=(60, 383))
player_mask = pygame.mask.from_surface(player_surface)

# Start screen
player_stand = pygame.image.load("images/character_idle.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rec = player_stand.get_rect(center=(640, 360))
player_gravity = 0

start_message = font.render("Pixel Escape!", False, "Black")
start_message_rect = start_message.get_rect(center=(620, 50))

instructions = font.render("Press Enter to start", False, "Black")
instructions_rect = instructions.get_rect(center=(620, 670))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 635:
                if event.key == pygame.K_SPACE:
                    player_gravity = -25

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rest_lits.append(ball_surface.get_rect(
                    topleft=(randint(1500, 1800), 480)))
            else:
                obstacle_rest_lits.append(fire_surface.get_rect(
                    topleft=(randint(1600, 1800), 300)))

    if game_active:
        screen.blit(game_surface, (0, 0))
        score = display_score()

        cloud1_rec.x += 3
        cloud2_rec.x -= 3
        if (cloud1_rec.left >= 1280) and (cloud2_rec.right <= 0):
            cloud1_rec.right = 0
            cloud2_rec.left = 1280

        screen.blit(cloud1_surface, cloud1_rec)
        screen.blit(cloud2_surface, cloud2_rec)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 635:
            player_rect.bottom = 635
        screen.blit(player_surface, player_rect)

        # Obstacle movement
        obstacle_rest_lits = obstacle_movement(obstacle_rest_lits)

        # Collision
        game_active = collisions(player_rect, obstacle_rest_lits)

    else:
        screen.fill('Yellow')
        screen.blit(player_stand, player_stand_rec)
        obstacle_rest_lits.clear()
        player_rect.topleft = (60, 383)
        player_gravity = 0

        score_message = font.render(f'Your Score : {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center=(620, 50))

        if score == 0:
            screen.blit(start_message, start_message_rect)
            screen.blit(instructions, instructions_rect)

        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(instructions, instructions_rect)

    pygame.display.update()
    clock.tick(60)
