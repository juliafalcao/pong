#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *

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

	# velocidades
	paddle_speed = 10
	ball_speed_x = 2
	ball_speed_y = 2

	# scores
	left_player = 0
	right_player = 0


	keyboard = Keyboard()

	loss_count = 0
	max_ball_speed = 0.05 * WINDOW_WIDTH
	increase = 1

	while True: # game loop

		# movimentos da paddle esquerda
		if keyboard.key_pressed("w"):
			if left_paddle.y >= 0:
				left_paddle.set_position(left_paddle.x, left_paddle.y - paddle_speed)

		elif keyboard.key_pressed("s"):
			if left_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				left_paddle.set_position(left_paddle.x, left_paddle.y + paddle_speed)

		# movimentos da paddle direita
		if keyboard.key_pressed("UP"):
			if right_paddle.y >= 0:
				right_paddle.set_position(right_paddle.x, right_paddle.y - paddle_speed)

		elif keyboard.key_pressed("DOWN"):
			if right_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				right_paddle.set_position(right_paddle.x, right_paddle.y + paddle_speed)

		# movimento automático da bola
		ball.set_position(ball.x + ball_speed_x, ball.y + ball_speed_y)

		# colisões com as paddles
		"""
		if left_paddle.collided(ball) or right_paddle.collided(ball):
		    ball_speed_x = 0 - ball_speed_x

		    if (ball.y + BALL_SIZE / 2 > left_paddle.y + PADDLE_HEIGHT / 2) or
				 (ball.y + BALL_SIZE / 2 > right_paddle.y + PADDLE_HEIGHT / 2):
		        ball_speed_y = abs(ball_speed_y)

		    else:
		        ball_speed_y = 0 - abs(ball_speed_y)
		"""

		# colisão com a parede esquerda
		if ball.x <= 0:
			loss_count += 1
			if loss_count % 2 == 0 and ball_speed_x <= max_ball_speed and ball_speed_y <= max_ball_speed:
				if ball_speed_x >= 0:
					ball_speed_x += increase

				else:
					ball_speed_x -= increase

				print("Ball speed: ", ball_speed_x, ball_speed_y)
			ball_speed_x = - ball_speed_x
			
			right_player += 1

			print("SCORE: ", left_player, "x", right_player)
			# ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
			
		# Colisao na parede direita
		if ball.x >= WINDOW_WIDTH:
			loss_count += 1

			if loss_count % 2 == 0 and ball_speed_x <= WINDOW_WIDTH * 0.05 and ball_speed_y <= WINDOW_HEIGHT * 0.05:
				if ball_speed_x >= 0:
					ball_speed_x += increase

				else:
					ball_speed_x -= increase

				print("Ball speed:", ball_speed_x, ball_speed_y)

			ball_speed_x = - ball_speed_x
			left_player += 1

			"""
			print("SCORE: ", left_player, "x", right_player)
			ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
			"""

		# colisões nas paredes superior e inferior
		if (ball.y <= 0) | (ball.y + BALL_SIZE / 2 >= WINDOW_HEIGHT):
			loss_count += 1

			if loss_count % 2 == 0 and ball_speed_x <= WINDOW_WIDTH * 0.05 and ball_speed_y <= WINDOW_HEIGHT * 0.05:
				if ball_speed_y >= 0:
					ball_speed_y += increase
					
				else:
					ball_speed_y -= increase

				print("Ball speed: ", ball_speed_x, ball_speed_y)

			ball_speed_y = - ball_speed_y

			"""
			# ball_speed_y = 0 - ball_speed_y
			"""

		janela.set_background_color((0, 0, 0)) # black background
		# left_paddle.draw()
		# right_paddle.draw()
		sep.draw()
		ball.draw()
		janela.update()


main()