import pygame
import time
from button import Button

class Scene1:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        # create button
        self.button1 = Button(screen, "Quiz", 117,325,140,40, font_size=35, type="rectangle")
        self.button2 = Button(screen, "Wardrobe", 117,390,140,40, font_size=35, type="rectangle")
        self.button3 = Button(screen, "Statistics", 117,455,140,40, font_size=35, type="rectangle")

    def draw_scene(self):
        backgroundimg = pygame.image.load('background.jpeg')
        self.screen.blit(backgroundimg, (-500,-400))
        self.button1.draw()
        self.button2.draw()
        self.button3.draw()
        pygame.display.update()
        
    def check_button_pressed(self, point):
            if self.button1.check_collision(point):
                return "Scene2"
            elif self.button2.check_collision(point):
                return "Scene3"
            elif self.button3.check_collision(point):
                return "Scene4"
            return None