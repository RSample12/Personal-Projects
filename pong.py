# Riley Sample
# Pong.py
# Practice using pygame: creating simple pong game
# Created: 4/16/22
# Last edited: 4/16/22

import pygame as pg
import sys, random

# init pygame
pg.init()
clock = pg.time.Clock()

# global variables
width = 1280
height = 720
ball_speedx = 7
ball_speedy = 7
paddle_speed1 = 0
paddle_speed2 = 0
score = [0, 0]

# color = (r, g, b)
white = (255, 255, 255)
lt_grey = (200, 200, 200)
random_color = (140, 56, 245)
bg_color = (20, 20, 20)
bg_color_2 = (40, 40, 40)

# display setup
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pong")

# game objects/ rects
# pygame.Rect(x coord, y coord, width, height)
ball = pg.Rect(width / 2 - 7.5, height / 2 - 7.5, 15, 15)
player1 = pg.Rect(15, height / 2 - 55, 5, 110)
player2 = pg.Rect(width - 15, height / 2 - 55, 5, 110)
half_line = pg.Rect(width / 2 - 1.5, 0, 3, 1280)
half_circle = pg.Rect(width / 2 - 200, height / 2 - 200, 400, 400)
half_circle2 = pg.Rect(width / 2 - 197.5, height / 2 - 197.5, 395, 395)
pong_text = pg.font.Font('freesansbold.ttf', 32)
other_text = pg.font.Font('freesansbold.ttf', 32)


def update_score(player):
    global ball_speedx, score

    ball.x = width / 2 - 7.5
    ball.y = height / 2 - 7.5

    if player == 1:
        score[1] += 1
    elif player == 2:
        score[0] += 1
    ball_speedx *= -1

    if score[0] == 7:
        print(score)
        print("Game Over, player 1 wins.")
        sys.exit()
    if score[1] == 7:
        print(score)
        print("Game Over, player 2 wins.")
        sys.exit()

    print(score)


def draw_starting_screen():
    pass


def draw_rects():
    screen.fill(bg_color)
    pg.draw.ellipse(screen, bg_color_2, half_circle)
    pg.draw.ellipse(screen, bg_color, half_circle2)
    pg.draw.rect(screen, bg_color_2, half_line)
    pg.draw.rect(screen, lt_grey, player1)
    pg.draw.rect(screen, lt_grey, player2)
    pg.draw.ellipse(screen, random_color, ball)


def player_movement():
    global paddle_speed1, paddle_speed2

    if event.type == pg.KEYDOWN:
        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= height:
            player1.bottom = height
        if event.key == pg.K_w:
            paddle_speed1 -= 7
        if event.key == pg.K_s:
            paddle_speed1 += 7
        if event.key == pg.K_UP:
            paddle_speed2 -= 7
        if event.key == pg.K_DOWN:
            paddle_speed2 += 7

    if event.type == pg.KEYUP:
        if event.key == pg.K_w:
            paddle_speed1 += 7
        if event.key == pg.K_s:
            paddle_speed1 -= 7
        if event.key == pg.K_UP:
            paddle_speed2 += 7
        if event.key == pg.K_DOWN:
            paddle_speed2 -= 7


def ball_animate():
    global ball_speedx, ball_speedy

    player1.y += paddle_speed1
    player2.y += paddle_speed2
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        update_score(1)
    if ball.right >= width:
        update_score(2)

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1
        ball_speedx += 2


def player2_ai():
    pass


# game loop
while True:

    # handles input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # player v player movement
        player_movement()
        # player v ai movement

    # draws rects on screen
    draw_rects()
    # animate rects
    ball_animate()

    # draws screen and sets fps
    pg.display.flip()
    clock.tick(60)
