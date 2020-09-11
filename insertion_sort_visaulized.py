import pygame
import random

WIDTH = 800
HEIGHT = 400

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selection Sort visualizer")


class Bar:
	def __init__(self, height, pos, color):
		self.height = height
		self.pos = pos
		self.color = color

	def get_height(self):
		return self.height

	def get_pos(self):
		return self.pos

	def get_color(self):
		return self.color

	def set_height(self, height):
		self.height = height

	def set_pos(self, pos):
		self.pos = pos

	def set_color(self, color):
		self.color = color


def createGraph(bar_no, bar_width):
	bars = []
	for i in range(bar_no):
		h = random.randrange(10, 390, 5)
		b = Bar(h, i * bar_width, (100, 100, 100))
		bars.append(b)

	return bars

def draw_bar(win, height, pos, bar_width, color):
	pygame.draw.rect(win, color, (pos + 1, 401 - height, bar_width - 1, height))

def draw(win, bars, bar_width):
	
	win.fill((250, 250, 250))
	for bar in bars:
		draw_bar(win, bar.get_height(), bar.get_pos(), bar_width, bar.get_color())
	pygame.display.update()

def main(win, width):
	bar_width = 5

	bar_no = width // bar_width

	run = True

	bars = createGraph(bar_no, bar_width)
	draw(win, bars, bar_width)


	i = 0

	while run:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		if i >= bar_no:
			continue


		key = bars[i].get_height()
		bars[i].set_color((100, 100, 100))

		j = i - 1
		while j >= 0 and bars[j].get_height() > key:
			bars[j + 1].set_height(bars[j].get_height())

			bars[j + 1].set_color((250, 0, 0))
			draw(win, bars, bar_width)
			bars[j + 1].set_color((100, 100, 100))
			j -= 1

		draw(win, bars, bar_width)

		#bars[i].set_color((250, 0, 0))
		bars[j + 1].set_height(key)
		i += 1



	pygame.quit()

main(WIN, WIDTH)
