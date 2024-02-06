import pygame
import random
from class_car import leave, Car, laptime

pygame.init()
pygame.font.init()
BG = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
SCREEN_WIGHT, SCREEN_HEIGHT = 1150, 750
WIN = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('Race!')

race_track_img = pygame.image.load('pics/race_track.png')
race_track = pygame.transform.scale(race_track_img, (SCREEN_WIGHT, SCREEN_HEIGHT))
race_track_mask = pygame.mask.from_surface(race_track)
finish_line_img = pygame.image.load('pics/finish_line.png')
finish_line = pygame.transform.scale(finish_line_img, (135, 14))
finish_mask = pygame.mask.from_surface(finish_line)
mask = finish_mask.to_surface()


def draw_window(win, track, finish, score_1):
    WIN.fill(BG)
    WIN.blit(race_track, (track.x, track.y))
    WIN.blit(mask, (finish.x, finish.y))
    WIN.blit(score_1, (550, 100))
    player_car.draw(win)
    player_car_2.draw(win)
    pygame.display.update()


start_x, start_y = 50, 325
player_car = Car(6, 2, start_x, start_y)
player_car_2 = Car(6, 2, start_x + 50, start_y)


def main():
    track = pygame.Rect(0, 0, SCREEN_WIGHT, SCREEN_HEIGHT)
    finish = pygame.Rect(25, 360, 500, 750)

    lap_time = laptime()
    font = pygame.font.Font(None, 36)
    score_1 = font.render(lap_time, True, (255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if player_car.collision_rect(finish):
            lap_time = laptime()
            font = pygame.font.Font(None, 36)
            score_1 = font.render(lap_time, True, (255, 255, 255))
            WIN.blit(score_1, (10, 10))
            print('Good')
        else:
            print('Schlecht')

        draw_window(WIN, track, finish, score_1)
        player_car.position()
        player_car_2.position()

        key = pygame.key.get_pressed()
        moved = False

        if key[pygame.K_a]:
            player_car.rotate(left=True)
        if key[pygame.K_d]:
            player_car.rotate(right=True)
        if key[pygame.K_w]:
            moved = True
            player_car.move_forward()
        if key[pygame.K_s]:
            moved = True
            player_car.move_backward()

        if key[pygame.K_LEFT]:
            player_car_2.rotate(left=True)
        if key[pygame.K_RIGHT]:
            player_car_2.rotate(right=True)
        if key[pygame.K_UP]:
            moved = True
            player_car_2.move_forward()
        if key[pygame.K_DOWN]:
            moved = True
            player_car_2.move_backward()

        if not moved:
            player_car.reduce()

        if player_car.collision(race_track_mask) is not None:
            pass
        else:
            leave()
        if player_car_2.collision(race_track_mask) is not None:
            pass
        else:
            leave()


if __name__ == '__main__':
    main()
