import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

class snowflake():
    
	def __init__(self, size, xcoord, ycoord):
		self.size = size
		self.xcoord = xcoord
		self.ycoord = ycoord
	def normalsnowfall(self, speed):
		self.location = (xcoord, ycoord+speed)
	
	def draw(self):
		pygame.draw.circle(screen, blue, self.location, 100,7)

done = False

clock = pygame.time.clock()
snowy = snowflake(10)

while not done:
	snowy.normalsnowfall(50)
	snowy.draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(white)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
