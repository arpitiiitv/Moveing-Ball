import pygame
#initializing game
pygame.init()
#setting window size
width=1500
height=300
speed=[1, 1]
#for background color
black=255,255,255
#setting screen for game
gameWindow=pygame.display.set_mode((width,height))
#loading image of ball
ball=pygame.image.load("Ball2.png")

ballrect=ball.get_rect()


game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    
    ballrect=ballrect.move(speed)
    if ballrect.left <0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom > height:
        speed[1]=-speed[1]
    gameWindow.fill(black)
    gameWindow.blit(ball,ballrect)
    pygame.display.flip()
