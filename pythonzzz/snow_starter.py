import pygame
import random

black = (0, 0, 0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init() #this is calling the function that starts the pygame


# Set the width and height of the screen [width, height]
size = (700, 500) #assigning height and width to size of screen
screen = pygame.display.set_mode(size) #creating screen variable and initializing it with parameter

#pygame.display.set_caption("Snow")
#subtitling program "snow"
class SnowFlake():
	def __init__(self, size, position,color):
		self.size_snow = size
		self.position_snow = position
		self.color = color
	def draw(self):
		pygame.draw.circle(screen,self.color,self.position_snow,self.size_snow)
	def fall(self, speed):
		self.position_snow = [self.position_snow[0], self.position_snow[1]+speed]
# Loop until the use clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

speed = 1

#INTIALIZE YOUR SNOWFLAKE HERE

#Snow List
snow_list=[]

#-----Main Program Loop-------
while not done:
   # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	for i in range(5):
		snow_list.append(SnowFlake(random.randint(2,7),[random.randint(0,700),0],(random.randint(100,255),random.randint(100,255),random.randint(100,255))))
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	background_image = pygame.image.load("moose.jpg").convert()
	screen.blit(background_image,[0,0])

	for i in snow_list:
		i.draw()
		i.fall(random.randint(4,5))
	#--Drawing code should go here
	#Begin Snow









	#end Snow
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

#Close the window and quit.
pygame.quit()
