import pygame
import random

#height and width of the window in which animation will run
WIDTH = 1200
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))

#declaring the colors that will be used 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# this method will only draw the bars on the given window
def draw(bars, total_bars, bars_width):
	for i in range(total_bars):
		pygame.draw.rect(win, WHITE, (i * bars_width , HEIGHT - bars[i], bars_width	- 1, bars[i]))

def lomuto_partition(bars, l, h, total_bars, bars_width):
	pivot = bars[h]
	i = l - 1
	j = l

	while(j <= h):
		if bars[j] < pivot:
			i += 1
			temp = bars[i]
			bars[i] = bars[j]
			bars[j] = temp
		win.fill(BLACK)
		draw(bars, total_bars, bars_width)
		pygame.display.update()

		j += 1

	temp = bars[i + 1]
	bars[i + 1] = bars[h]
	bars[h] = temp
	win.fill(BLACK)
	draw(bars, total_bars, bars_width)
	pygame.display.update()

	return i + 1

#sorting function
def quick_sort(bars, l, h, total_bars, bars_width):
	win.fill(BLACK)
	draw(bars, total_bars, bars_width)
	pygame.display.update()
	if l < h:
		p = lomuto_partition(bars, l, h, total_bars, bars_width)
		win.fill(BLACK)
		draw(bars, total_bars, bars_width)
		pygame.display.update()
		quick_sort(bars, l, p - 1, total_bars, bars_width)
		quick_sort(bars, p + 1, h, total_bars, bars_width)

def main():

	# width of single bar displayed, indirectly proportional to number of bars
	bars_width = 3

	total_bars = WIDTH // bars_width

	bars = [] # list that will contain the height of the bars

	for i in range(0, total_bars):
		bars.append(random.randrange(10, HEIGHT - 5, 1))
		#randomizing the bars_height from 10 to 590 with 1 as a step

	draw(bars, total_bars, bars_width)
	pygame.display.update()

	# printing elements before sorting
	print(bars)

	quick_sort(bars, 0, total_bars - 1, total_bars, bars_width)

	#time after which the pygame window will be closed autometically
	pygame.time.delay(5000)

	#printing elemetns after sorting 
	print(bars)

main()