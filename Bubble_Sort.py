import pygame
import random

WIDTH = 500
HEIGHT = 400

GREY = (200, 200, 200)
DARK = (64, 64, 64)
win = pygame.display.set_mode((WIDTH, HEIGHT))


class Bar:
	def __init__(self, height, index):
		self.height = height
		self.index = index

	def get_index(self):
		return self.index

	def get_height(self):
		return self.height


def createGraph(total_bars, width, bar_width):

	bars = []
	for i in range(50):
		h = random.randrange(10, 390, 5)
		b = Bar(h, i * bar_width)
		bars.append(b)

	return bars

def draw_bar(win, height, pos, width):
	pygame.draw.rect(win, DARK, (pos + 1, 400 - height + 1, width - 1, height - 1))

def draw_graph(win, bars, bar_width, total_bars):
	win.fill(GREY)

	for bar in bars:
		draw_bar(win, bar.get_height(), bar.get_index(), bar_width)

	pygame.display.update()


def main(win, width):
	bar_width = 10
	total_bars = width // bar_width

	run = True

	bars = createGraph(width, total_bars, bar_width)

	while run:

		draw_graph(win, bars, bar_width, total_bars)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


	pygame.quit()

main(win, WIDTH)
