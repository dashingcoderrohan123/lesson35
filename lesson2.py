import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(screen, (0,125,255),(100,100),50)
    
    pygame.draw.circle(screen, (0,125,255),(200,200),50,3)
    pygame.display.flip()