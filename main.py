#Jeux video
import pygame

pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeux video")

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

pygame.quit()