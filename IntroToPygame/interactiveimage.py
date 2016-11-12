import sys, pygame

# Initialize Pygame functions
pygame.init()

# Frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()

# Screen size variables
screenX = 800
screenY = 800

# Create the display surface window
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Interactive Image')

# Load the images and get the rectangles around them
img1 = pygame.image.load('cat.png')
img2 = pygame.image.load('cat2.png')
currentImg = img1
imgRect = currentImg.get_rect()

# Decides whether the image is moving or not depending on if the arrow key is being held down
imgMovingLeft = False
imgMovingRight= False
imgMovingUp = False
imgMovingDown = False

# Starts off the image in the center of the screen
imgRect.centerx = screenX/2
imgRect.centery = screenY/2

speed = 10 # Number of pixels the image moves

# The main game loop
while True:
	screen.fill((255, 255, 255)) # Makes the screen background white

	screen.blit(currentImg, imgRect) # Puts the image onto the display surface

	# The event handling loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				imgMovingRight = True
			elif event.key == pygame.K_LEFT:
				imgMovingLeft = True
			elif event.key == pygame.K_UP:
				imgMovingUp = True
			elif event.key == pygame.K_DOWN:
				imgMovingDown = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				imgMovingRight = False
			elif event.key == pygame.K_LEFT:
				imgMovingLeft = False
			elif event.key == pygame.K_UP:
				imgMovingUp = False
			elif event.key == pygame.K_DOWN:
				imgMovingDown = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			position = pygame.mouse.get_pos()
			if imgRect.collidepoint(position):
				if currentImg == img1:
					currentImg = img2
				else:
					currentImg = img1

	if imgMovingRight and imgRect.right < screenX:
		imgRect.centerx += speed
	if imgMovingLeft and imgRect.left > 0:
		imgRect.centerx -= speed
	if imgMovingUp and imgRect.top > 0:
		imgRect.centery -= speed
	if imgMovingDown and imgRect.bottom < screenY:
		imgRect.centery += speed

	pygame.display.flip() # Update and redraw the screen
	fpsClock.tick(FPS)
