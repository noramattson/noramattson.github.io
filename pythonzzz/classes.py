import random
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snow")

done = False

clock = pygame.time.Clock()

class snowflake:
    def __init__(self, size):
        self.size = size
    #    self.location = location
        self.location = location = [random.randint(0,700),0]
    def normalsnowfall(self, speed):
        self.location = [self.location[0], self.location[1]+speed]
snowy = snowflake(10)
while not done:
	snowy.normalsnowfall(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pygame.draw.circle(screen, BLUE, snowy.position, snowy.size)
# nora = snowflake(5)
# nadia = snowflake(10)
# nadia.normalsnowfall(10)
# print(nadia.size)
pygame.quit()
exit()
