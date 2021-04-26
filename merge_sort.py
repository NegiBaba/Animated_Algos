import pygame
import random

WIDTH = 1000
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)

sorted = False

def chalo(bars, total_bars, bars_width):
	WIN.fill(BLACK)
	draw(bars, total_bars, bars_width)
	pygame.display.update()


def draw(bars, total_bars, bars_width):
	i = 0
	for bar in bars:
		pygame.draw.rect(WIN, WHITE, (i * bars_width, HEIGHT - bar, bars_width - 2, bar))
		i += 1

def merge(bars, l, m, h, total_bars, bars_width):
	'''WIN.fill(BLACK)
	draw(bars, total_bars, bars_width)
	pygame.display.update()'''

	left = []
	right = []

	n1 = m - l + 1
	n2 = h - m

	for i in range(0, n1):
		left.append(bars[l + i])


	for i in range(0, n2):
		right.append(bars[m + i + 1])

	i = 0
	j = 0
	k = l

	while(i < n1 and j < n2):
		if left[i] < right[j]:
			bars[k] = left[i]
			i += 1
			k += 1
		else:
			bars[k] = right[j]
			k += 1
			j += 1
		#pygame.display.update()
		WIN.fill((0, 0, 0))
		draw(bars, total_bars, bars_width)
		pygame.display.update()
		#print(i, " ", j)

	while(i < n1):
		bars[k] = left[i]
		i += 1
		k += 1
		chalo(bars, total_bars, bars_width)

	while(j < n2):
		bars[k] = right[j]
		j += 1
		k += 1
		chalo(bars, total_bars, bars_width)

def mergeSort(bars, l, h, total_bars, bars_width):
	if(l >= h):
		sorted = True
		return
	else:
		m = (l + h) // 2

		mergeSort(bars, l, m, total_bars, bars_width)
		mergeSort(bars, m + 1, h, total_bars, bars_width)
		merge(bars, l, m, h, total_bars, bars_width)	

def main():

	# this define the number of bars to have in the animation
	bars_width = 5
	# bars_width is indirectly proportional to the number of bars
	total_bars = WIDTH // bars_width

	bars = []
	for i in range(total_bars):
		bars.append(random.randrange(10, 490, 2))

	draw(bars, total_bars, bars_width)
	#print(bars)

	i = 0
	run = True

	while(run):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		if(not sorted):
			mergeSort(bars, 0, total_bars - 1, total_bars, bars_width)
		
	
	pygame.quit()


main()
