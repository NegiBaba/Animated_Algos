
import pygame
import random

#height and width of the window in which animation will run
WIDTH = 1170
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))

#declaring the colors that will be used 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# this method will only draw the bars on the given window
def draw(bars, total_bars, bars_width):
	for i in range(total_bars):
		pygame.draw.rect(win, WHITE, (i * bars_width , HEIGHT - bars[i], bars_width - 1, bars[i]))

#using hoarse partition 
def hoarse_partition(bars, l, h, total_bars, bars_width):
	pivot = bars[l]
	i = l - 1
	j = h + 1


	while True:
		while i < h:
			i += 1
			if bars[i] >= pivot:
				break

		while j > l:
			j -= 1
			if bars[j] < pivot:
				break

		if i >= j:
			return j

		temp = bars[i]
		bars[i] = bars[j]
		bars[j] = temp


		win.fill(BLACK)
		draw(bars, total_bars, bars_width)
		pygame.display.update()


#sorting function
def quick_sort(bars, l, h, total_bars, bars_width):
	win.fill(BLACK)
	draw(bars, total_bars, bars_width)
	pygame.display.update()
	if l < h:
		p = hoarse_partition(bars, l, h, total_bars, bars_width)

		win.fill(BLACK)
		draw(bars, total_bars, bars_width)
		pygame.display.update()
		quick_sort(bars, l, p, total_bars, bars_width)
		quick_sort(bars, p + 1, h, total_bars, bars_width)

def main():

	# width of single bar displayed, indirectly proportional to number of bars
	bars_width = 3

	total_bars = WIDTH // bars_width

	bars = [] # list that will contain the height of the bars

	curr_height = HEIGHT - 10
	for i in range(0, total_bars):
		#this time lets try something different
		bars.append(curr_height)
		curr_height -= 1.5

	random.shuffle(bars)
	'''
	now this time what i have done is, made a list of integers in decresing order or ramp
	then i have shuffled that list using random.shuffle() method
	'''

	draw(bars, total_bars, bars_width)
	pygame.display.update()

	# printing elements before sorting
	#print(bars)

	quick_sort(bars, 0, total_bars - 1, total_bars, bars_width)

	#time after which the pygame window will be closed autometically
	pygame.time.delay(5000)

	#printing elemetns after sorting 
	#print(bars)
main()