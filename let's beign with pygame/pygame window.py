import pygame 
pygame.init()
screen = pygame.display.set_model((400,500))
done = False

while not done:
         for event in pygame.event.get():
                 if event.type == pygame.OUIT:
                         pygame.quit()

pygame.display.flip()