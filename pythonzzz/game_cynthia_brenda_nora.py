import pygame
import random
black = (0, 0, 0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()

size = (700, 500) #assigning height and width to size of screen
screen = pygame.display.set_mode(size) #creating screen variable and initializing it with parameter

class Ball():
	def __init__(self, size, position, color):
		self.size = size
		self.position = position
		self.color = color
	def draw(self):
		pygame.draw.circle(screen,self.color,self.position,self.size)
	def fall(self, speed):
		self.position = [self.position[0], self.position[1]+speed]

class Basket():
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, 2000, 0)
#background_image = pygame.image.load("gamebackground.jpg").convert()
# Loop until the use clicks the close button
done = False
brenda = Basket([100,100],green)
#Used to manage how fast the screen updates
clock = pygame.time.Clock()
ball_list = []
ball_list.append(Ball(10,[random.randint(0,700),0],red))
while not done:
    #main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move object over to right
            if event.key == pygame.K_LEFT:
                #move object over to left

    screen.fill(white)

    #screen.blit(background_image,[0,0])
    brenda.draw()
    for i in ball_list:
    	i.draw()
    	i.fall(1)
	#end Snow
	# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

	# --- Limit to 60 frames per second
    clock.tick(60)

#Close the window and quit.
pygame.quit()
