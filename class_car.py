import pygame
import math
import time
import sys
import tkinter as tk

SCREEN_WIGHT, SCREEN_HEIGHT = 1150, 750
car_wight, car_height = 15, 30
car_1_img = pygame.image.load('pics/red-car.png')
car_1 = pygame.transform.scale(car_1_img, (car_wight, car_height))

class Car:
    IMG = car_1
    def __init__(self, max_vel, rotation_vel, start_x, start_y):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_x, start_y
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def reduce(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def collision(self, mask, x=0, y=0):
        car_1_mask = pygame.mask.from_surface(car_1)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_1_mask, offset)
        return poi

    def collision_rect(self, rect):
        car_rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        return car_rect.colliderect(rect)

    def position(self):
        if self.x > SCREEN_WIGHT or self.x < 0:
            leave()
        if self.y > SCREEN_HEIGHT or self.y < 0:
            leave()


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def leave():
    sys.exit()


def laptime():
    starttime = time.time()
    lasttime = starttime
    laptime = str(round((time.time() - lasttime), 2))
    return laptime
