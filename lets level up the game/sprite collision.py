import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()
background_image = pygame.transform,scale(pygame.imageload("download (6).jpg"),(SCREEN_WEIGHT, SCREEN_HEIGHT))
 
font = pygame.font.SysFont("Times New Roman",FONT_SIZE)
class Spirte(pygame.sprite.Sprite):
     
     def __init__(self,color,height,width):
         super().__init()
         self.image = pygame.Surface([width,height])
         self.rect = self.image.get_rect()
     def move(self,x_change, y_change):
         self.rect.X = max(min(self.rect)