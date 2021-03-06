#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 80
BALL_SIZE = 14


def main():
	goal_distance = 70
	left_goal = goal_distance
	right_goal = WINDOW_WIDTH - goal_distance

	janela = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

	janela.set_title("Pong!")

	left_paddle = Sprite("img/paddle.png")
	right_paddle = Sprite("img/paddle.png")
	ball = Sprite("img/ball.png")
	sep = GameImage("img/sep.png")

	# posições iniciais
	left_paddle.set_position(left_goal - PADDLE_WIDTH, (WINDOW_HEIGHT / 2) - (left_paddle.y / 2))
	right_paddle.set_position(right_goal + PADDLE_WIDTH, (WINDOW_HEIGHT / 2) - (right_paddle.y / 2))
	ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
	sep.set_position(WINDOW_WIDTH / 2, 0)


	# velocidades (Windows)
	paddle_speed = 170
	ball_speed_x = 170
	ball_speed_y = 170
	max_ball_speed = 300
	speed_delta = 3

	ia_right_paddle_speed = 300

	# scores
	left_player = 0
	right_player = 0

	keyboard = Keyboard()

	count = 0

	while True:  # game loop
		time = janela.delta_time()

		if keyboard.key_pressed("ESC"):
			janela.close()
			return

		# movimentos da paddle esquerda
		if keyboard.key_pressed("w"):
			if left_paddle.y >= 0:
				left_paddle.y -= paddle_speed * time


		elif keyboard.key_pressed("s"):
			if left_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				left_paddle.y += paddle_speed * time

		# movimentos da paddle direita
		"""
		if keyboard.key_pressed("UP"):
			if right_paddle.y >= 0:
				right_paddle.y -= paddle_speed * time

		elif keyboard.key_pressed("DOWN"):
			if right_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				right_paddle.y += paddle_speed * time
		"""


		# IA
		if ball.y > left_paddle.y + PADDLE_HEIGHT / 2:
			ia_right_paddle_speed = abs(ia_right_paddle_speed)

		else:
			ia_right_paddle_speed = - abs(ia_right_paddle_speed)


		right_paddle.y += ia_right_paddle_speed * time



		# usando o mouse pra paddle direita
		# right_paddle.set_position(right_paddle.x, mouse.get_position()[1])

		# movimento automático da bola
		# ball.set_position(ball.x + ball_speed_x, ball.y + ball_speed_y)
		ball.x += ball_speed_x * time
		ball.y += ball_speed_y * time


		# colisões com as paddles
		if left_paddle.collided(ball) or right_paddle.collided(ball):
			ball_speed_x = - ball_speed_x

			if (ball.y + BALL_SIZE / 2 > left_paddle.y + PADDLE_HEIGHT / 2) or (ball.y + BALL_SIZE / 2 > right_paddle.y + PADDLE_HEIGHT / 2):
				ball_speed_y = abs(ball_speed_y)

			else:
				ball_speed_y = - abs(ball_speed_y)

		# colisão com a parede esquerda
		if ball.x <= 0:
			"""
			count += 1
			if count % 2 == 0 and ball_speed_x <= max_ball_speed:
				if ball_speed_x >= 0:
					ball_speed_x += speed_delta

				else:
					ball_speed_x -= speed_delta
			"""

			ball_speed_x = - ball_speed_x
			right_player += 1
			print("score: ", left_player, " x ", right_player)
			ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2) # reseta bola para o centro

		# Colisao na parede direita
		if ball.x >= WINDOW_WIDTH:
			"""
			count += 1
			if count % 2 == 0 and ball_speed_x <= max_ball_speed:
				if ball_speed_x >= 0:
					ball_speed_x += speed_delta

				else:
					ball_speed_x -= speed_delta
			"""

			ball_speed_x = - ball_speed_x
			left_player += 1
			print("score: ", left_player, " x ", right_player)
			ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)  # reseta bola para o centro

		# colisões nas paredes superior e inferior
		if ball.y <= 0 or ball.y + BALL_SIZE / 2 >= WINDOW_HEIGHT:
			"""
			count += 1

			if count % 2 == 0 and ball_speed_y <= max_ball_speed:
				if ball_speed_y >= 0:
					ball_speed_y += speed_delta

				else:
					ball_speed_y -= speed_delta
			"""

			ball_speed_y = - ball_speed_y


		janela.set_background_color((0, 0, 0)) # black background
		left_paddle.draw()
		right_paddle.draw()
		sep.draw()
		ball.draw()
		janela.draw_text(str(left_player), WINDOW_WIDTH/2 - 40, 10, size=30, color=(255, 255, 255), font_name="Consolas", bold=True)
		janela.draw_text(str(right_player), WINDOW_WIDTH/2 + 30, 10, size=30, color=(255, 255, 255), font_name="Consolas", bold=True)
		janela.update()

main()
