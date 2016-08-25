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

	def __init__(self,size,xcoord,ycoord):
		self.size = size
		self.xcoord = xcoord
		self.ycoord = ycoord
	def draw(self):
		pygame.draw.circle(screen, blue, self.location, self.size, 7)
	def normalsnowfall(self,speed):
		self.ycoord = self.ycoord+self.speed
		self.location = (self.xcoord,self.ycoord)
		return self.location
		
done = False

clock = pygame.time.Clock()
snowy = snowflake(10,100,0)
#snowflake_list = []
while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
	
	
	pygame.display.flip()
	clock.tick(60)
	snowy.normalsnowfall(10)
	snowy.normalsnowfall(10)
	snowy.normalsnowfall(10)
	snowy.normalsnowfall(10)
	snowy.normalsnowfall(10)
	snowy.draw()

pygame.quit()
