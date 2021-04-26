import pygame
import random

WIDTH = 500
HEIGHT = 400

GREY = (200, 200, 200)
DARK = (0, 0, 0)
win = pygame.display.set_mode((WIDTH, HEIGHT))


class Bar:
	def __init__(self, height, index, color):
		self.height = height
		self.index = index
		self.color = color

	def set_index(self, index):
		self.index = index

	def set_height(self, height):
		self.height = height

	def set_color(self, color):
		self.color = color

	def get_index(self):
		return self.index

	def get_height(self):
		return self.height

	def get_color(self):
		return self.color


def createGraph(total_bars, width, bar_width):

	bars = []
	for i in range(total_bars - 1):
		h = random.randrange(10, 390)
		b = Bar(h, i * bar_width, DARK)
		bars.append(b)

	return bars

def draw_bar(win, height, pos, color, width):
	pygame.draw.rect(win, color, (pos, 400 - height, width, height - 1))

def draw_graph(win, bars, bar_width):
	win.fill(GREY)

	for bar in bars:
		draw_bar(win, bar.get_height(), bar.get_index(), bar.get_color(), bar_width)

	pygame.display.update()
	

def main(win, width):
	bar_width = 5
	total_bars = width // bar_width

	run = True

	bars = createGraph(width, total_bars, bar_width)

	i = 0
	draw_graph(win, bars, bar_width)

	while run:

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		if i >= total_bars:
			continue
		j = 0
		while j < total_bars - 1 - i:

			if bars[j].get_height() > bars[j + 1].get_height():
				bars[j + 1].set_color((255, 0, 0))
				temp = bars[j].get_height()
				bars[j].set_height(bars[j + 1].get_height())
				bars[j + 1].set_height(temp)
			draw_graph(win, bars, bar_width)
			bars[j + 1].set_color((0, 0, 0))
			j += 1
		i += 1

	pygame.quit()

main(win, WIDTH)
