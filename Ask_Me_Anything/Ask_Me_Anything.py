import sys
import pygame
import pygame.font
import pygame.mixer
def run_game():
	#soundcheck
	pygame.mixer.init()
	pygame.mixer.pre_init(44100,16,2,4096)
	#initialize game and create a screen object.
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Ask Me Anything, Really")
	#set background colour
	bg_color = (230, 230, 230)
	#font and sizing
	myfont = pygame.font.SysFont(None, 30)
	#colour
	black = (0, 0, 0)
    #apply to label
	label = myfont.render('Ask me a question!', True, black)
    #create rectangular object
	labelRect = label.get_rect()
    #set the center
	labelRect.center = (1200 // 2, 800 // 2)
    #set background music
	pygame.mixer.music.load("music.mp3") 
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1,0.0)
	#start the main loop for the game
	while True: 
        #Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
        #redraw the screen during each pass through the loop
		screen.fill(bg_color)
        #project label at center coordinate
		screen.blit(label, labelRect)
        #Make the most recently drawn screen visible
		pygame.display.flip()
run_game()