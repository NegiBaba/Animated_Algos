import pygame
import random

#height and width of the window in which animation will run
WIDTH = 1000
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))

#declaring the colors that will be used 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# this method will only draw the bars on the given window
def draw(bars, total_bars, bars_width):
	for i in range(total_bars):
		pygame.draw.rect(win, WHITE, (i * 10 , HEIGHT - bars[i], bars_width - 2, bars[i]))


#sorting function
def quick_sort(bars, l, h):
	

def main():

	# width of single bar displayed, indirectly proportional to number of bars
	bars_width = 10

	total_bars = WIDTH // bars_width

	bars = [] # list that will contain the height of the bars

	for i in range(0, total_bars):
		bars.append(random.randrange(10, 590, 1))
		#randomizing the bars_height from 10 to 590 with 1 as a step

	draw(bars, total_bars, bars_width)
	pygame.display.update()

	quick_sort(bars, 0, total_bars - 1)

main()