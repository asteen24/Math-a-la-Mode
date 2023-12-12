# scene4.py

import pygame
from button import Button
from statistics_page import StatisticsPage

class Scene4:
    def __init__(self, screen):
        self.screen = screen
        self.statistics_page = StatisticsPage(screen)
        self.width, self.height= pygame.display.get_surface().get_size()

        # Create the back button
        self.back_button = Button(screen, "<--", 50, 50, 50, 50, (228,128,152), font_size=35, type="circle") 


    def draw_scene(self):
        graphimg = pygame.image.load('graphing.jpg')
        self.screen.blit(graphimg, (0,-100))

        self.back_button.draw()
        self.statistics_page.load_data()
        self.statistics_page.draw_statistics()

        

    def check_button_pressed(self, point):
        if self.back_button.check_collision(point):
            return "Scene1"  # Switch to Scene1 when the "Back" button is clicked
        return None
