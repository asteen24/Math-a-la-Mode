import pygame
import os
import sys
from scene1 import Scene1
from scene2 import Scene2
from scene3 import Scene3
from scene4 import Scene4
import time


pygame.init()


res = (720,720)


# opens up a window
screen = pygame.display.set_mode(res)


# Set up the display
WINDOW_SIZE = (375, 667)
screen = pygame.display.set_mode(WINDOW_SIZE)


# Set the caption of the window
pygame.display.set_caption('Scene Switching')


# Create the scenes
scene1 = Scene1(screen)
scene2 = Scene2(screen)
scene3 = Scene3(screen, scene2)
scene4 = Scene4(screen)

# Set the current scene to scene1
current_scene = scene1


while True:
    count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Check if a button is pressed in the current scene
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = current_scene.check_button_pressed(pygame.mouse.get_pos())
            if button == "Scene2":
                current_scene = scene2
            elif button == "Scene1":
                current_scene = scene1
            elif button == "Scene3":
                current_scene= scene3
            elif button == "Scene4":
                current_scene= scene4


    # Draw the background
    #screen.fill(BACKGROUND_COLOR)


    # Draw the current scene
    current_scene.draw_scene()


    # Update the display
    pygame.display.update()