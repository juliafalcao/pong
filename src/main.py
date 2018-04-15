from PPlay.window import *
from PPlay.gameimage import *
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

	janela.set_title("Pong")

	left_paddle = GameImage("../img/paddle.png")
	right_paddle = GameImage("../img/paddle.png")
	ball = GameImage("../img/ball.png")
	sep = GameImage("../img/sep.png")

	left_paddle.set_position(left_goal - PADDLE_WIDTH, (WINDOW_HEIGHT / 2) - (left_paddle.y / 2))
	right_paddle.set_position(right_goal + PADDLE_WIDTH, (WINDOW_HEIGHT / 2) - (right_paddle.y / 2))
	ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
	sep.set_position(WINDOW_WIDTH / 2, 0)

	paddle_speed = 10
	ball_speed_y = 2
	ball_speed_x = 2

	player_1 = 0
	player_2 = 0

	keyboard = Keyboard()

	# ALTERACAO PRO EXERCICIO
	contador = 0

	while True: # game loop
		if keyboard.key_pressed("w"):
			if left_paddle.y >= 0:
				left_paddle.set_position(left_paddle.x, left_paddle.y - paddle_speed)
		elif keyboard.key_pressed("s"):
			if left_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				left_paddle.set_position(left_paddle.x, left_paddle.y + paddle_speed)

		if keyboard.key_pressed("UP"):
			if right_paddle.y >= 0:
				right_paddle.set_position(right_paddle.x, right_paddle.y - paddle_speed)
		elif keyboard.key_pressed("DOWN"):
			if right_paddle.y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
				right_paddle.set_position(right_paddle.x, right_paddle.y + paddle_speed)

		ball.set_position(ball.x + ball_speed_x, ball.y + ball_speed_y)

		# PONG NORMAL
		#if left_paddle.collided(ball) | right_paddle.collided(ball):
		#    ball_speed_x = 0 - ball_speed_x
		#    if (ball.y + BALL_SIZE / 2 > left_paddle.y + PADDLE_HEIGHT / 2) \
		#            | (ball.y + BALL_SIZE / 2 > right_paddle.y + PADDLE_HEIGHT / 2):
		#        ball_speed_y = abs(ball_speed_y)
		#    else:
		#        ball_speed_y = 0 - abs(ball_speed_y)

		# Colisao na parede esquerda
		if ball.x <= 0:
			# ALTERACAO DE EXERCICIO
			contador += 1
			if contador % 2 == 0 and ball_speed_x <= WINDOW_WIDTH * 0.05 and ball_speed_y <= WINDOW_HEIGHT * 0.05:
				if ball_speed_x >= 0:
					ball_speed_x += 0.1
				else:
					ball_speed_x -= 0.1
				print(ball_speed_x, ball_speed_y)
			ball_speed_x = - ball_speed_x
			# PONG NORMAL:
			#player_2 += 1
			#print(player_1, player_2)
			#ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
		# Colisao na parede direita
		if ball.x >= WINDOW_WIDTH:
			# ALTERACAO DE EXERCICIO
			contador += 1
			if contador % 2 == 0 and ball_speed_x <= WINDOW_WIDTH * 0.05 and ball_speed_y <= WINDOW_HEIGHT * 0.05:
				if ball_speed_x >= 0:
					ball_speed_x += 0.1
				else:
					ball_speed_x -= 0.1
				print(ball_speed_x, ball_speed_y)
			ball_speed_x = - ball_speed_x
			# PONG NORMAL:
			#player_1 += 1
			#print(player_1, player_2)
			#ball.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
		# Colisao na parede superior e inferior
		if (ball.y <= 0) | (ball.y + BALL_SIZE / 2 >= WINDOW_HEIGHT):
			# ALTERACAO DE EXERCICIO
			contador += 1
			if contador % 2 == 0 and ball_speed_x <= WINDOW_WIDTH * 0.05 and ball_speed_y <= WINDOW_HEIGHT * 0.05:
				if ball_speed_y >= 0:
					ball_speed_y += 0.1
				else:
					ball_speed_y -= 0.1
				print(ball_speed_x, ball_speed_y)
			ball_speed_y = - ball_speed_y
			# PONG NORMAL
			# ball_speed_y = 0 - ball_speed_y

		janela.set_background_color((0, 0, 0))
		left_paddle.draw()
		right_paddle.draw()
		sep.draw()
		ball.draw()
		janela.update()


main()